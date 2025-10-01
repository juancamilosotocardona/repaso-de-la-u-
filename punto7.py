def estadisticas(valores: list) -> dict:
    if not isinstance(valores, list):
        raise TypeError("Se esperaba una lista")
    
    if not valores:
        # Decisión: lanzar ValueError porque no se puede calcular estadísticas de lista vacía
        raise ValueError("La lista no puede estar vacía")

    # validar que todos sean numéricos
    for v in valores:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Valor no numérico encontrado: {v}")

    # cálculos
    mayor = max(valores)
    menor = min(valores)
    promedio = sum(valores) / len(valores)
    pares = sum(1 for v in valores if isinstance(v, int) and v % 2 == 0)

    return {
        "mayor": mayor,
        "menor": menor,
        "promedio": promedio,
        "pares": pares,
    }


# Pruebas mínimas
print(estadisticas([1, 2, 3, 4, 5]))
# {"mayor": 5, "menor": 1, "promedio": 3.0, "pares": 2}

print(estadisticas([10.5, 2, 8, 4.5]))
# {"mayor": 10.5, "menor": 2, "promedio": 6.25, "pares": 1}


"""
def estadisticas(valores: list) -> dict:
    if not isinstance(valores, list):
        raise TypeError("Se esperaba una lista")
    
    if not valores:
        # Decisión: lanzar ValueError porque no se puede calcular estadísticas de lista vacía
        raise ValueError("La lista no puede estar vacía")

    # validar que todos sean numéricos
    for v in valores:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Valor no numérico encontrado: {v}")

    # cálculos
    mayor = max(valores)
    menor = min(valores)
    promedio = sum(valores) / len(valores)
    pares = sum(1 for v in valores if isinstance(v, int) and v % 2 == 0)

    return {
        "mayor": mayor,
        "menor": menor,
        "promedio": promedio,
        "pares": pares,
    }

# Programa principal
try:
    entrada = input("Ingrese números separados por comas: ")
    lista = [float(x.strip()) for x in entrada.split(",") if x.strip()]

    resultado = estadisticas(lista)
    print("Resultados:")
    print(f"Mayor: {resultado['mayor']}")
    print(f"Menor: {resultado['menor']}")
    print(f"Promedio: {resultado['promedio']:.2f}")
    print(f"Cantidad de pares: {resultado['pares']}")

except ValueError as e:
    print("Error:", e)
except TypeError as e:
    print("Error:", e)


"""