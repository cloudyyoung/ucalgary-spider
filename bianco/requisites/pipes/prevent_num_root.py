from spacy.tokens import Doc
from spacy.language import Language


@Language.component("prevent_num_root")
def prevent_num_root(doc: Doc):
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "NUM":
            # Find a new root, preferring verbs
            new_root = None
            for possible_root in token.children:
                if possible_root.pos_ == "VERB":
                    new_root = possible_root
                    break
            # If no verb found, fall back to the first child
            if new_root is None and token.children:
                new_root = list(token.children)[0]

            if new_root:
                for child in list(token.children):
                    child.head = new_root
                new_root.head = token.head
                new_root.dep_ = token.dep_
                token.dep_ = "nummod"
                token.head = new_root

    return doc
