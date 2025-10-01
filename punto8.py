def leer_entero(msg: str) -> int:
    while True:
        try:
            valor = int(input(msg))  # leer y convertir a entero
            return valor             # si todo bien, lo retorna
        except ValueError:
            print("Error: debe ingresar un número entero válido. Intente de nuevo.")

# Ejemplo de uso
n = leer_entero("Ingrese un número entero: ")
print(f"El número válido ingresado es: {n}")

"""
def leer_entero(msg: str) -> int:
    while True:
        try:
            valor = int(input(msg))  # 👉 el usuario escribe aquí
            return valor             # si es válido, lo devuelve
        except ValueError:
            print("Error: debe ingresar un número entero válido. Intente de nuevo.")

# Programa principal
numero = leer_entero("Ingrese un número entero: ")
print(f"El número válido ingresado es: {numero}")

"""