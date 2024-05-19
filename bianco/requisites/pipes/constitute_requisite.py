from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher
import re

from requisites.utils import get_dynamic_patterns, replacement_letters


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


consent_of_patterns = get_dynamic_patterns(
    [
        {"LEMMA": "consent"},
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
### Consent of


### Both A and B
def both_a_and_b(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"and": [{"course": a.text}, {"course": b.text}]}
    doc._.json_logics.append((span, json_logic))


### Both A and B


### Either A or B
def either_a_or_b(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"or": [{"course": a.text}, {"course": b.text}]}
    doc._.json_logics.append((span, json_logic))


### Either A or B


@Language.factory("constitute_requisite")
def constitute_requisite(nlp: Language, name: str):
    requisite_pattern_matcher = Matcher(nlp.vocab)
    requisite_pattern_matcher.add(
        "X units of",
        x_units_of_patterns,
        greedy="LONGEST",
        on_match=x_units_of,
    )
    requisite_pattern_matcher.add(
        "x_units",
        [[{"IS_DIGIT": True}, {"LEMMA": "unit"}]],
        greedy="LONGEST",
        on_match=x_units,
    )
    requisite_pattern_matcher.add(
        "X of",
        x_of_patterns,
        greedy="LONGEST",
        on_match=x_of,
    )
    requisite_pattern_matcher.add(
        "Admission to",
        admission_of_patterns,
        greedy="LONGEST",
        on_match=admission_of,
    )
    requisite_pattern_matcher.add(
        "Consent of",
        consent_of_patterns,
        greedy="LONGEST",
        on_match=consent_of,
    )
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

    def constitute(doc: Doc):
        sent = doc.text

        while matches := requisite_pattern_matcher(doc):
            # sort matches by length of span
            matches = sorted(matches, key=lambda x: x[2] - x[1], reverse=True)
            match_id, start, end = matches[0]

            letter = next(replacement_letters)
            replacement = f"RQ {letter}"
            span = doc[start:end]
            new_sent = re.sub(re.escape(span.text), replacement, sent)

            if new_sent != sent:
                sent = new_sent
                doc._.replacements.append((replacement, span))

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
