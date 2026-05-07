frase = input("Escribe una frase: ")
palabras = 0

lista = frase.split()
for palabra in lista:
    palabras +=1

print(f"la frase tiene {palabras} palabras")