patterns = [
    {
        "label": "COURSE",
        "pattern": [{"TEXT": {"REGEX": r"([A-Z]{3,4})"}}, {"POS": "NUM"}],
    },
    {
        "label": "REQUISITE",
        "pattern": [
            {"TEXT": "RQ"},
            {"TEXT": {"REGEX": "[A-Z]"}},
        ],
    },
]
