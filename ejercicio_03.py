# Ejercicio 3: Realiza el promedio de 4 materias y evalúa acceso a beca
matematicas = float(input("ingrese la nota de matematicas: "))
castellano = float(input("ingrese la nota de castellano: "))
ingles = float(input("ingrese la nota de ingles: "))
sociales = float(input("ingrese la nota de sociales: "))

promedio = (matematicas + castellano + ingles + sociales) / 4
print(promedio)

if promedio > 4.5:
    print("puedes acceder a la beca")
else:
    print("aún no puedes acceder a la beca, intenta el otro semestre ")
