from spacy.language import Language
from spacy.tokens import Doc, Token
from spacy.matcher import Matcher
import re

from requisites.utils import get_dynamic_patterns, replacement_letters


def sort_matches_by_length(matches: list[tuple[int, int, int]]):
    return sorted(matches, key=lambda x: x[2] - x[1], reverse=True)


def is_longest_match(i: int, matches: list[tuple[int, int, int]]):
    match_id, _, _ = matches[i]
    sorted_matches = sort_matches_by_length(matches)
    longest_match_id, _, _ = sorted_matches[0]
    return match_id == longest_match_id


### X Units of
def x_units_of(matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]):
    if not is_longest_match(i, matches):
        return

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

    doc._.json_logics.append((span.text, json_logic))


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


def x_units(matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]

    units_required = int(span[0].text)

    json_logic = {
        "units": {
            "required": units_required,
        }
    }

    doc._.json_logics.append((span.text, json_logic))


### X of
def x_of(matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches):
        return

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

    doc._.json_logics.append((span.text, json_logic))


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
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    consent_of = span[2:].text.strip()
    if consent_of.endswith("."):
        consent_of = consent_of[:-1]
    json_logic = {"consent": consent_of}
    doc._.json_logics.append((span.text, json_logic))


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
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    admission_of = span[2:].text.strip()
    if admission_of.endswith("."):
        admission_of = admission_of[:-1]
    json_logic = {"admission": admission_of}
    doc._.json_logics.append((span.text, json_logic))


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
def both_a_and_b(
    matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]
):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"and": [{"course": a.text}, {"course": b.text}]}
    doc._.json_logics.append((span.text, json_logic))


### Both A and B


### Either A or B
def either_a_or_b(
    matcher: Matcher, doc: Doc, i: int, matches: list[tuple[int, int, int]]
):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    a = span[1]
    b = span[3]
    json_logic = {"or": [{"course": a.text}, {"course": b.text}]}
    doc._.json_logics.append((span.text, json_logic))


### Either A or B


@Language.factory("constitute_requisite")
def constitute_requisite(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(
        "X units of",
        x_units_of_patterns,
        greedy="LONGEST",
        on_match=x_units_of,
    )
    matcher.add(
        "x_units",
        [[{"IS_DIGIT": True}, {"LEMMA": "unit"}]],
        greedy="LONGEST",
        on_match=x_units,
    )
    matcher.add(
        "X of",
        x_of_patterns,
        greedy="LONGEST",
        on_match=x_of,
    )
    matcher.add(
        "Admission to",
        admission_of_patterns,
        greedy="LONGEST",
        on_match=admission_of,
    )
    matcher.add(
        "Consent of",
        consent_of_patterns,
        greedy="LONGEST",
        on_match=consent_of,
    )
    matcher.add(
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
    matcher.add(
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
        while matches := matcher(doc):
            # sort matches by length of span
            matches = sort_matches_by_length(matches)
            match_id, start, end = matches[0]

            letter = next(replacement_letters)
            replacement = f"RQ {letter}"
            span = doc[start:end]

            doc_copy = Doc(nlp.vocab).from_json(doc.to_json())
            span_copy = doc_copy[span.start : span.end]
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
