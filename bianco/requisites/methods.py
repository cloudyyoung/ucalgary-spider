from requisites.expand_nlp import expand_nlp
from requisites.constituency_nlp import constituency_nlp
from requisites.structure_nlp import structure_nlp
from requisites.utils import extract_doc, replace_subject_code


def try_nlp(course: dict, sent: str):
    sent = replace_subject_code(sent)
    doc = expand_nlp(sent)
    doc = constituency_nlp(doc)
    doc = structure_nlp(doc)
    j = extract_doc(doc)
    return j
