from bianco.requisites.nlp import nlp
from bianco.requisites.utils import extract_doc, replace_subject_code, clean_text


def try_nlp(course: dict, sent: str):
    sent = replace_subject_code(sent)
    sent = clean_text(sent)
    doc = nlp(sent)
    json_logic = extract_doc(doc)
    return doc, json_logic
