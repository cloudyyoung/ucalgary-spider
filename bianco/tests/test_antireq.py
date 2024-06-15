from bianco.requisites.methods import Mode
from bianco.tests.test_prereq import assert_json_logic


def test_a_and_b_or_c():
    sent = (
        "Credit for Computer Science 572 and either 599.77 and 672 will not be allowed."
    )
    jl = {
        "or": [
            {"course": "CPSC572"},
            {"course": "CPSC599.77"},
            {"course": "CPSC672"},
        ]
    }
    assert_json_logic(sent, jl, mode=Mode.ANTIREQ)


def test_simple_anti():
    sent = "Credit for Mathematics 583 and 683 will not be allowed."
    jl = {"or": [{"course": "MATH583"}, {"course": "MATH683"}]}
    assert_json_logic(sent, jl, mode=Mode.ANTIREQ)


def test_and_either():
    sent = "Credit for Data Science 222 and either Zoology 269 or Kinesiology 260 will not be allowed."
    jl = {
        "or": [
            {"course": "DATA222"},
            {"course": "ZOOL269"},
            {"course": "KNES260"},
        ]
    }
    assert_json_logic(sent, jl, mode=Mode.ANTIREQ)


def test_any_one_of():
    sent = "Credit for Data Science 211 and any one of Computer Science 215, 217, 231, 235, Computer Engineering 339, Engineering 233 and Digital Engineering 233 will not be allowed."
    jl = {
        "or": [
            {"course": "DATA211"},
            {
                "courses": {
                    "from": [
                        {"course": "CPSC215"},
                        {"course": "CPSC217"},
                        {"course": "CPSC231"},
                        {"course": "CPSC235"},
                        {"course": "ENCM339"},
                        {"course": "ENGG233"},
                        {"course": "ENDG233"},
                    ],
                    "required": 1,
                }
            },
        ]
    }
    assert_json_logic(sent, jl, mode=Mode.ANTIREQ)
