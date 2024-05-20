from bianco.requisites.methods import try_nlp


def assert_json_logic(sent: str, expected: dict, mode="prereq"):
    doc, json_logic = try_nlp({}, sent, mode)
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


def test_2():
    sent = "ENEL 471; and one of BMEN 319 or ENGG 319 or ENEL 419."
    jl = {
        "and": [
            {"course": "ENEL471"},
            {
                "courses": {
                    "from": [
                        {"course": "BMEN319"},
                        {"course": "ENGG319"},
                        {"course": "ENEL419"},
                    ],
                    "required": 1,
                }
            },
        ]
    }
    assert_json_logic(sent, jl)


def test_admission_of():
    sent = "MATH 277 and PHYS 259 and admission to a program in Engineering."
    jl = {
        "and": [
            {"course": "MATH277"},
            {"course": "PHYS259"},
            {"admission": "a program in Engineering"},
        ]
    }
    assert_json_logic(sent, jl)


def test_course_number_head_to_subject_code():
    sent = "Biology 315, 72 units and consent of the Department."
    jl = {
        "and": [
            {"course": "BIOL315"},
            {"units": {"required": 72}},
            {"consent": "the Department"},
        ]
    }
    assert_json_logic(sent, jl)


def test_parallel_predicate():
    sent = "Biology 315, 327, 233 or 244.72, 72 units and consent of the Department."
    jl = {
        "and": [
            {
                "or": [
                    {"course": "BIOL315"},
                    {"course": "BIOL327"},
                    {"course": "BIOL233"},
                    {"course": "BIOL244.72"},
                ]
            },
            {"units": {"required": 72}},
            {"consent": "the Department"},
        ]
    }
    assert_json_logic(sent, jl)


def test_simplest_single_course():
    sent = "Biology 371."
    jl = {"course": "BIOL371"}
    assert_json_logic(sent, jl)


def test_ors_minor_with_comma():
    sent = "Chemistry 351; Chemistry 353, or 355."
    jl = {
        "and": [
            {"course": "CHEM351"},
            {"or": [{"course": "CHEM353"}, {"course": "CHEM355"}]},
        ]
    }
    assert_json_logic(sent, jl)


def test_minor_and_list_with_comma():
    sent = "Chemistry 351, and one of 353 or 355."
    jl = {
        "and": [
            {"course": "CHEM351"},
            {
                "courses": {
                    "from": [{"course": "CHEM353"}, {"course": "CHEM355"}],
                    "required": 1,
                }
            },
        ]
    }
    assert_json_logic(sent, jl)


def test_far_subject_code_inference():
    sent = "Film 201 and 3 units from 305 or 321."
    jl = {
        "and": [
            {"course": "FILM201"},
            {
                "units": {
                    "from": [{"course": "FILM305"}, {"course": "FILM321"}],
                    "required": 3,
                }
            },
        ]
    }
    assert_json_logic(sent, jl)


def test_sent_with_dirty_punct():
    sent = "Chemistry 201 or 211; and 203 or 213;, and 351."
    jl = {
        "and": [
            {"or": [{"course": "CHEM201"}, {"course": "CHEM211"}]},
            {"or": [{"course": "CHEM203"}, {"course": "CHEM213"}]},
            {"course": "CHEM351"},
        ]
    }
    assert_json_logic(sent, jl)


def x_units_from_courses_labelled():
    sent = "6 units of courses labelled Biochemistry."
    jl = {"units": {"from": {"course": "BCEM"}, "required": 6}}
    assert_json_logic(sent, jl)
