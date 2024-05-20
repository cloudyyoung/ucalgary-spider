from spacy.language import Language
from spacy.tokens import Doc

from bianco.requisites.utils import subject_codes


@Language.component("fix_ent_head")
def fix_ent_head(doc: Doc):
    for sent in doc.sents:
        for token in sent:
            if token.pos_ == "NUM" and token.tag_ == "COURSE_NUMBER":
                ancestors = list(
                    filter(lambda x: x.text in subject_codes, token.ancestors)
                )
                ancestor = ancestors[0] if len(ancestors) > 0 else None

                if ancestor:
                    token.head = ancestor
    return doc
