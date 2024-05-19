import spacy

from pipes.constitute_requisite import *
from pipes.detect_entity import *
from pipes.merge_entity_spans import *

constituency_nlp = spacy.load("en_core_web_sm", exclude=["ner"])

for t in range(1, 2):
    constituency_nlp.add_pipe("constitute_requisite", f"constitute_requisite_{t}")
    constituency_nlp.add_pipe("detect_entity", f"detect_entity_{t}")
    constituency_nlp.add_pipe("merge_entity_spans", f"merge_entity_spans_{t}")
