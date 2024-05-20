from bianco.requisites.methods import try_nlp


def assert_json_logic(sent, expected):
    doc, json_logic = try_nlp({}, sent)
    assert json_logic == expected


def test_1():
    sent = "Actuarial Science 327; Statistics 323; 3 units from Mathematics 311, 313, 367 or 375; and 3 units from Computer Science 217, 231, 235 or Data Science 211."
    json_logic = {
        "and": [
            {"course": "ACSC327"},
            {"course": "STAT323"},
            {
                "units": {
                    "from": [
                        {"course": "MATH 311"},
                        {"course": "MATH 313"},
                        {"course": "MATH 367"},
                        {"course": "MATH 375"},
                    ],
                    "required": 3,
                }
            },
            {
                "units": {
                    "from": [
                        {"course": "CPSC 217"},
                        {"course": "CPSC 231"},
                        {"course": "CPSC 235"},
                        {"course": "DATA 211"},
                    ],
                    "required": 3,
                }
            },
        ]
    }
    assert_json_logic(sent, json_logic)


def test_x_units():
    sent = "60 units."
    json_logic = {"units": {"required": 60}}
    assert_json_logic(sent, json_logic)
