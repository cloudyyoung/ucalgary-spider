import spacy

from requisites.pipes.merge_course_number import *
from requisites.pipes.fix_ent_head import *
from requisites.pipes.expand_course_code import *
from requisites.pipes.merge_entity_spans import *

expand_nlp = spacy.load("en_core_web_sm", exclude=["ner"])
expand_nlp.add_pipe("fix_ent_head")
# expand_nlp.add_pipe("expand_course_code")
# expand_nlp.add_pipe("detect_entity")
# expand_nlp.add_pipe("merge_entity_spans")
