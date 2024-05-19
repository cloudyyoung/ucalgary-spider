from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher
import re

from requisites.utils import get_dynamic_patterns, replacement_letters
from requisites.nlp import nlp

requisite_pattern_matcher = Matcher(nlp.vocab)


### X Units of
def x_units_of(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]

    units_required = int(span[0].text)
    courses = [ent for ent in span.ents if ent.label_ == "COURSE"]

    json_logic = {
        "units": {
            "required": units_required,
            "from": [{"course": course.text} for course in courses],
        }
    }

    doc._.json_logics.append((span, json_logic))


x_units_of_patterns = get_dynamic_patterns(
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

requisite_pattern_matcher.add(
    "X units of", x_units_of_patterns, greedy="LONGEST", on_match=x_units_of
)
### X Units of


def x_units(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]

    units_required = int(span[0].text)
    courses = [ent for ent in span.ents if ent.label_ == "COURSE"]

    json_logic = {
        "units": {
            "required": units_required,
        }
    }

    doc._.json_logics.append((span, json_logic))


requisite_pattern_matcher.add(
    "x_units",
    [[{"IS_DIGIT": True}, {"LEMMA": "unit"}]],
    greedy="LONGEST",
    on_match=x_units,
)


### X of
def x_of(matcher, doc: Doc, i, matches):
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
            "from": [{"course": course.text} for course in courses],
        },
    }

    doc._.json_logics.append((span, json_logic))


x_of_patterns = get_dynamic_patterns(
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

requisite_pattern_matcher.add("X of", x_of_patterns, greedy="LONGEST", on_match=x_of)
### One of


### Consent of
def consent_of(matcher, doc: Doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    consent_of = span[2:].text.strip()
    if consent_of.endswith("."):
        consent_of = consent_of[:-1]
    json_logic = {"consent": consent_of}
    doc._.json_logics.append((span, json_logic))


requisite_pattern_matcher.add(
    "Consent of",
    [
        [
            {"LEMMA": "consent"},
            {"POS": "ADP", "OP": "+"},
            {"TEXT": {"REGEX": "[A-Za-z, ]"}, "OP": "*"},
            {"IS_SENT_START": False},
        ]
    ],
    greedy="LONGEST",
    on_match=consent_of,
)


def admission_of(matcher, doc: Doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    admission_of = span[2:].text.strip()
    if admission_of.endswith("."):
        admission_of = admission_of[:-1]
    json_logic = {"admission": admission_of}
    doc._.json_logics.append((span, json_logic))


admission_of_patterns = get_dynamic_patterns(
    [
        {"LEMMA": "admission"},
        {"POS": "ADP", "OP": "+"},
    ],
    [
        {"ENT_TYPE": {"NOT_IN": ["COURSE"]}},
    ],
    range(1, 200),
    [
        {
            "LEMMA": {"NOT_IN": ["and", "or", ",", ";"]},
            "ENT_TYPE": {"NOT_IN": ["COURSE", "REQUISITE"]},
        },
    ],
)

requisite_pattern_matcher.add(
    "Admission to",
    admission_of_patterns,
    greedy="LONGEST",
    on_match=admission_of,
)
### Consent of


### Both A and B
def both_a_and_b(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"and": [{"course": a.text}, {"course": b.text}]}
    doc._.json_logics.append((span, json_logic))


requisite_pattern_matcher.add(
    "Both A and B",
    [
        [
            {"LEMMA": "both"},
            {"ENT_TYPE": "COURSE"},
            {"LEMMA": "and"},
            {"ENT_TYPE": "COURSE"},
        ]
    ],
    greedy="LONGEST",
    on_match=both_a_and_b,
)
### Both A and B


### Either A or B
def either_a_or_b(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"or": [{"course": a.text}, {"course": b.text}]}
    doc._.json_logics.append((span, json_logic))


requisite_pattern_matcher.add(
    "Either A or B",
    [
        [
            {"LEMMA": "either"},
            {"ENT_TYPE": "COURSE"},
            {"LEMMA": "or"},
            {"ENT_TYPE": "COURSE"},
        ]
    ],
    greedy="LONGEST",
    on_match=either_a_or_b,
)
### Either A or B


@Language.component("constitute_requisite")
def constitute_requisite(doc: Doc):
    sent = doc.text
    matches = requisite_pattern_matcher(doc)
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
