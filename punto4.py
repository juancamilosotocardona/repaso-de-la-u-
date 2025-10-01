def analizar_texto(texto: str) -> tuple[int, int, str]:
    # validar texto no vacío
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío")

    def contar_palabras(t: str) -> int:
        # separar por espacios y contar
        return len(t.split())

    def contar_vocales(t: str) -> int:
        # contar vocales mayúsculas y minúsculas
        vocales = "aeiouAEIOU"
        return sum(1 for c in t if c in vocales)

    def palabra_mas_larga(t: str) -> str:
        # dividir en palabras y encontrar la más larga
        palabras = t.split()
        return max(palabras, key=len) if palabras else ""

    # retornar tupla con resultados
    return (contar_palabras(texto), contar_vocales(texto), palabra_mas_larga(texto))


# Pruebas mínimas
print(analizar_texto("Hola mundo"))         
# (2, 4, "mundo")

print(analizar_texto("Esto es una prueba de funciones"))  
# (6, 11, "funciones")

print(analizar_texto("Python"))             
# (1, 1, "Python")


"""
def analizar_texto(texto: str) -> tuple[int, int, str]:
    # validar texto no vacío
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío")

    def contar_palabras(t: str) -> int:
        return len(t.split())

    def contar_vocales(t: str) -> int:
        vocales = "aeiouAEIOU"
        return sum(1 for c in t if c in vocales)

    def palabra_mas_larga(t: str) -> str:
        palabras = t.split()
        return max(palabras, key=len) if palabras else ""

    return (contar_palabras(texto), contar_vocales(texto), palabra_mas_larga(texto))


# Programa principal
texto = input("Ingrese un texto: ")

try:
    num_palabras, num_vocales, palabra_larga = analizar_texto(texto)
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de vocales: {num_vocales}")
    print(f"Palabra más larga: {palabra_larga}")
except ValueError as e:
    print("Error:", e)


"""