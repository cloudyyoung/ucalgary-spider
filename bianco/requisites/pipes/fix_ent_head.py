from spacy.language import Language
from spacy.tokens import Doc

from bianco.requisites.utils import subject_codes


def recursive_find_subject_code(ancestors):
    for ancestor in ancestors:
        if ancestor.text in subject_codes:
            return ancestor
        elif ancestor.pos_ == "NUM" or ancestor.tag_ == "COURSE_NUMBER":
            return recursive_find_subject_code(ancestor.ancestors)
        elif ancestor.pos_ not in ["NOUN", "PROPN"]:
            continue
        else:
            return None
    return None


@Language.component("fix_ent_head")
def fix_ent_head(doc: Doc):
    for sent in doc.sents:
        for token in sent:
            ancestor = recursive_find_subject_code(token.ancestors)
            if ancestor:
                token.head = ancestor
    return doc
