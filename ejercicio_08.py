# Ejercicio 8: Descuento del 25% en entrada al circo para menores de 10 años
p = float(input("Ingrese el precio de la entrada: "))
edad = int(input("Ingrese la edad del cliente: "))

if edad < 10:
    p = p - (p * 0.25)

print("El monto final a pagar es", p)
