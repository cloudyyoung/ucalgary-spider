from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

from requisites.utils import (
    get_dynamic_patterns,
    find_replacement,
    find_json_logic,
    replacement_letters,
    copy_doc,
    copy_span,
    extract_entity,
)
from requisites.pipes.constitute_requisite import (
    sort_matches_by_length,
    is_longest_match,
)


### A, B, C, ..., and D
def and_list(matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    predicates = []

    for ent in span.ents:
        if res := extract_entity(ent, doc._.replacements, doc._.json_logics):
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
        {"TEXT": {"IN": ["and", ","]}},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": [","]}, "OP": "?"},
    ],
)
### A, B, C, ..., and D


### A, B, C, ..., or D
def or_list(matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    predicates = []

    for ent in span.ents:
        if res := extract_entity(ent, doc._.replacements, doc._.json_logics):
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
        {"TEXT": {"IN": ["or"]}},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": [","]}, "OP": "?"},
    ],
)
### A, B, C, ..., or D


@Language.factory("constitute_structure_minor")
def constitute_structure_minor(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(
        "A, B, C, ..., and D", and_list_patterns, greedy="LONGEST", on_match=and_list
    )
    matcher.add(
        "A, B, C, ..., or D", or_list_patterns, greedy="LONGEST", on_match=or_list
    )

    def constitute(doc: Doc):
        while matches := matcher(doc):
            # sort matches by length of span
            matches = sort_matches_by_length(matches)
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
