from gpt.utils import courses_collection, openai_client

response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "requisite_schema",
        "strict": True,
        "schema": {
            "type": "object",
            "required": ["requisite"],
            "additionalProperties": False,
            "properties": {
                "requisite": {
                    "anyOf": [
                        {"$ref": "#/$defs/and"},
                        {"$ref": "#/$defs/or"},
                    ]
                }
            },
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
                            "items": {
                                "anyOf": [
                                    {"$ref": "#/$defs/and"},
                                    {"$ref": "#/$defs/or"},
                                    {"type": "string"},
                                ]
                            },
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
                            "items": {
                                "anyOf": [
                                    {"$ref": "#/$defs/and"},
                                    {"$ref": "#/$defs/or"},
                                    {"type": "string"},
                                ]
                            },
                            "additionalProperties": False,
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
            "content": "Engineering 201 or 212; and Mathematics 275 or Applied Mathematics 217.",
        },
    ],
    response_format=response_format, # type: ignore
)

research_paper = completion.choices[0].message
print(research_paper)
