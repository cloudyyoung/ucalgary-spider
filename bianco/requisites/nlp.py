import spacy

from requisites.pipes.merge_course_number import *
from requisites.pipes.fix_ent_head import *
from requisites.pipes.detect_entity import *
from requisites.pipes.merge_entity_spans import *

nlp = spacy.load("en_core_web_sm", exclude=["ner"])
nlp.add_pipe("merge_complex_course_number")
nlp.add_pipe("fix_ent_head")
# nlp.add_pipe("detect_entity")
# nlp.add_pipe("merge_entity_spans")

print(nlp.pipe_names)
