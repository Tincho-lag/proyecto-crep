# utilidades.py
def es_numero_entero(cadena):
    if not cadena:
        return False
    if cadena[0] == "-":
        cadena = cadena[1:]
    if not cadena:
        return False
    return cadena.isdigit()

# Solicitar un número entero
while True:
    entrada = input("Ingrese un número entero (puede ser negativo): ")
    if es_numero_entero(entrada):
        numero = int(entrada)  # Convertimos solo si es válido
        print("Número válido:", numero)
        break
    else:
        print("Error: Ingrese un número entero válido.")