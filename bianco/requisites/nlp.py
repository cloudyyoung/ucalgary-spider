import spacy

from requisites.pipes.merge_course_number import *

nlp = spacy.load("en_core_web_sm", exclude=["ner"])
nlp.add_pipe("merge_course_number", before="detect_entity")
