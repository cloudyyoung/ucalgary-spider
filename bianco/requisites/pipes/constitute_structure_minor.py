from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    replacement_letters,
    copy_span,
    extract_entity,
)
from bianco.requisites.pipes.constitute_requisite import (
    sort_matches_by_length,
    is_longest_match,
)


match_key = lambda x: (x[2] - x[1] + (1000 if x[0] == 999 else 0))


### A, B, C, ..., and D
def and_list(matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches, match_key):
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


and_list_patterns = get_dynamic_patterns(
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
### A, B, C, ..., and D


### A, B, C, ..., or D
def or_list(matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches, match_key):
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


or_list_patterns = get_dynamic_patterns(
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
### A, B, C, ..., or D


### A and B or C
def a_and_b_or_c(matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches, match_key):
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
### A and B or C


@Language.factory("constitute_structure_minor")
def constitute_structure_minor(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(
        "A, B, C, ..., and D", and_list_patterns, greedy="LONGEST", on_match=and_list
    )
    matcher.add(
        "A, B, C, ..., or D", or_list_patterns, greedy="LONGEST", on_match=or_list
    )
    matcher.add(999, a_and_b_or_c_patterns, greedy="LONGEST", on_match=a_and_b_or_c)

    def constitute(doc: Doc):
        while matches := matcher(doc):
            # sort matches by length of span, prioritize "or" over "and"
            matches = sort_matches_by_length(matches, match_key)
            match_id, start, end = matches[0]

            letter = next(replacement_letters)
            replacement = f"RQ {letter}"
            span = doc[start:end]

            span_copy = copy_span(span)
            doc._.replacements.append((replacement, span_copy))

            with doc.retokenize() as retokenizer:
                retokenizer.merge(
                    span,
                    attrs={
                        "LEMMA": replacement,
                        "ENT_TYPE": "REQUISITE",
                        "POS": "PROPN",
                        "TAG": "REQUISITE",
                    },
                )

        return doc

    return constitute
