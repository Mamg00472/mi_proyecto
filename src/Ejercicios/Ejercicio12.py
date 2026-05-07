import random

dado1 = 0
dado2 = 0

print("Saca 2 seises en los dados para salir")

while dado1 + dado2 != 12:
    input("Pulsa enter para tirar los dados")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"""
Sacaste en el primer dado un {dado1}
Sacaste en el segundo dado un {dado2}""")
    