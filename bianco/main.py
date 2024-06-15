from tqdm import tqdm

from bianco.requisites.methods import Mode, try_nlp
from bianco.requisites.utils import DIRTY_CATALOG_DB, LAB_CATALOG_DB

# Get all courses
courses = list(
    DIRTY_CATALOG_DB.get_collection("courses").find(
        {"career": "Undergraduate Programs", "active": True}
    )
)

courses_prereq = LAB_CATALOG_DB.get_collection("courses_prereq")
courses_prereq.delete_many({})

courses_antireq = LAB_CATALOG_DB.get_collection("courses_antireq")
courses_antireq.delete_many({})

courses_coreq = LAB_CATALOG_DB.get_collection("courses_coreq")
courses_coreq.delete_many({})

for course in tqdm(courses, desc="Courses"):
    prereq = course["prereq"]
    antireq = course["antireq"]
    coreq = course["coreq"]

    if prereq:
        doc, json_logic = try_nlp(course, prereq)
        courses_prereq.insert_one(
            {"course": course["code"], "prereq_text": prereq, "prereq": json_logic}
        )

    if antireq:
        doc, json_logic = try_nlp(course, antireq, mode=Mode.ANTIREQ)
        courses_antireq.insert_one(
            {"course": course["code"], "antireq_text": antireq, "antireq": json_logic}
        )

    if coreq:
        doc, json_logic = try_nlp(course, coreq)
        courses_coreq.insert_one(
            {"course": course["code"], "coreq_text": coreq, "coreq": json_logic}
        )
