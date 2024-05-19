from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import Matcher

eng = Language(True)

course_number_matcher = Matcher(eng.vocab)
course_number_matcher.add(
    "COURSE_NUMBER",
    [
        [
            {"IS_DIGIT": True, "LENGTH": {">=": 2, "<=": 3}},
            {"TEXT": {"IN": ["-", "."]}},
            {"IS_DIGIT": True, "LENGTH": {">=": 1, "<=": 2}},
        ],
    ],
)


@Language.component("merge_course_number")
def merge_course_number(doc: Doc):
    with doc.retokenize() as retokenizer:
        for match_id, start, end in course_number_matcher(doc):
            retokenizer.merge(
                doc[start:end],
                attrs={"POS": "NUM", "TAG": "COURSE_NUMBER"},
            )
    return doc
