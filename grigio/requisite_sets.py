from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB, process_requisites

requisite_sets = list(DIRTY_CATALOG_DB.get_collection("requisite_sets").find({}))


# Process all course sets
requisite_sets_catalog = CATALOG_DB.get_collection("requisite_sets")
requisite_sets_catalog.delete_many({})

# Fields of study
fields_of_study = CATALOG_DB.get_collection("fields_of_study")
fields_of_study.delete_many({})


for requisite_set in tqdm(requisite_sets, desc="Requisite Sets"):
    requisite_set = requisite_set.copy()

    # Process requisites
    name = str(requisite_set["name"])
    requisites = process_requisites(requisite_set["requisites"])
    requisite_set["requisites"] = requisites

    # Insert course set
    requisite_sets_catalog.insert_one(requisite_set)

    # Insert fields of study
    field_of_study = requisite_set.copy()
    if name.startswith("Courses Constituting the Field of"):
        if len(requisites) == 1:
            requisites = requisites[0]
            field_of_study["requisites"] = requisites
        else:
            raise Exception(f"Multiple requisites for {name}")

        # Get all courses in the field of study
        courses = []
        for rule in requisites["rules"]:
            value = rule.get("value", {"values": []})

            for value in value["values"]:
                courses.extend(value["courses"])

        field_of_study["courses"] = courses
        fields_of_study.insert_one(field_of_study)
