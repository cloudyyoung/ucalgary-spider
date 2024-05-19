from spacy.language import Language
from spacy.tokens import Doc

from requisites.utils import subject_codes
from requisites.nlp import nlp


@Language.component("expand_course_code")
def expand_course_code(doc: Doc):
    sent = ""

    for token in doc:
        if token.text in subject_codes:
            continue

        elif token.pos_ == "NUM" and token.tag_ == "COURSE_NUMBER":
            left_tokens = [token.head] + list(reversed(list(doc[: token.i])))

            for left_token in left_tokens:
                if left_token.text in subject_codes:
                    sent += left_token.text_with_ws
                    break

            sent += token.text_with_ws

        else:
            sent += token.text_with_ws

    new_doc = nlp(sent)
    new_doc.ents = []
    return new_doc
