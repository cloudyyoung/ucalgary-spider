from bianco.tests.test_prereq import assert_json_logic


def test_a_and_b_or_c():
    sent = (
        "Credit for Computer Science 572 and either 599.77 and 672 will not be allowed."
    )
    jl = {
        "and": [
            {"course": "CPSC572"},
            {"or": [{"course": "CPSC599.77"}, {"course": "CPSC672"}]},
        ]
    }
    assert_json_logic(sent, jl, mode="antireq")
