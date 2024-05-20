from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    copy_span,
    is_top_match,
)


def admission_of(matcher: Matcher, doc: Doc, i, matches):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    admission_of = span[2:].text.strip()
    if admission_of.endswith("."):
        admission_of = admission_of[:-1]
    json_logic = {"admission": admission_of}

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


admission_of_patterns = get_dynamic_patterns(
    [
        {"LEMMA": "admission"},
        {"POS": "ADP", "OP": "+"},
    ],
    [
        {"ENT_TYPE": {"NOT_IN": ["COURSE", "REQUISITE"]}},
    ],
    range(1, 200),
    [
        {
            "LEMMA": {"NOT_IN": ["and", "or", ",", ";"]},
            "ENT_TYPE": {"NOT_IN": ["COURSE", "REQUISITE"]},
        },
    ],
)
