import re

from bianco.requisites.nlp import nlp
from bianco.requisites.utils import extract_doc, replace_subject_code, clean_text


def try_nlp(course: dict, sent: str, mode="prereq"):
    sent = replace_subject_code(sent)
    sent = clean_text(sent)

    if mode == "prereq":
        doc = nlp(sent)
        json_logic = extract_doc(doc)

    elif mode == "antireq":
        if sent.startswith("Credit for ") and sent.endswith(" will not be allowed."):
            sent = sent.replace("Credit for ", "")
            sent = sent.replace(" will not be allowed", "")
            sent = sent.replace("any of", "one of")
            sent = sent.replace("either of", "one of")
            sent = re.sub(r"either (.*) and (.*)", r"\1 or \2", sent)
            sent = re.sub(r"both (.*) or (.*)", r"\1 and \2", sent)
        elif sent.startswith("Not open to students with credit in "):
            sent = sent.replace("Not open to students with credit in ", "")
        elif sent.startswith("Not for credit with "):
            sent = sent.replace("Not for credit with ", "")

        doc = nlp(sent)
        json_logic = extract_doc(doc)

        if is_convertable(json_logic):
            json_logic = convert_logic(json_logic)

    return doc, json_logic


def is_convertable(json_logic):
    if not json_logic:
        return False

    if "and" in json_logic:
        predicates = json_logic["and"]

        for predicate in predicates:
            if "course" not in predicate:
                return False

        return True
    return False


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
