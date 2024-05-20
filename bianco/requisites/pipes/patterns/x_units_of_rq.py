from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    extract_entity,
    copy_span,
    is_top_match,
)


def x_units_of_rq(
    matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]
):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]

    units_required = int(span[0].text)
    rq = span[-1]
    rq_json_logic = None

    if res := extract_entity(rq, doc._.replacements, doc._.json_logics):
        rq_json_logic = res

    json_logic = {
        "units": {
            "required": units_required,
            "from": rq_json_logic,
        }
    }

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


x_units_of_rq_patterns = [
    [
        {"IS_DIGIT": True},
        {"LEMMA": "unit"},
        {"POS": "ADP", "OP": "+"},
        {"ENT_TYPE": "REQUISITE"},
    ],
]
