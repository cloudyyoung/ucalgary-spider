from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB

course_sets = list(DIRTY_CATALOG_DB.get_collection("course_sets").find({}))

# Process all course sets
course_sets_catalog = CATALOG_DB.get_collection("course_sets")
course_sets_catalog.delete_many({})

for course_set in tqdm(course_sets, desc="Course Sets"):
    course_set = course_set.copy()

    # Process courses
    course_list = list(course_set["course_list"])

    courses = DIRTY_CATALOG_DB.get_collection("courses").find(
        {"course_group_id": {"$in": course_list}}
    )

    course_codes = []
    for course in courses:
        course_code = course["code"]
        course_codes.append(course_code)

    course_set["courses"] = course_codes

    course_set.pop("_id")
    course_set.pop("course_list")
    course_set.pop("structure")
    course_set.pop("type")

    # Insert course set
    course_sets_catalog.insert_one(course_set)
