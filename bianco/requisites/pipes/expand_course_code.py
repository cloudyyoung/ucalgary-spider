from spacy.language import Language
from spacy.tokens import Doc
import re

from requisites.utils import subject_codes, course_number_regex


@Language.component("expand_course_code")
def expand_course_code(doc: Doc):
    tokens = []

    def add_token(token):
        tokens.append(token)

    for token in doc:
        if token.text in subject_codes:
            continue

        elif token.pos_ == "NUM" and re.match(course_number_regex, token.text):
            left_tokens = [token.head] + list(reversed(list(doc[: token.i])))

            for left_token in left_tokens:
                if left_token.text in subject_codes:
                    add_token(left_token)
                    break

            add_token(token)

        else:
            add_token(token)

    words = [token.text for token in tokens]
    spaces = [token.whitespace_ for token in tokens]

    new_doc = Doc(doc.vocab, words=words, spaces=spaces)

    for token, new_token in zip(tokens, new_doc):
        new_token.tag_ = token.tag_
        new_token.pos_ = token.pos_
        new_token.dep_ = token.dep_
        new_token.lemma_ = token.lemma_
        new_token.ent_type_ = token.ent_type_
        new_token.ent_id = token.ent_id
        new_token.norm_ = token.norm_

    return new_doc