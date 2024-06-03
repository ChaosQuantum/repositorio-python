"""
Se requiere un algoritmo para determinar cuánto ahorrará una persona
en un año, si al final de cada mes deposita variables cantidades de dinero;
además, se requiere saber cuánto lleva ahorrado cada mes.
"""

ahorro_mensual=0
mes=2

while mes<=11:
    dinero=int(input("Escribir el ahorro del mes: "))
    ahorro_mensual=ahorro_mensual+dinero
    print("El ahorro del mes: ", mes, " es de ", ahorro_mensual)
    mes+=1

print("El ahorro en un año es: ", ahorro_mensual)