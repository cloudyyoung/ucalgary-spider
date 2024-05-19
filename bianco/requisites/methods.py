from requisites.nlp import nlp
from requisites.utils import extract_doc, replace_subject_code


def try_nlp(course: dict, sent: str):
    sent = replace_subject_code(sent)
    doc = nlp(sent)
    j = extract_doc(doc)
    return j
