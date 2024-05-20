from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    copy_span,
    is_longest_match,
)


def consent_of(matcher: Matcher, doc: Doc, i, matches):
    if not is_longest_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]
    consent_of = span[2:].text.strip()
    if consent_of.endswith("."):
        consent_of = consent_of[:-1]
    json_logic = {"consent": consent_of}

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


consent_of_patterns = get_dynamic_patterns(
    [
        {"LEMMA": "consent"},
        {"POS": "ADP", "OP": "+"},
    ],
    [
        {"ENT_TYPE": {"NOT_IN": ["COURSE", "REQUISITE"]}, "POS": {"NOT_IN": ["NUM"]}},
    ],
    range(1, 200),
    [
        {
            "LEMMA": {"NOT_IN": ["and", "or", ",", ";"]},
            "ENT_TYPE": {"NOT_IN": ["COURSE", "REQUISITE"]},
        },
    ],
)
