from bianco.requisites.methods import try_nlp

sent = "Software Engineering for Engineers 300; and 3 units from Engineering 319, Digital Engineering 319 or Electrical Engineering 419; and 3 units from Software Engineering for Engineers 337, Computer Engineering 335, 339, or Geomatics Engineering 333."
sent = "Biology 30 or 212; Chemistry 30 or 212; and Mathematics 30-1 or 212."

j = try_nlp({}, sent)
print(j)
