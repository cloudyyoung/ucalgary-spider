from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    copy_span,
    is_longest_match,
)


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

    span_copy = copy_span(span)
    doc._.json_logics.append((span_copy, json_logic))


x_units_patterns = [[{"IS_DIGIT": True}, {"LEMMA": "unit"}]]
