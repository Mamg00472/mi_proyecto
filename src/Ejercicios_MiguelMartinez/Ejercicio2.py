numero = 0

def calcular_factorial(num):
    contador = num -1
    while contador > 0:
        num *= contador
        contador -= 1
    print(num)

while numero >= 0:
    numero = int(input("""
=================================================
Escriba el numero que quieres calcular su factorial
(0, 1 y no estan aceptados en este programa)
(escribe un numero negativo para salir)
=================================================
"""))
    if numero == 0 or numero == 1:
        print(f"{numero} es un numer no aceptado")
    elif numero < 0:
        print("Fin del programa")
        break
    else:
        calcular_factorial(numero)
        
