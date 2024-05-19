from spacy.tokens import Doc

from pipes import *

Doc.set_extension("replacements", default=[], force=True)
Doc.set_extension("json_logics", default=[], force=True)
