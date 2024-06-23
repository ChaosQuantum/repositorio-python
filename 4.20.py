'''
Realice un algoritmo para obtener el seno de un ángulo
Utilizando la serie de Taylor para el seno de un angulo x (en radiantes)
'''
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def seno(x, num_terms=10):
    resultado = 0
    for n in range(num_terms):
        termino = ((-1)**n) * (x**(2*n+1)) / factorial(2*n+1)
        resultado += termino
    return resultado

# Ejemplo de uso:
angulo_grados = 30  # ángulo en grados
angulo_radianes = math.radians(angulo_grados)  # conversión a radianes
num_terms = 10  # número de términos de la serie de Taylor

resultado = seno(angulo_radianes, num_terms)
print(f"sen({angulo_grados}°) ≈ {resultado:.10f}")

# Comparación con el valor de math.sin
print(f"Valor exacto usando math.sin: {math.sin(angulo_radianes):.10f}")
