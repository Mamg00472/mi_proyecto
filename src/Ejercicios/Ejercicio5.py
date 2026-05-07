def numeros_fibonacci(count):
    num_siguiente = 0
    num_actual = 1
    num_anterior = 0
    while count > 0:
        print(f"{num_siguiente}, ", end="")
        num_siguiente = num_actual + num_anterior
        num_anterior = num_actual
        num_actual = num_siguiente
        
        
        count-=1

num = int(input("Escriba cuantos numeros de fibonacci quiere ver: "))
numeros_fibonacci(num)