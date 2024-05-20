from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import get_dynamic_patterns
from bianco.requisites.pipes.patterns.ors_minor import ors_minor


def ors_major(matcher: Matcher, doc: Doc, i, matches):
    return ors_minor(matcher, doc, i, matches)


ors_major_patterns = major_or_list_patterns = get_dynamic_patterns(
    [],
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": ["or", ";"]}, "OP": "+"},
    ],
    range(1, 20),
    [
        {"LEMMA": "or"},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
)
