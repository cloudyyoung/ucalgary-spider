import spacy

constituency_nlp = spacy.load("en_core_web_sm", exclude=["ner"])
