from spacy.language import Language
from spacy.tokens import Doc


@Language.component("merge_entity_spans")
def merge_entity_spans(doc: Doc):
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            if ent.label_ is not None:
                retokenizer.merge(
                    ent,
                    attrs={
                        "ENT_TYPE": ent.label_,
                        "ENT_IOB": "B",
                        "ENT_IOE": "E",
                        "ENT_IOR": "",
                        "POS": "PROPN",
                        "TAG": ent.label_,
                        "LEMMA": (
                            ent.text.replace(" ", "")
                            if ent.label_ == "COURSE"
                            else ent.lemma_
                        ),
                    },
                )
    return doc
