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
                                            "description": "department name",
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
                            "enum": [
                                "Arts",
                                "Science",
                                "Engineering",
                                "Business",
                            ],
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
                                    "enum": [
                                        "Arts",
                                        "Science",
                                        "Engineering",
                                        "Business",
                                    ],
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

courses = courses_collection.find()

# for course in courses[:100]:
#     print(course)

completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an admission bot of a university. You are provided with with some course requisites. You must convert the requisite text into json format.",
        },
        {
            "role": "user",
            # "content": "Digital Engineering 319 and 3 units from Sustainable Systems Engineering 315, Engineering 209 or Economic 209.",
            # "content": "Actuarial Science 327; Statistics 323; 3 units from Mathematics 311, 313, 367 or 375; and 3 units from Computer Science 217, 231, 235 or Data Science 211.",
            # "content": "SGMA 395 or ENTI 317 or 381.",
            # "content": "One of FILM 321 or 323 and one of FILM 331 or 333.",
            # "content": "ENCI 473; and ENGG 319 or ENDG 319.",
            # "content": "ENEL 471; and one of BMEN 319 or ENGG 319 or ENEL 419.",
            # "content": "One of GEOG 211, 251, 253, UBST 253, GLGY 201, 209; and consent of the Department.",
            # "content": "Both MATH 349 and 353; or both MATH 283 and 381; or MATH 267.",
            # "content": "MATH 431 or PMAT 431; MATH 429 or PMAT 429 or MATH 327 or PMAT 427.",
            # "content": "MATH 445 or 447; 3 units of Mathematics in the Field of Mathematics at the 400 level or above.",
            # "content": "MATH 277 and PHYS 259 and admission to a program in Engineering.",
            # "content": "Anthropology 201 and admission to the BSc Anthropology or BSc Archaeology major or Honours programs.",
            # "content": "Anthropology 411 and admission to the Anthropology Honours Program.",
            # "content": "Architecture 504, 506 and admission to the Minor in Architectural Studies or the Master of Architecture Programs.",
            # "content": "Arts and Science Honours Academy 222 or 220 and admission to the Arts and Science Honours Academy.",
            # "content": "Chemistry 351, Biology 311 and admission to a Major offered by the Department of Biological Sciences or the Neuroscience Major or a primary concentration in Biological Sciences in either the Natural Sciences or Environmental Science Major. Or, Chemistry 351, and Medical Science 341, and admission to either the Biomedical Science or Bioinformatics Major.",
            # "content": "Communication and Media Studies 201; and an additional 3 units of a course labelled Communication and Media Studies and admission to a majors or minor program in the Department of Communication, Media and Film and consent of the Department.",
            # "content": "78 units, including Communication and Media Studies 313, 369, 371, 381, and admission to the BA in Communication and Media Studies.",
            # "content": "Communication and Media Studies 595 and admission to the Honours Program.",
            # "content": "Fourth- or fifth-year standing in Schulich School of Engineering and admission to the Biomedical Engineering minor.",
            # "content": "Dance 433 and admission to the BFA Dance program.",
            # "content": "Educational Psychology 661 and admission to a doctoral program in Educational Psychology.",
            # "content": "24 units including at least one of Community Rehabilitation 205 or 209 or admission to BCR program.",
            # "content": "Admission to the MEng with specialization in Software Engineering and completion of Software Engineering for Engineers 692, 693 and 694; or admission to the MEng with specialization in Software Engineering, foundation courses exempt cohort.",
            "content": "Completion of 60 units including 3 units from Political Science 321, 426, 427, 428.",
        },
    ],
    response_format=response_format,  # type: ignore
)

research_paper = completion.choices[0].message.content
print(research_paper)
