from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import (
    replacement_letters,
    copy_span,
    sort_matches_by_length,
)
from bianco.requisites.pipes.patterns.x_units_of_courses import (
    x_units_of_patterns,
    x_units_of,
)
from bianco.requisites.pipes.patterns.x_units import x_units_patterns, x_units
from bianco.requisites.pipes.patterns.x_of_courses import x_of_patterns, x_of
from bianco.requisites.pipes.patterns.consent_of import consent_of_patterns, consent_of
from bianco.requisites.pipes.patterns.admission_of import (
    admission_of_patterns,
    admission_of,
)
from bianco.requisites.pipes.patterns.both_a_and_b import (
    both_a_and_b,
    both_a_and_b_patterns,
)
from bianco.requisites.pipes.patterns.either_a_or_b import (
    either_a_or_b,
    either_a_or_b_patterns,
)


@Language.factory("constitute_requisite")
def constitute_requisite(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(1, x_units_of_patterns, greedy="LONGEST", on_match=x_units_of)
    matcher.add(2, x_units_patterns, greedy="LONGEST", on_match=x_units)
    matcher.add(3, x_of_patterns, greedy="LONGEST", on_match=x_of)
    matcher.add(4, admission_of_patterns, greedy="LONGEST", on_match=admission_of)
    matcher.add(5, consent_of_patterns, greedy="LONGEST", on_match=consent_of)
    matcher.add(6, both_a_and_b_patterns, greedy="LONGEST", on_match=both_a_and_b)
    matcher.add(7, either_a_or_b_patterns, greedy="LONGEST", on_match=either_a_or_b)

    def constitute(doc: Doc):
        while matches := matcher(doc):
            # sort matches by length of span
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
