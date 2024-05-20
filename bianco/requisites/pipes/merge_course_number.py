from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

patterns = [
    [
        {"IS_DIGIT": True, "LENGTH": {">=": 2, "<=": 3}},
        {"TEXT": "-"},
        {"IS_DIGIT": True, "LENGTH": {">=": 1, "<=": 2}},
    ]
]


@Language.factory("merge_complex_course_number")
def create_complex_merge_course_number(nlp: Language, name: str):
    matcher = Matcher(nlp.vocab)
    matcher.add("COURSE_NUMBER", patterns, greedy="LONGEST")

    def merge_course_number(doc: Doc):
        with doc.retokenize() as retokenizer:
            for match_id, start, end in matcher(doc):
                retokenizer.merge(
                    doc[start:end],
                    attrs={"POS": "NUM", "TAG": "COURSE_NUMBER"},
                )
        return doc

    return merge_course_number
