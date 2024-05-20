sents = [
    "Actuarial Science 327; Statistics 323; 3 units from Mathematics 311, 313, 367 or 375; and 3 units from Computer Science 217, 231, 235 or Data Science 211.",
    "CPSC 457 and 3 units from SENG 300, 301 or ENSF 480; and admission to the Schulich School of Engineering.",
    "SGMA 395 or ENTI 317 or 381.",
    "One of FILM 321 or 323 and one of FILM 331 or 333.",
    "FILM 331 or 333.",
    "ENCI 473; and ENGG 319 or ENDG 319.",
    "3 units from ENCI 481, ENEE 377 or 519.09.",
    "ENEL 341, BMEN 327 or ENGG 225.",
    "ENEL 471; and one of BMEN 319 or ENGG 319 or ENEL 419.",
    "3 units from ENGG 319, ENDG 319 or ENEL 419.",
    "FILM 201 and 3 units from 305 or 321.",
    "INDG 201 and 3 units from INDG 303 or 345.",
    "One of GEOG 211, 251, 253, UBST 253, GLGY 201, 209; and consent of the Department.",
    "STAT 205 or 213; and admission to the Kinesiology Honours program; and consent of the Faculty.",
    "MATH 209 and admission to the Energy Engineering program.",
    "Both MATH 349 and 353; or both MATH 283 and 381; or MATH 267.",
    "MATH 431 or PMAT 431; MATH 429 or PMAT 429 or MATH 327 or PMAT 427.",
    "MATH 445 or 447; 3 units of Mathematics in the Field of Mathematics at the 400 level or above.",
    "MATH 383; and 6 units of Mathematics in the Field of Mathematics at the 400 level or above.",
    "MRSC 451 and consent of the Department.",
    "Admission to the Haskayne School of Business and OBHR 317.",
    "PHYS 211 or 221 or 227.",
    "MATH 277 and PHYS 259 and admission to a program in Engineering.",
    "PHYS 341; and 3 units from CPSC 217, 231 or DATA 211.",
    "ACSC 327; and MATH 323 or STAT 323.",
    "ANTH 203.",
    "One of GEOG 211, 251, 253, UBST 253, GLGY 201, 209; and consent of the Department.",
    "One of CORE 209, 435, KNES 355, NURS 303, 305, PSYC 203, 205, SOWK 300, 302, 304, 306, 363 or consent of the instructor(s).",
    "History 300 and one of East Asian Studies 331, 333, History 209, 301, 315, 317, 405, 407.01, 407.02, 407.03, or consent of the Department.",
    "Kinesiology 203, 213, 323 and admission to the Faculty of Kinesiology.",
    "Mathematics 30-1, Mathematics 30-2, or Mathematics 31.",
    "Admission to the Psychology major or Honours program and Psychology 300, 301, 369.",
    "Computer Science 219, 233 or Data Science 311 and enrolment in one of the Majors in Computer Science, Bioinformatics, Electrical Engineering, Software Engineering, Computer Engineering, Natural Sciences with a primary concentration in Computer Science.",
    "Computer Science 219, 233 or Data Science 311 and enrolment in one of the Majors in Computer Science, Bioinformatics, Electrical Engineering, Software Engineering, Computer Engineering, Natural Sciences with a primary concentration in Computer Science.",
    "Admission to the Haskayne School of Business, and 54 units including Accounting 217.",
    "3 units from Engineering 204, Chemistry 201, 209 or 211; and Chemistry 203 or 213; and 3 units from Mathematics 249, 265, 275.",
    "Software Engineering for Engineers 300; and 3 units from Engineering 319, Digital Engineering 319 or Electrical Engineering 419; and 3 units from Software Engineering for Engineers 337, Computer Engineering 335, 339, or Geomatics Engineering 333.",
    "3 units from Computer Science 219, 233 or 235; and Computer Science 251 or Statistics 213; and Mathematics 271 or 273; and 3 units from Mathematics 249, 265 or 275; and Philosophy 279 or 377.",
    "Psychology 200, 201, and admission to the International Indigenous Studies major.",
    "Geology 201 and 202; and Mathematics 267 or 277; and Physics 211 or 221, and 223.",
    "Physics 481; and Mathematics 433, Physics 435 or Physics Engineering 435.",
    "Chemistry 333 or 433; and one of 353 or 355; or Chemistry 357 and 409.",
    "Software Engineering for Engineers 300; and 3 units from Engineering 319, Digital Engineering 319 or Electrical Engineering 419; and 3 units from Software Engineering for Engineers 337, Computer Engineering 335, 339, or Geomatics Engineering 333.",
    "Medical Science 301 or 401: and Statistics 321.",
    "Biology 30 or 212; Chemistry 30 or 212; and Mathematics 30-1 or 212.",
    "60 units.",
]


from bianco.requisites.methods import try_nlp


def test_1():
    sent = "Actuarial Science 327; Statistics 323; 3 units from Mathematics 311, 313, 367 or 375; and 3 units from Computer Science 217, 231, 235 or Data Science 211."
    doc, json_logic = try_nlp({}, sent)

    assert json_logic == {
        "and": [
            {"course": "ACSC327"},
            {"course": "STAT323"},
            {
                "units": {
                    "from": [
                        {"course": "MATH 311"},
                        {"course": "MATH 313"},
                        {"course": "MATH 367"},
                        {"course": "MATH 375"},
                    ],
                    "required": 3,
                }
            },
            {
                "units": {
                    "from": [
                        {"course": "CPSC 217"},
                        {"course": "CPSC 231"},
                        {"course": "CPSC 235"},
                        {"course": "DATA 211"},
                    ],
                    "required": 3,
                }
            },
        ]
    }
