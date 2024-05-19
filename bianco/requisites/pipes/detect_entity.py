from spacy.language import Language
from spacy.tokens import Doc
from spacy.pipeline import EntityRuler

from requisites.nlp import nlp

subject_code_regex = r"([A-Z]{3,4})"

entity_ruler = EntityRuler(nlp)
patterns = [
    {
        "label": "COURSE",
        "pattern": [{"TEXT": {"REGEX": subject_code_regex}}, {"POS": "NUM"}],
    },
    {
        "label": "REQUISITE",
        "pattern": [
            {"TEXT": "RQ"},
            {"TEXT": {"REGEX": "[A-Z]"}},
        ],
    },
]
entity_ruler.clear()
entity_ruler.add_patterns(patterns)


@Language.component("detect_entity")
def detect_entity(doc: Doc):
    ents = entity_ruler.match(doc)
    doc.ents = ents
    return doc
