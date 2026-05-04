contador= 0
palabra = input("Escribe la palabra a buscar: ")

with open("../Documentos/Ejercicio_10.txt", "r", encoding="utf-8") as f:
    for linea in f:
        contador += linea.count(palabra)

if contador == 0:
    print(f"La palabra {palabra} no se ha encontrado en el documento")
else:
    print(f"La palabra {palabra} se ha encontrado {contador} veces")
