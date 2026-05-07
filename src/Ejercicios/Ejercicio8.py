n = int(input("Introduce el tamaño de la matriz identidad: "))

matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    for num in fila:
        print(num, end="")

    print()
        