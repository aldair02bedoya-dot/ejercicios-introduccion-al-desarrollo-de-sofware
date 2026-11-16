# Ejercicio 7: Bonificación del 7% sobre el sueldo básico si el trabajador tiene hijos
nombre = input("Ingrese el nombre del trabajador: ")
basico = float(input("Ingrese el sueldo basico: "))
hijos = int(input("Ingrese el numero de hijos: "))

bonificacion = 0
if hijos > 0:
    bonificacion = basico * 0.07

final = basico + bonificacion
print("La bonificacion es:", bonificacion)
print("El sueldo final es:", final)
