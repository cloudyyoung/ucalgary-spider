from gpt.utils import courses_collection, openai_client

any_of = [
    {"$ref": "#/$defs/and"},
    {"$ref": "#/$defs/or"},
    {"$ref": "#/$defs/units"},
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
                    "required": ["units"],
                    "additionalProperties": False,
                    "properties": {
                        "units": {
                            "type": "object",
                            "description": "units",
                            "required": ["number", "from", "include"],
                            "additionalProperties": False,
                            "properties": {
                                "number": {
                                    "type": "integer",
                                    "description": "number of units",
                                },
                                "from": {
                                    "type": "array",
                                    "description": "from a list of objects",
                                    "items": {"anyOf": any_of},
                                    "additionalProperties": False,
                                },
                                "include": {
                                    "type": "array",
                                    "description": "include a list of objects",
                                    "items": {"anyOf": any_of},
                                    "additionalProperties": False,
                                },
                            },
                        }
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
            "content": "Digital Engineering 319 and 3 units from Sustainable Systems Engineering 315, Engineering 209 or Economic 209.",
        },
    ],
    response_format=response_format,  # type: ignore
)

research_paper = completion.choices[0].message.content
print(research_paper)
