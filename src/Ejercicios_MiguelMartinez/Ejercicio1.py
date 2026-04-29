numero = 0

while numero != -1:
    numero = int (input("""
=============================
Escribe un numero entero
y se te dira si es par o no
(-1 para salir)
=============================
"""))
    if numero % 2 == 0:
        print(f"{numero} es un numero par")
    else:
        print(f"{numero} es un numero impar")


print("fin del programa")