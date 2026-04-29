matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

for i, tabla in enumerate(matriz):
    for c, elemento in enumerate(tabla):
        if elemento % 2 == 0:
            matriz[i][c] = 0
        else:
            matriz[i][c] = 1

print(matriz)

dict = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
    "ciudad": "Madrid"
}

dict2 = set(["Hola Mundo", "Python", "Programacion"])

print(dict)
print(dict2)

