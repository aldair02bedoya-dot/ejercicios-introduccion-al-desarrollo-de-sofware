def cifrado_cesar(mensaje):
    resultado = ""

    for letra in mensaje.upper():
        if letra.isalpha():
            nueva = chr((ord(letra) - 65 + 3) % 26 + 65)
            resultado += nueva
        else:
            resultado += letra

    return resultado
mensaje = input("Ingrese un mensaje: ")
print("mensaje encriptado:", cifrado_cesar(mensaje))
