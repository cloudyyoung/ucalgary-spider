from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    copy_span,
    is_longest_match,
    extract_entity,
)


def ands_minor(matcher: Matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    predicates = []

    for ent in span.ents:
        if res := extract_entity(ent, doc._.replacements, doc._.json_logics):
            # If both parent and nested logic operator are "and", merge them
            if res.get("and"):
                predicates.extend(res["and"])
            else:
                predicates.append(res)

    if len(predicates) == 1:
        json_logic = predicates[0]
    else:
        json_logic = {"and": predicates}

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


ands_minor_patterns = get_dynamic_patterns(
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
    [
        {"TEXT": {"IN": ["and", ","]}},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
    range(0, 20),
    [
        {"TEXT": ",", "OP": "?"},
        {"TEXT": {"IN": ["and", ","]}},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": [","]}, "OP": "?"},
    ],
)
