# --- Contenido de mini_utils.py ---

def cuadrado(n: int) -> int:
    # validar tipo
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un entero")
    return n * n


def es_mayus(cadena: str) -> bool:
    # validar tipo
    if not isinstance(cadena, str):
        raise TypeError("El valor debe ser una cadena de texto")
    return cadena.isupper()


# --- Contenido de main.py ---

from mini_utils import cuadrado, es_mayus

def main():
    # el usuario digita el número
    num_txt = input("Digite un número entero: ")
    try:
        num = int(num_txt)  # conversión a entero
        print("El cuadrado es:", cuadrado(num))
    except (TypeError, ValueError) as e:
        print("Error con el número:", e)

    # el usuario digita el texto
    texto = input("Digite un texto: ")
    try:
        if es_mayus(texto):
            print("El texto está en MAYÚSCULAS")
        else:
            print("El texto NO está en mayúsculas")
    except TypeError as e:
        print("Error con el texto:", e)

if __name__ == "__main__":
    main()

"""
# --- Contenido de mini_utils.py ---
def cuadrado(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un entero")
    return n * n

def es_mayus(cadena: str) -> bool:
    if not isinstance(cadena, str):
        raise TypeError("El valor debe ser una cadena de texto")
    return cadena.isupper()


# --- Contenido de main.py ---
from mini_utils import cuadrado, es_mayus

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1) Calcular cuadrado")
        print("2) Verificar si un texto está en mayúsculas")
        print("3) Salir")
        opcion = input("Digite una opción: ").strip()

        if opcion == "1":
            num_txt = input("Digite un número entero: ")
            try:
                num = int(num_txt)
                print("El cuadrado es:", cuadrado(num))
            except (TypeError, ValueError) as e:
                print("Error con el número:", e)

        elif opcion == "2":
            texto = input("Digite un texto: ")
            try:
                if es_mayus(texto):
                    print("El texto está en MAYÚSCULAS")
                else:
                    print("El texto NO está en mayúsculas")
            except TypeError as e:
                print("Error con el texto:", e)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()


"""

