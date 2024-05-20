from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

from bianco.requisites.utils import replacement_letters, copy_span
from bianco.requisites.pipes.constitute_requisite import sort_matches
from bianco.requisites.pipes.patterns.ands_major import ands_major, ands_major_patterns
from bianco.requisites.pipes.patterns.ors_major import ors_minor, ors_major_patterns


@Language.factory("constitute_structure_major")
def constitute_structure_major(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add(1, ors_major_patterns, greedy="LONGEST", on_match=ors_minor)
    matcher.add(2, ands_major_patterns, greedy="LONGEST", on_match=ands_major)

    def constitute(doc: Doc):
        while matches := matcher(doc):
            # sort matches by length of span
            matches = sort_matches(matches)
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
