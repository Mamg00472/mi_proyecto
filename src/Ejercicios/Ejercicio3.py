numeros = input("Escriba numeros separados por comas: ")
lista = numeros.split(",")
lista_resuelta = []
for num in lista:
    lista_resuelta.append(int(num))
    

lista_resuelta.sort()

print(lista_resuelta)