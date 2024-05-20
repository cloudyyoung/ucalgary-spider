from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import is_top_match, copy_span, subject_codes


def courses_labelled(matcher: Matcher, doc: Doc, i: int, matches: list):
    if not is_top_match(i, matches):
        return

    match_id, start, end = matches[i]
    span = doc[start:end]

    subject_code = span[2]

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, {"course": subject_code.text}))


courses_labelled_patterns = [
    [
        {"LEMMA": "course"},
        {"LEMMA": "label"},
        {"TEXT": {"IN": subject_codes}},
    ]
]
