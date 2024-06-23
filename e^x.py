'''
Realice un algoritmo para obtener una función exponencial, la cual está dada por: e^x
La función exponencial  e^x se puede aproximar utilizando la serie de Taylor
'''

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def exponencial(x, num_terms=10):
    resultado = 0
    for n in range(num_terms):
        resultado += (x**n) / factorial(n)
    return resultado

# Ejemplo de uso:
x = 5  # valor de x para e^x
num_terms = 20  # número de términos de la serie de Taylor

resultado = exponencial(x, num_terms)
print(f"e^{x} ≈ {resultado:.10f}")

# Comparación con el valor de math.exp
print(f"Valor exacto usando math.exp: {math.exp(x):.10f}")
