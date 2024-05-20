from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    copy_span,
    is_longest_match,
)


def x_of_courses(matcher: Matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]

    number_token = span[0]
    switch = {
        "one": 1,
        "two": 2,
        "three": 3,
    }
    number = switch.get(number_token.lemma_, 1)

    courses = [ent for ent in span.ents if ent.label_ == "COURSE"]

    json_logic = {
        "courses": {
            "required": number,
            "from": [{"course": course.lemma_} for course in courses],
        },
    }

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


x_of_courses_patterns = get_dynamic_patterns(
    [
        {"POS": "NUM"},
        {"POS": "ADP", "OP": "+"},
    ],
    [
        {"ENT_TYPE": "COURSE"},
        {"TEXT": {"IN": ["or", ","]}},
    ],
    range(1, 20),
    [
        {"ENT_TYPE": "COURSE"},
    ],
)
