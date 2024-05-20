from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import replacement_letters, copy_span
from bianco.requisites.utils import sort_matches_by_length
from bianco.requisites.pipes.patterns.ands_minor import ands_minor_patterns, ands_minor
from bianco.requisites.pipes.patterns.ors_minor import ors_minor_patterns, ors_minor
from bianco.requisites.pipes.patterns.a_and_b_or_c import (
    a_and_b_or_c_patterns,
    a_and_b_or_c,
)


@Language.factory("constitute_structure_minor")
def constitute_structure_minor(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(11, a_and_b_or_c_patterns, greedy="LONGEST", on_match=a_and_b_or_c)
    matcher.add(12, ands_minor_patterns, greedy="LONGEST", on_match=ands_minor)
    matcher.add(13, ors_minor_patterns, greedy="LONGEST", on_match=ors_minor)

    def constitute(doc: Doc):
        while matches := matcher(doc):
            matches = sort_matches_by_length(matches)
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
