from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    copy_span,
    is_top_match,
    extract_entity,
)


def ors_minor(matcher: Matcher, doc: Doc, i, matches):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    predicates = []

    for ent in span.ents:
        if res := extract_entity(ent, doc._.replacements, doc._.json_logics):
            # If both parent and nested logic operator are "or", merge them
            if res.get("or"):
                predicates.extend(res["or"])
            else:
                predicates.append(res)

    if len(predicates) == 1:
        json_logic = predicates[0]
    else:
        json_logic = {"or": predicates}

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


ors_minor_patterns = get_dynamic_patterns(
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
    [
        {"TEXT": {"IN": ["or", ","]}},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
    range(0, 20),
    [
        {"TEXT": ",", "OP": "?"},
        {"TEXT": "or"},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": [","]}, "OP": "?"},
    ],
)
