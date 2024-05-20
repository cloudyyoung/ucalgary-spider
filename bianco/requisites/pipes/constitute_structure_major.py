from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    get_dynamic_patterns,
    replacement_letters,
    copy_span,
)
from bianco.requisites.pipes.constitute_requisite import sort_matches_by_length
from bianco.requisites.pipes.constitute_structure_minor import (
    and_list,
    or_list,
    match_key,
)


### A; and B; and C; ... and D
major_and_list_patterns_1 = get_dynamic_patterns(
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
major_and_list_patterns_2 = get_dynamic_patterns(
    [{"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}}],
    [
        {"TEXT": {"IN": [",", ";"]}, "OP": "?"},
        {"ENT_TYPE": {"IN": ["COURSE", "REQUISITE"]}},
    ],
    range(1, 20),
    [],
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
### A; or B; or C; ... or D


@Language.factory("constitute_structure_major")
def constitute_structure_major(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(
        "A; and B; and C; ... and D",
        major_and_list_patterns_1 + major_and_list_patterns_2,
        greedy="LONGEST",
        on_match=and_list,
    )
    matcher.add(
        "A; or B; or C; ... or D",
        major_or_list_patterns,
        greedy="LONGEST",
        on_match=or_list,
    )

    def constitute(doc: Doc):
        while matches := matcher(doc):
            # sort matches by length of span
            matches = sort_matches_by_length(matches, match_key)
            match_id, start, end = matches[0]

            letter = next(replacement_letters)
            replacement = f"RQ {letter}"
            span = doc[start:end]

            span_copy = copy_span(span)
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
