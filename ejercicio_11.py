# Ejercicio 11: Categorización de postulantes según sexo y edad
sexo = input("Ingrese el sexo del postulante (Femenino / Masculino): ")
edad = int(input("Ingrese la edad del postulante: "))

if sexo in ("Femenino", "femenino", "F", "f"):
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
else:
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"

print("La categoria del postulante es:", categoria)
