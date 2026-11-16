# Ejercicio 6: Consumo de gasolina y velocidad media
km_recorrido = float(input("Ingrese el total de km recorridos: "))
precio = float(input("Ingrese el precio de la gasolina (por litro): "))
dinero = float(input("Ingrese el dinero gastado en el viaje: "))
horas = float(input("Ingrese el tiempo de horas del viaje: "))
minutos = float(input("Ingrese el tiempo adicional de minutos: "))

consumo_gaso_total = dinero / precio
consumo_gaso_km = consumo_gaso_total / km_recorrido  # Total en litros por km
consumo_gaso_100km = consumo_gaso_km * 100  # Litros por 100 kilometros
precio_gaso_km = consumo_gaso_km * precio
precio_gaso_100km = precio_gaso_km * 100  # Gasto en euros por 100 kilometros
vel_km_hora = km_recorrido / (horas + (minutos / 60))
vel_metr_seg = (km_recorrido * 1000) / ((horas * 3600) + (minutos * 60))

print("El consumo de gasolina en litros por 100 kilometros es:", consumo_gaso_100km)
print("El consumo de gasolina en euros por 100 kilometros es:", precio_gaso_100km)
print("El consumo de gasolina en litros por kilometro es:", consumo_gaso_km)
print("El consumo de gasolina en euros por kilometro es:", precio_gaso_km)
print("La velocidad media de Km/Hora es:", vel_km_hora)
print("La velocidad media de metros/seg es:", vel_metr_seg)
