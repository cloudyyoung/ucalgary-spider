from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    copy_span,
    is_top_match,
    extract_entity,
)


def a_and_b_or_c(matcher: Matcher, doc: Doc, i, matches):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]

    a = span[0]
    b = span[2]
    c = span[4]

    if res := extract_entity(a, doc._.replacements, doc._.json_logics):
        a = res

    if res := extract_entity(b, doc._.replacements, doc._.json_logics):
        b = res

    if res := extract_entity(c, doc._.replacements, doc._.json_logics):
        c = res

    json_logic = {"and": [a, {"or": [b, c]}]}
    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


a_and_b_or_c_patterns = [
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": "and"},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": "or"},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ]
]
