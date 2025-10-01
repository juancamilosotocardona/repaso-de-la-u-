def es_par(n: int) -> bool:
    """Retorna True si n es par, False en caso contrario."""
    return n % 2 == 0

# Pruebas mínimas
print(es_par(2))   # True
print(es_par(7))   # False
print(es_par(0))   # True
