"""
Realice un diagrama de flujo y pseudocódigo que representen el algoritmo
para determinar cuánto dinero ahorra una persona en un
año si considera que cada semana ahorra 15% de su sueldo (considere
cuatro semanas por mes y que no cambia el sueldo).
"""

sueldo = int(input("Ingres el valor del sueldo al mes "))
print(sueldo)

ahorro= (sueldo*0.15)
print(f"El ahorro mensual es:  {ahorro}")