frase = input("Escribe una frase y se te dira si es un polindromo: ")
frase = frase.lower()
frase = frase.replace(" ", "")

lista = list(frase)
print(lista)

lista.reverse()

frase_al_reves = "".join(lista)

if frase_al_reves == frase:
    print("Has escrito un políndromo")
else:
    print("no es un polindromo")