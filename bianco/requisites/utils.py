import itertools
from spacy.tokens import Span, Doc, Token
from pymongo import MongoClient
import re

course_number_regex = r"(\d{2}-\d|\d{3}\.\d{1,2}|\d{2,3})"  # 101, 30-1, 599.45


def get_replacement_letter():
    # Create an iterator that cycles through the alphabet
    for letter in itertools.cycle("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        yield letter


replacement_letters = get_replacement_letter()


# Connect to mongodb
client = MongoClient("mongodb://root:password@localhost:27017/")
catalog = client.get_database("catalog")

# Sort by length of title
subject_codes_docs = list(catalog.get_collection("subject_codes").find())
subject_codes_docs.sort(key=lambda x: len(x["title"]), reverse=True)
subject_codes_map = {doc["title"]: doc["code"] for doc in subject_codes_docs}
subject_codes = [doc["code"] for doc in subject_codes_docs]


def replace_subject_code(sentence: str, loose: bool=False):
	for subject_code in subject_codes_docs:
		if loose:
			sentence = re.sub(rf"{subject_code["title"]}", rf"{subject_code["code"]}", sentence)
		else:
			sentence = re.sub(rf"{subject_code["title"]} {course_number_regex}", rf"{subject_code["code"]} \1", sentence)
	return sentence

def get_repeating_array(
    head: list, repeat_elemnts: list, repeat_times: int, tail: list
):
    repeated_part = repeat_elemnts * repeat_times
    return head + repeated_part + tail


def get_dynamic_patterns(
    head: list, repeat_tokens: list, repeat_range: range, tail: list
):
    patterns = []
    for i in repeat_range:
        patterns.append(get_repeating_array(head, repeat_tokens, i, tail))
    return patterns


def find_replacement(key: str, replacements: list[tuple[str, Span]]):
    if not replacements or not key:
        return

    key = key[:-1].strip() if key.strip().endswith(".") else key

    for _key, span in replacements:
        if key == _key:
            return span


def find_json_logic(span: Span, json_logic: list[tuple[Span, dict]]):
    if not json_logic or not span:
        return

    for _span, logic in json_logic:
        if span.text == _span.text:
            return logic


def sanity_check(span: Span):
    if len(span) == 0:
        return False

    token = span[0]
    is_ent_type = token.ent_type_ in ["COURSE", "REQUISITE"]

    if len(span) == 1 and is_ent_type:
        return True

    if len(span) == 2 and is_ent_type:
        return True

    return False


def extract_entity(
    token: Token | Span, replacements: dict[str, Span], json_logics: list[tuple[Span, dict]]
):
    if (isinstance(token, Token) and token.ent_type_ == "COURSE") or (isinstance(token, Span) and token.label_ == "COURSE"):
        return {"course": token.text}

    elif (isinstance(token, Token) and token.ent_type_ == "REQUISITE") or (isinstance(token, Span) and token.label_ == "REQUISITE"):
        replacement = find_replacement(token.lemma_, replacements)
        json_logic = find_json_logic(replacement, json_logics)
        return json_logic


def extract_doc(doc: Doc):
    if not sanity_check(doc):
        print("A - Sanity check failed")
        return None

    token = doc[0]
    return extract_entity(token, doc._.replacements, doc._.json_logics)


def add_token_at_index(doc, token_text, index, space_after=True):
    # Create a list of words and spaces from the original doc
    words = [token.text for token in doc]
    spaces = [token.whitespace_ for token in doc]

    # Insert the new token at the specified index
    words.insert(index, token_text)
    spaces.insert(index, " " if space_after else "")

    # Create a new Doc object with the modified words and spaces
    new_doc = Doc(doc.vocab, words=words, spaces=spaces)

    # Transfer annotations from the original doc to the new doc
    new_doc.ents = [
        Span(new_doc, ent.start, ent.end, label=ent.label_) for ent in doc.ents
    ]
    for token, new_token in zip(doc, new_doc):
        new_token.tag_ = token.tag_
        new_token.pos_ = token.pos_
        new_token.dep_ = token.dep_
        new_token.head = new_doc[token.head.i]

    return new_doc


def copy_doc(doc: Doc):
    new_doc = Doc(doc.vocab).from_json(doc.to_json())
    return new_doc

def copy_span(span: Span):
    doc_copy = copy_doc(span.doc)
    new_span = Span(doc_copy, span.start, span.end)
    return new_span
