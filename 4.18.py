'''
En 1961, una persona vendió las tierras de su abuelo al gobierno
por la cantidad de $1500. Suponga que esta persona ha colocado el
dinero en una cuenta de ahorros que paga 15% anual. ¿Cuánto vale
ahora su inversión? P(1+i)^n. Realice un algoritmo para obtener este
valor
P(1+i)^n
Donde:

P es el monto principal (inicial) de la inversión.
i es la tasa de interés anual.
n es el número de años.
En este caso:
P=1500 dólares.
i=0.15 (15% anual).
n=2024−1961 (la cantidad de años desde 1961 hasta 2024).
'''

def calcular_valor_futuro(P, i, n):
    return P * (1 + i) ** n

# Datos iniciales
P = 1500  # Monto inicial de la inversión
i = 0.15  # Tasa de interés anual (15%)
año_inicial = 1961
año_actual = 2024
n = año_actual - año_inicial  # Número de años

valor_futuro = calcular_valor_futuro(P, i, n)

print(f"El valor de la inversión en el año {año_actual} es: ${valor_futuro:.2f}")
