def formatear_nombre(nombre: str) -> str:
    # validar string no vacío
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    # partir por espacios, ignorando múltiples espacios
    partes = nombre.strip().split()

    # verificar que haya al menos 2 palabras
    if len(partes) < 2:
        raise ValueError("Debe ingresar al menos nombre y apellido")

    # primera palabra = Nombre, última = Apellido
    nombre_propio = partes[0].capitalize()
    apellido = partes[-1].capitalize()

    # construir formato "Apellido, Nombre"
    return f"{apellido}, {nombre_propio}"


# Pruebas mínimas
print(formatear_nombre("juan perez"))          # "Perez, Juan"
print(formatear_nombre("   maria    lopez  ")) # "Lopez, Maria"
print(formatear_nombre("Carlos"))              # ❌ ValueError
print(formatear_nombre(""))                    # ❌ ValueError


"""
def formatear_nombre(nombre: str) -> str:
    # validar string no vacío
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    # partir por espacios, ignorando múltiples espacios
    partes = nombre.strip().split()

    # verificar que haya al menos 2 palabras
    if len(partes) < 2:
        raise ValueError("Debe ingresar al menos nombre y apellido")

    # primera palabra = Nombre, última = Apellido
    nombre_propio = partes[0].capitalize()
    apellido = partes[-1].capitalize()

    # construir formato "Apellido, Nombre"
    return f"{apellido}, {nombre_propio}"


# Programa principal
try:
    nombre_usuario = input("Ingrese su nombre completo: ")
    resultado = formatear_nombre(nombre_usuario)
    print("Nombre formateado:", resultado)
except ValueError as e:
    print("Error:", e)

"""