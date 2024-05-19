from spacy.language import Language
from spacy.pipeline import EntityRuler

from requisites.utils import subject_codes

patterns = [
    {
        "label": "COURSE",
        "pattern": [{"TEXT": {"IN": subject_codes}}, {"POS": "NUM"}],
    },
    {
        "label": "REQUISITE",
        "pattern": [
            {"TEXT": "RQ"},
            {"TEXT": {"REGEX": "[A-Z]"}},
        ],
    },
]


@Language.factory("detect_entity")
def create_detect_entity(nlp: Language, name: str):
    entity_ruler: EntityRuler = nlp.add_pipe(
        "entity_ruler", name, config={"overwrite_ents": True}
    )
    entity_ruler.add_patterns(patterns)

    def detect_entity(doc):
        ents = entity_ruler.match(doc)
        doc.ents = ents
        return doc

    return detect_entity
