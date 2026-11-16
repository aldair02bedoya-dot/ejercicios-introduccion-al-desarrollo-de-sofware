# Ejercicio 4: Ganancia por inversión en banco con interés del 2%
capital = int(input("Ingrese el monto a invertir: "))
dias = int(input("ingrese el numero total de dias del mes a considerar: "))

interes = 0.02
ganancia = (capital * dias) * interes

print("La ganancia por cobrar después del mes es de:")
print(ganancia)
