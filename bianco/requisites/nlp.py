import spacy
from spacy.pipeline import EntityRuler

from requisites.pipes.merge_course_number import *
from requisites.pipes.detect_entity import patterns as entity_patterns
from requisites.pipes.merge_entity_spans import *

nlp = spacy.load("en_core_web_sm", exclude=["ner"])
nlp.add_pipe("merge_course_number")

entity_ruler: EntityRuler = nlp.add_pipe(
    "entity_ruler", config={"overwrite_ents": True}
)
entity_ruler.add_patterns(entity_patterns)

nlp.add_pipe("merge_entity_spans")

print(nlp.pipe_names)
