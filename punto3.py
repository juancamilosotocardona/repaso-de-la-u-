def dividir(a, b):
    try:
        # convertir a y b a float (pueden venir como str)
        a = float(a)
        b = float(b)
        # realizar la división
        resultado = a / b
        # retornar el resultado
        return resultado
    except ZeroDivisionError:
        print("Error: división por cero")
        return None
    except (TypeError, ValueError):
        print("Error: entradas no numéricas")
        return None

# Pruebas mínimas
print(dividir(10, 2))      # 5.0
print(dividir("9", "3"))   # 3.0
print(dividir(5, 0))       # Error: división por cero → None
print(dividir("a", 2))     # Error: entradas no numéricas → None



def dividir(a, b):
    try:
        # convertir a y b a float (pueden venir como str)
        a = float(a)
        b = float(b)
        # realizar la división
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: división por cero")
        return None
    except (TypeError, ValueError):
        print("Error: entradas no numéricas")
        return None

# Programa principal
a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")

resultado = dividir(a, b)

if resultado is not None:
    print(f"El resultado de la división es: {resultado}")
