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

for course in courses:
    prereq = course["prereq"]

    if prereq:
        print(prereq)

        result = try_nlp(course, prereq)

        print(result)
        print("")

        courses_prereq.insert_one(
            {"course": course["code"], "prereq_text": prereq, "prereq": result}
        )
