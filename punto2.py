def convertir_temperatura(valor: float, escala: str) -> float:
    """Convierte temperaturas entre C y F según escala."""
    if escala == 'C->F':
        # fórmula: (°C × 9/5) + 32 = °F
        return (valor * 9/5) + 32
    elif escala == 'F->C':
        # fórmula: (°F − 32) × 5/9 = °C
        return (valor - 32) * 5/9
    else:
        # escala inválida
        raise ValueError("Escala no válida. Use 'C->F' o 'F->C'.")

# Pruebas mínimas
print(convertir_temperatura(0, 'C->F'))     # 32.0
print(convertir_temperatura(32, 'F->C'))    # 0.0



#def convertir_temperatura(valor: float, escala: str) -> float:
    #"""Convierte temperaturas entre C y F según escala."""
    #if escala == 'C->F':
        #return (valor * 9/5) + 32
    #elif escala == 'F->C':
        #return (valor - 32) * 5/9
    #else:
        #raise ValueError("Escala no válida. Use 'C->F' o 'F->C'.")

# Programa principal
#valor = float(input("Ingrese el valor de la temperatura: "))
#escala = input("Ingrese la escala ('C->F' o 'F->C'): ")

#try:
    #resultado = convertir_temperatura(valor, escala)
    #if escala == 'C->F':
       # print(f"{valor} °C equivalen a {resultado:.2f} °F")
    #elif escala == 'F->C':
        #print(f"{valor} °F equivalen a {resultado:.2f} °C")
#except ValueError as e:
    #print("Error:", e)

