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
            sent = sent.replace("either of", "one of")
            is_convertable = True

        doc = nlp(sent)
        json_logic = extract_doc(doc)

        if is_convertable and sent.count("and") == 1 and sent.count("or") == 0:
            json_logic = convert_logic(json_logic)

    return doc, json_logic


def convert_logic(json_logic):
    if not json_logic:
        return json_logic

    new_json_logic = {}
    if "and" in json_logic:
        new_json_logic["or"] = convert_logic(json_logic["and"])
    elif "or" in json_logic:
        new_json_logic["and"] = convert_logic(json_logic["or"])
    else:
        new_json_logic = json_logic
    return new_json_logic
