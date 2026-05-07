texto = input("Escriba un texto: ")

diccionario = {}
lista = texto.split()



for palabra in lista:
    if palabra in diccionario:
        diccionario[palabra] = diccionario[palabra] +1
    else:
        diccionario[palabra] = 1

print(diccionario)
    