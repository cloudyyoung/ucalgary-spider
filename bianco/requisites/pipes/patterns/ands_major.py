from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import get_dynamic_patterns
from bianco.requisites.pipes.patterns.ands_minor import ands_minor


def ands_major(matcher: Matcher, doc: Doc, i, matches):
    return ands_minor(matcher, doc, i, matches)


group_a = get_dynamic_patterns(
    [],
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": ["and", ";"]}, "OP": "+"},
    ],
    range(1, 20),
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
)

group_b = get_dynamic_patterns(
    [{"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}}],
    [
        {"TEXT": {"IN": [",", ";"]}, "OP": "?"},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
    range(1, 20),
    [],
)

ands_major_patterns = group_a + group_b
