from bianco.requisites.nlp import nlp
from bianco.requisites.utils import extract_doc, replace_subject_code, clean_text


def try_nlp(course: dict, sent: str, mode="prereq"):
    sent = replace_subject_code(sent)
    sent = clean_text(sent)

    if mode == "prereq":
        doc = nlp(sent)
        json_logic = extract_doc(doc)

    elif mode == "antireq":
        is_convertable = False

        if sent.startswith("Credit for "):
            sent = sent.replace("Credit for ", "")
            sent = sent.replace(" will not be allowed", "")
            sent = sent.replace("any of", "one of")
            is_convertable = True

        doc = nlp(sent)
        json_logic = extract_doc(doc)

        if is_convertable:
            json_logic = convert_logic(json_logic)

    return doc, json_logic


def convert_logic(json_logic):
    new_json_logic = {}
    if json_logic["and"]:
        new_json_logic["or"] = convert_logic(json_logic["and"])
    else:
        new_json_logic["and"] = convert_logic(json_logic["or"])
    return new_json_logic
