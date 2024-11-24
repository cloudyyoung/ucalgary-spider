from bson.json_util import dumps, loads
from tqdm import tqdm
from gpt.utils import courses_collection, openai_client

any_of = [
    {"$ref": "#/$defs/and"},
    {"$ref": "#/$defs/or"},
    {"$ref": "#/$defs/units"},
    {"$ref": "#/$defs/consent"},
    {"$ref": "#/$defs/admission"},
    {"$ref": "#/$defs/program"},
    {"type": "string"},
]

faculties = [
    "Faculty of Arts",
    "Faculty of Science",
    "Schulich School of Engineering",
    "Haskayne School of Business",
    "Cumming School of Medicine",
    "School of Architecture, Planning and Landscape",
    "Faculty of Graduate Studies",
    "Faculty of Law",
    "Faculty of Nursing",
    "Faculty of Nursing (Qatar)",
    "Faculty of Kinesiology",
    "Faculty of Social Work",
    "Werklund School of Education",
    "Faculty of Veterinary Medicine",
    "Faculty of Public Policy",
]

response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "requisite_schema",
        "strict": True,
        "schema": {
            "type": "object",
            "required": ["requisite"],
            "additionalProperties": False,
            "properties": {"requisite": {"anyOf": any_of}},
            "$defs": {
                "and": {
                    "type": "object",
                    "description": "A and B",
                    "required": ["and"],
                    "additionalProperties": False,
                    "properties": {
                        "and": {
                            "type": "array",
                            "description": "and",
                            "items": {"anyOf": any_of},
                            "additionalProperties": False,
                        }
                    },
                },
                "or": {
                    "type": "object",
                    "description": "A or B",
                    "required": ["or"],
                    "additionalProperties": False,
                    "properties": {
                        "or": {
                            "type": "array",
                            "description": "or",
                            "items": {"anyOf": any_of},
                            "additionalProperties": False,
                        }
                    },
                },
                "units": {
                    "type": "object",
                    "description": "X units",
                    "required": [
                        "units",
                        "from",
                        "include",
                        "field",
                        "level",
                        "subject",
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "units": {"type": "number", "description": "X units"},
                        "from": {
                            "description": "from a list of courses",
                            "additionalProperties": False,
                            "anyOf": [
                                {"type": "array", "items": {"type": "string"}},
                                {"type": "null"},
                            ],
                        },
                        "include": {
                            "description": "include a list of courses",
                            "additionalProperties": False,
                            "anyOf": [
                                {"$ref": "#/$defs/and"},
                                {"$ref": "#/$defs/or"},
                                {"$ref": "#/$defs/units"},
                                {"type": "array", "items": {"type": "string"}},
                                {"type": "null"},
                            ],
                        },
                        "field": {
                            "description": "field of study",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                        "level": {
                            "description": "course level of study; when suffixed with +, it means at or above the level",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                        "subject": {
                            "description": "subject of study",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                    },
                },
                "consent": {
                    "type": "object",
                    "description": "consent",
                    "required": ["consent"],
                    "additionalProperties": False,
                    "properties": {
                        "consent": {
                            "anyOf": [
                                {"$ref": "#/$defs/faculty"},
                                {
                                    "type": "object",
                                    "description": "consent to a department",
                                    "required": ["department"],
                                    "additionalProperties": False,
                                    "properties": {
                                        "department": {
                                            "type": "string",
                                            "description": "name of the department; exclude 'Department of' prefix",
                                        }
                                    },
                                },
                                {"type": "string", "description": "consent"},
                            ]
                        }
                    },
                },
                "admission": {
                    "type": "object",
                    "description": "admission to a program, a department, or a course",
                    "required": ["admission"],
                    "additionalProperties": False,
                    "properties": {
                        "admission": {
                            "anyOf": [
                                {"$ref": "#/$defs/faculty"},
                                {"$ref": "#/$defs/program"},
                                {
                                    "type": "object",
                                    "description": "admission to a department",
                                    "required": ["department"],
                                    "additionalProperties": False,
                                    "properties": {
                                        "department": {
                                            "type": "string",
                                            "description": "department",
                                        }
                                    },
                                },
                            ]
                        }
                    },
                },
                "faculty": {
                    "type": "object",
                    "description": "a faculty",
                    "required": ["faculty"],
                    "additionalProperties": False,
                    "properties": {
                        "faculty": {
                            "type": "string",
                            "description": "faculty",
                            "enum": faculties,
                        }
                    },
                },
                "program": {
                    "type": "object",
                    "description": "a program",
                    "required": [
                        "program",
                        "faculty",
                        "department",
                        "honours",
                        "type",
                        "degree",
                        "career",
                        "year",
                        "gpa",
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "program": {
                            "description": "the field name of the program; leave null if no specific program name is specified",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                        "faculty": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "enum": faculties,
                                },
                                {"type": "null"},
                            ]
                        },
                        "department": {
                            "description": "department",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                        "honours": {
                            "description": "honours program",
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "null"},
                            ],
                        },
                        "type": {
                            "description": "type of program; eg, major, minor, concentration",
                            "anyOf": [
                                {
                                    "type": "string",
                                    "enum": ["major", "minor", "concentration"],
                                },
                                {"type": "null"},
                            ],
                        },
                        "degree": {
                            "description": "degree name; eg, BSc, BA, BEng, etc",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                        "career": {
                            "description": "career level; eg, undergraduate, master, doctoral",
                            "anyOf": [
                                {
                                    "type": "string",
                                    "enum": ["undergraduate", "master", "doctoral"],
                                },
                                {"type": "null"},
                            ],
                        },
                        "year": {
                            "description": "academic standing",
                            "anyOf": [
                                {
                                    "type": "string",
                                    "enum": [
                                        "first",
                                        "second",
                                        "third",
                                        "fourth",
                                        "fifth",
                                    ],
                                },
                                {"type": "null"},
                            ],
                        },
                        "gpa": {
                            "description": "minimum GPA",
                            "anyOf": [
                                {"type": "number"},
                                {"type": "null"},
                            ],
                        },
                    },
                },
            },
        },
    },
}


def generate_prereq(prereq):
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an admission bot of a university. You are provided with with a course information and its pre-requisite (prereq). You must convert the pre-requisite text into json format. Use full subject name for courses, do not use the capital letters abbreviated name. Try to avoid nested 'and'. No 'units' should be 0.",
            },
            {
                "role": "user",
                "content": prereq,
            },
        ],
        response_format=response_format,  # type: ignore
    )
    json_str = completion.choices[0].message.content

    if json_str is None:
        return None

    json = loads(json_str)
    requisite = json["requisite"]
    if isinstance(requisite, str):
        requisite = {"and": [requisite]}
    return requisite


def slim_json(body):
    if body is None:
        return None
    if isinstance(body, dict):
        return {k: slim_json(v) for k, v in body.items() if v is not None}
    if isinstance(body, list):
        return [slim_json(v) for v in body]
    return body


courses = courses_collection.find(
    {"career": {"$regex": "Undergraduate"}, "active": True, "prereq_json": None}
)
courses = list(courses)

for course in tqdm(courses):
    try:
        prereq = course["prereq"]
        prereq_json = None

        if prereq:
            prereq_json = slim_json(generate_prereq(prereq))

        courses_collection.update_one(
            {"_id": course["_id"]}, {"$set": {"prereq_json": prereq_json}}
        )
    except:
        print(f"Error: {course['subject']} {course['number']}")
