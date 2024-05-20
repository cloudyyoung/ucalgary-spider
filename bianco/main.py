from bianco.requisites.methods import try_nlp
from bianco.requisites.utils import catalog

# Get all courses
courses = list(
    catalog.get_collection("courses").find(
        {"prereq": {"$ne": None}, "career": "Undergraduate Programs", "active": True}
    )
)

courses_prereq = catalog.get_collection("courses_prereq")
courses_prereq.delete_many({})

courses_antireq = catalog.get_collection("courses_antireq")
courses_antireq.delete_many({})

courses_coreq = catalog.get_collection("courses_coreq")
courses_coreq.delete_many({})

for course in courses:
    prereq = course["prereq"]
    antireq = course["antireq"]
    coreq = course["coreq"]

    if prereq:
        doc, json_logic = try_nlp(course, prereq)
        courses_prereq.insert_one(
            {"course": course["code"], "prereq_text": prereq, "prereq": json_logic}
        )

    if antireq:
        doc, json_logic = try_nlp(course, antireq, mode="antireq")
        courses_antireq.insert_one(
            {"course": course["code"], "antireq_text": antireq, "antireq": json_logic}
        )

    if coreq:
        doc, json_logic = try_nlp(course, coreq)
        courses_coreq.insert_one(
            {"course": course["code"], "coreq_text": coreq, "coreq": json_logic}
        )
