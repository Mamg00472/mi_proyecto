import re

email = input("Escribe tu email: ")
expresion_regular = r'^[^@]+@[^@]+\.[^@]+$'

if re.match(expresion_regular, email):
    print("Email validado correctamente")
else:
    print("Email no es correcto, corrigelo:", email)