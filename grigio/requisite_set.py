import re
from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB

requisite_sets = list(DIRTY_CATALOG_DB.get_collection("requisite_sets").find({}))

# Collections
courses_collection = CATALOG_DB.get_collection("courses")
programs_collection = CATALOG_DB.get_collection("programs")
course_sets_collection = CATALOG_DB.get_collection("course_sets")
requisite_sets_collection = CATALOG_DB.get_collection("requisite_sets")

# Process all course sets
requisite_sets_catalog = CATALOG_DB.get_collection("requisite_sets")
requisite_sets_catalog.delete_many({})


def process_requisites(requisites: list):
    return [process_requisite(requisite) for requisite in requisites]


def process_requisite(requisite: dict):
    type = REQUISITE_TYPE_MAP.get(requisite.get("type", ""))
    if not type:
        raise ValueError(f"Unknown requisite type: {requisite.get('type')}")
    requisite["type"] = type

    rules = requisite.get("rules", [])
    requisite["rules"] = [process_rule(rule) for rule in rules]

    requisite.pop("show_in_catalog")

    return requisite


REQUISITE_TYPE_MAP = {
    "Prerequisite": "prerequisite",
    "Corequisite": "corequisite",
    "Antirequisite": "antirequisite",
    "Completion Requirement": "completion_requirement",
    "Narrative Text": "text",
}


def process_rule(rule: dict):
    condition = rule.get("condition")
    if not condition:
        raise ValueError(f"Unknown condition: {condition}")

    # Convert camel case condition to snake case
    rule["condition"] = re.sub(r"(?<!^)(?=[A-Z])", "_", condition).lower()

    # Process subrules
    sub_rules = rule.get("sub_rules")
    if sub_rules:
        rule["sub_rules"] = [process_rule(sub_rule) for sub_rule in sub_rules]

    value = rule.get("value")
    if isinstance(value, str):
        rule["value"] = value.strip()
    elif isinstance(value, dict):
        rule["value"] = process_rule_value(value)

    return rule


def process_rule_value(value):
    # Convert camel case condition to snake case
    condition = value.get("condition")
    if not condition or condition == "none":
        return None

    value["condition"] = re.sub(r"(?<!^)(?=[A-Z])", "_", condition).lower()
    value["values"] = process_rule_value_values(condition, value.get("values", []))
    return value


def process_rule_value_values(condition: str, values: dict):
    processed_values = []

    # Determine collection
    collection = None
    id_field = None

    if condition == "courses":
        collection = courses_collection
        id_field = "course_group_id"
    elif condition in ["courseSets", "course_sets"]:
        collection = course_sets_collection
        id_field = "id"
    elif condition == "programs":
        collection = programs_collection
        id_field = "program_group_id"
    elif condition in [
        "requirementSets",
        "requirement_sets",
        "requisiteSets",
        "requisite_sets",
    ]:
        collection = requisite_sets_collection
        id_field = "requisite_set_group_id"
    else:
        raise ValueError(f"Unknown condition: {condition}")

    # Process values items
    for value_item in values:
        logic = value_item.get("logic")
        ids = value_item.get("value", [])
        objects = []

        # Process values
        for id in ids:
            object = collection.find_one({id_field: id})
            objects.append(object)

        if len(objects) == 1:
            processed_values.append(objects[0])
        elif len(objects) == 0:
            ...
        else:
            processed_values.append({"logic": logic, "values": objects})

    return processed_values


for requisite_set in tqdm(requisite_sets, desc="Course Sets"):
    requisite_set = requisite_set.copy()

    # Process requisites
    requisites = requisite_set["requisites"]
    requisite_set["requisites"] = process_requisites(requisites)

    # Insert course set
    requisite_sets_catalog.insert_one(requisite_set)
