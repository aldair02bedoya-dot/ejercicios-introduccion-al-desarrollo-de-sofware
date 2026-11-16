print(" BIENVENIDOS A LA TIENDA DE PRODUCTOS ")
print("1 = (energizante)")
print("2 = (helado)")
print("3 = (gaseosa)")
print("4 = (manzana)")
print("5 = (naranja)")

menu= int(input("Ingrese un número del 1 al 5 para escoger un producto o 0 para salir: "))

while menu != 0:
    if menu == 1:
        print(f"{1} cuesta $10.000")
    elif menu == 2:
        print(f"{2} cuesta $20.000")
    elif menu == 3:
        print(f"{3} cuesta $30.000")
    elif menu == 4:
        print(f"{4} cuesta $40.000")
    elif menu == 5:
        print(f"{5} cuesta $50.000")
    else:
        print("Opción inválida, por favor ingrese un número del 1 al 5 o 0 para salir.")
    menu= int(input("Ingrese un número del 1 al 5 para escoger un producto o 0 para salir: "))
