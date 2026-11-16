try:
    n = int(input("Ingrese un número n: "))

    contador = 0
    for i in range(0, n + 1, 2):
        print(i, end=" ")
        contador += 1
        if contador % 10 == 0:
            print()

except ValueError:
    print("Error: Debe ingresar un número entero.")
