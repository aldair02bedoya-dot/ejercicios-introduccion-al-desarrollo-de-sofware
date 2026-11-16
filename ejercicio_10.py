# Ejercicio 10: Cambio de moneda de soles a dólares o euros
nombre = input("Ingrese el nombre cliente: ")
monto = float(input("Ingrese el monto a cambiar en soles: "))
print("Seleccion moneda de cambio")
print("[1]Dolares [2]Euros")
moneda = int(input())

if moneda == 1:
    cambio = monto / 2.35
    simbolo = "$"
else:
    cambio = monto / 3.58
    simbolo = "€"

print("Se cambio en", simbolo, cambio)
