from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher
import re

from ..nlp import nlp
from ..utils import (
    get_dynamic_patterns,
    find_replacement,
    find_json_logic,
    replacement_letters,
)

structure_minor_matcher = Matcher(nlp.vocab)


### A, B, C, ..., and D
def and_list(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    predicates = []

    for ent in span.ents:
        if ent.label_ == "COURSE":
            predicates.append({"course": ent.text})

        elif ent.label_ == "REQUISITE":
            requisite_span = find_replacement(ent.text, doc._.replacements)
            requisite_logic = find_json_logic(requisite_span, doc._.json_logics)
            if requisite_logic:
                predicates.append(requisite_logic)

    if len(predicates) == 1:
        json_logic = predicates[0]
    else:
        json_logic = {"and": predicates}

    doc._.json_logics.append((span, json_logic))


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

structure_minor_matcher.add(
    "A, B, C, ..., and D", and_list_patterns, greedy="LONGEST", on_match=and_list
)
### A, B, C, ..., and D


### A, B, C, ..., or D
def or_list(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    predicates = []

    for ent in span.ents:
        if ent.label_ == "COURSE":
            predicates.append({"course": ent.text})

        elif ent.label_ == "REQUISITE":
            requisite_span = find_replacement(ent.text, doc._.replacements)
            requisite_logic = find_json_logic(requisite_span, doc._.json_logics)
            if requisite_logic:
                predicates.append(requisite_logic)

    if len(predicates) == 1:
        json_logic = predicates[0]
    else:
        json_logic = {"or": predicates}

    doc._.json_logics.append((span, json_logic))


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

structure_minor_matcher.add(
    "A, B, C, ..., or D", or_list_patterns, greedy="LONGEST", on_match=or_list
)
### A, B, C, ..., or D


@Language.component("constitute_structure_minor")
def constitute_structure(doc: Doc):
    sent = doc.text
    matches = structure_minor_matcher(doc)
    replacements = []

    # sort matches by length of span
    matches = sorted(matches, key=lambda x: x[2] - x[1], reverse=True)

    for match_id, start, end in matches:
        letter = next(replacement_letters)
        replacement = f"RQ {letter}"
        span = doc[start:end]
        new_sent = re.sub(re.escape(span.text), replacement, sent)

        if new_sent != sent:
            sent = new_sent
            replacements.append((replacement, span))

    new_doc = nlp(sent)
    new_doc._.replacements = doc._.replacements + replacements
    new_doc._.json_logics = doc._.json_logics
    return new_doc
