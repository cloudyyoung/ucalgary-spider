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
                        {"course": "MATH311"},
                        {"course": "MATH313"},
                        {"course": "MATH367"},
                        {"course": "MATH375"},
                    ],
                    "required": 3,
                }
            },
            {
                "units": {
                    "from": [
                        {"course": "CPSC217"},
                        {"course": "CPSC231"},
                        {"course": "CPSC235"},
                        {"course": "DATA211"},
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


def test_or_list():
    sent = "SGMA 395 or ENTI 317 or 381."
    jl = {"or": [{"course": "SGMA395"}, {"course": "ENTI317"}, {"course": "ENTI381"}]}
    assert_json_logic(sent, jl)


def test_one_of():
    sent = "One of FILM 321 or 323 and one of FILM 331 or 333."
    jl = {
        "and": [
            {
                "courses": {
                    "from": [{"course": "FILM321"}, {"course": "FILM323"}],
                    "required": 1,
                }
            },
            {
                "courses": {
                    "from": [{"course": "FILM331"}, {"course": "FILM333"}],
                    "required": 1,
                }
            },
        ]
    }
    assert_json_logic(sent, jl)


def test_x_units_from():
    sent = "3 units from ENCI 481, ENEE 377 or 519.09."
    jl = {
        "units": {
            "from": [
                {"course": "ENCI481"},
                {"course": "ENEE377"},
                {"course": "ENEE519.09"},
            ],
            "required": 3,
        }
    }
    assert_json_logic(sent, jl)
