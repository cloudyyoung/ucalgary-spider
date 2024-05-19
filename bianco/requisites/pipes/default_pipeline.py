from spacy.language import Language
from spacy.pipeline import EntityRuler


@Language.factory("default_pipeline")
def default_pipeline(nlp: Language, name: str):
    tok2vec = nlp.get_pipe("tok2vec")
    tagger = nlp.get_pipe("tagger")
    parser = nlp.get_pipe("parser")
    attribute_ruler = nlp.get_pipe("attribute_ruler")
    lemmatizer = nlp.get_pipe("lemmatizer")

    def run_pipeline(doc):
        doc = tok2vec(doc)
        doc = tagger(doc)
        doc = parser(doc)
        doc = attribute_ruler(doc)
        doc = lemmatizer(doc)
        return doc

    return run_pipeline
