import spacy
from spacy.pipeline import EntityRuler

from requisites.pipes.merge_course_number import *
from requisites.pipes.detect_entity import *
from requisites.pipes.merge_entity_spans import *

nlp = spacy.load("en_core_web_sm", exclude=["ner"])
nlp.add_pipe("merge_course_number")
nlp.add_pipe("detect_entity")
nlp.add_pipe("merge_entity_spans")

print(nlp.pipe_names)
