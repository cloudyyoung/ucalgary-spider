from gpt.utils import courses_collection, openai_client

any_of = [
    {"$ref": "#/$defs/and"},
    {"$ref": "#/$defs/or"},
    {"$ref": "#/$defs/units"},
    {"$ref": "#/$defs/consent"},
    {"$ref": "#/$defs/admission"},
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
                    "required": ["units", "from", "include", "field", "level"],
                    "additionalProperties": False,
                    "properties": {
                        "units": {"type": "number", "description": "X units"},
                        "from": {
                            "type": "array",
                            "description": "from a list of courses",
                            "items": {"type": "string"},
                            "additionalProperties": False,
                        },
                        "include": {
                            "type": "array",
                            "description": "include a list of courses",
                            "items": {"type": "string"},
                            "additionalProperties": False,
                        },
                        "field": {
                            "type": "string",
                            "description": "field of study",
                        },
                        "level": {
                            "type": "string",
                            "description": "course level of study; when suffixed with +, it means at or above the level",
                        },
                    },
                },
                "consent": {
                    "type": "object",
                    "description": "consent",
                    "required": ["consent"],
                    "additionalProperties": False,
                    "properties": {
                        "consent": {"type": "string", "description": "consent"}
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
                    "required": ["program", "from", "honours", "degree"],
                    "additionalProperties": False,
                    "properties": {
                        "program": {
                            "description": "program",
                            "anyOf": [
                                {"type": "string"},
                                {"type": "null"},
                            ],
                        },
                        "from": {
                            "anyOf": [
                                {"$ref": "#/$defs/faculty"},
                                {"type": "null"},
                            ]
                        },
                        "honours": {
                            "description": "honours program",
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "null"},
                            ],
                        },
                        "degree": {
                            "description": "degree level",
                            "anyOf": [
                                {
                                    "type": "string",
                                    "enum": ["undergraduate", "master", "doctoral"],
                                },
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
            "content": "MATH 277 and PHYS 259 and admission to a program in Engineering.",
        },
    ],
    response_format=response_format,  # type: ignore
)

research_paper = completion.choices[0].message.content
print(research_paper)
