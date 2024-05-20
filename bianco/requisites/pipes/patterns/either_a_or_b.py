from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    copy_span,
    is_top_match,
)


def either_a_or_b(
    matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]
):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"or": [{"course": a.lemma_}, {"course": b.lemma_}]}

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


either_a_or_b_patterns = [
    [
        {"LEMMA": "either"},
        {"ENT_TYPE": "COURSE"},
        {"LEMMA": "or"},
        {"ENT_TYPE": "COURSE"},
    ]
]
