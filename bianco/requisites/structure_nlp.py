import spacy

from requisites.pipes.constitute_structure_minor import *
from requisites.pipes.constitute_structure_major import *
from requisites.pipes.detect_entity import *
from requisites.pipes.merge_entity_spans import *

structure_nlp = spacy.load("en_core_web_sm", exclude=["ner"])

for t in range(1, 5):
    structure_nlp.add_pipe(
        "constitute_structure_minor", f"constitute_structure_minor_{t}"
    )
    structure_nlp.add_pipe("detect_entity", f"detect_entity_{t}")
    structure_nlp.add_pipe("merge_entity_spans", f"merge_entity_spans_{t}")

for t in range(6, 10):
    structure_nlp.add_pipe(
        "constitute_structure_major", f"constitute_structure_major_{t}"
    )
    structure_nlp.add_pipe("detect_entity", f"detect_entity_{t}")
    structure_nlp.add_pipe("merge_entity_spans", f"merge_entity_spans_{t}")
