def es_par(n: int) -> bool:
    """Retorna True si n es par, False en caso contrario."""
    return n % 2 == 0

# Pruebas mínimas
print(es_par(2))   # True
print(es_par(7))   # False
print(es_par(0))   # True

"""
def es_par(n: int) -> bool:
    """Retorna True si n es par, False en caso contrario."""
    return n % 2 == 0


# Programa principal: el usuario digita el número
numero = int(input("Digite un número entero: "))
if es_par(numero):
    print(f"{numero} es par ->", es_par(numero))
else:
    print(f"{numero} es impar ->", es_par(numero))

""" 
