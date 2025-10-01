# Definición de excepción personalizada
class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad no está en el rango permitido."""
    pass

def verificar_edad(edad: int) -> str:
    # validar tipo
    if not isinstance(edad, int):
        raise EdadInvalidaError("La edad debe ser un número entero")
    # validar rango
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 0 y 120")
    # si todo bien
    return "Edad válida"


# Ejemplos de uso
try:
    print(verificar_edad(25))   # ✅ Edad válida
    print(verificar_edad(-5))   # ❌ Levanta EdadInvalidaError
except EdadInvalidaError as e:
    print("Error:", e)




"""# Definición de excepción personalizada
class EdadInvalidaError(Exception):

def verificar_edad(edad: int) -> str:
    # validar tipo
    if not isinstance(edad, int):
        raise EdadInvalidaError("La edad debe ser un número entero")
    # validar rango
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 0 y 120")
    # si todo bien
    return "Edad válida"

# Programa principal
try:
    edad = int(input("Ingrese su edad: "))
    print(verificar_edad(edad))
except ValueError:
    print("Error: debe ingresar un número entero.")
except EdadInvalidaError as e:
    print("Error:", e)"""""