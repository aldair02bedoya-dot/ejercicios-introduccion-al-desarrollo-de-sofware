votosValidos = int(input("ingrese votos validos: "))
votosPartidos = int(input("ingrese votos por su partido: "))

umbral = votosValidos*0.03

if(votosPartidos > umbral):
    print("tu partido tendra curules")
else:
    print("se quemaron")
