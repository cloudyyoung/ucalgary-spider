from spacy.language import Language
from spacy.pipeline import EntityRuler

patterns = [
    {
        "label": "COURSE",
        "pattern": [{"TEXT": {"REGEX": r"([A-Z]{3,4})"}}, {"POS": "NUM"}],
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
        "entity_ruler", config={"overwrite_ents": True}
    )
    entity_ruler.add_patterns(patterns)

    def detect_entity(doc):
        ents = entity_ruler.match(doc)
        doc.ents = ents
        return doc

    return detect_entity
