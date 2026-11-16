#velocidades en colombia
velocidad = float(input("menciona una velocidad en Colombia:"))
if velocidad > 0 and velocidad <= 30 :
    print("zonas escolares")
elif velocidad > 30 and velocidad <= 60:
    print("zonas urbanas")
elif velocidad > 60 and velocidad <= 80:
    print("zonas rurales")
elif velocidad > 80 and velocidad <= 100:
    print("rutas nacionales")
else:
    print("velocidad no permitida")
