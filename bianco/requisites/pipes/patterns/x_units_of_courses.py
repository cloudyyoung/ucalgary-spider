from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    copy_span,
    is_top_match,
)


def x_units_of_courses(
    matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]
):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]

    units_required = int(span[0].text)
    courses = [ent for ent in span.ents if ent.label_ == "COURSE"]

    json_logic = {
        "units": {
            "required": units_required,
            "from": [{"course": course.lemma_} for course in courses],
        }
    }

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


x_units_of_courses_patterns = get_dynamic_patterns(
    [
        {"IS_DIGIT": True},
        {"LEMMA": "unit"},
        {"POS": "ADP", "OP": "+"},
    ],
    [
        {"ENT_TYPE": "COURSE"},
        {"TEXT": {"IN": ["or", ","]}, "OP": "{1,2}"},
    ],
    range(1, 20),
    [
        {"ENT_TYPE": "COURSE"},
    ],
)
