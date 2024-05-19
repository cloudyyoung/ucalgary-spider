from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher
import re

from ..nlp import nlp
from ..utils import get_dynamic_patterns, replacement_letters
from .constitute_structure_minor import and_list, or_list

structure_major_matcher = Matcher(nlp.vocab)

### A; and B; and C; ... and D
major_and_list_patterns = get_dynamic_patterns(
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
structure_major_matcher.add(
    "A; and B; and C; ... and D",
    major_and_list_patterns,
    greedy="LONGEST",
    on_match=and_list,
)
### A; and B; and C; ... and D


### A; or B; or C; ... or D
major_or_list_patterns = get_dynamic_patterns(
    [],
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
        {"TEXT": {"IN": ["or", ";"]}, "OP": "+"},
    ],
    range(1, 20),
    [
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
)
structure_major_matcher.add(
    "A; or B; or C; ... or D",
    major_or_list_patterns,
    greedy="LONGEST",
    on_match=or_list,
)
### A; or B; or C; ... or D


@Language.component("constitute_structure_major")
def constitute_structure(doc: Doc):
    sent = doc.text
    matches = structure_major_matcher(doc)
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
