num = int(input("Escribe un numero: "))

if num < 2:
    print(f"el {num} no es considerado primo")
else:
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} no es un numero primo")
            break
    else:
        print(f"{num} es un numero primo")
            