from tqdm import tqdm

from bianco.requisites.methods import try_nlp

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB

# Only process all active undergraduate courses
dirty_courses = list(
    DIRTY_CATALOG_DB.get_collection("courses").find(
        {"prereq": {"$ne": None}, "career": "Undergraduate Programs", "active": True}
    )
)

# Process all courses
courses_catalog = CATALOG_DB.get_collection("courses")
courses_catalog.delete_many({})


for dirty_course in tqdm(dirty_courses, desc="Courses"):
    course = dirty_course.copy()

    # Process prereq, antireq, coreq
    prereq = course["prereq"]
    antireq = course["antireq"]
    coreq = course["coreq"]

    if prereq:
        doc, json_logic = try_nlp(course, prereq)
        course["prereq"] = json_logic
        course["prereq_text"] = prereq
    else:
        course["prereq"] = None
        course["prereq_text"] = None

    if antireq:
        doc, json_logic = try_nlp(course, antireq, mode="antireq")
        course["antireq"] = json_logic
        course["antireq_text"] = antireq
    else:
        course["antireq"] = None
        course["antireq_text"] = None

    if coreq:
        doc, json_logic = try_nlp(course, coreq)
        course["coreq"] = json_logic
        course["coreq_text"] = coreq
    else:
        course["coreq"] = None
        course["coreq_text"] = None

    course.pop("_id")
    course.pop("requisites")

    # Insert course
    courses_catalog.insert_one(course)