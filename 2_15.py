"""
Se desea calcular la potencia eléctrica de circuito de la figura 2.6. Realice
un diagrama de flujo y el pseudocódigo que representen el algoritmo
para resolver el problema. Considere que: P = V*I y V = R*I.
"""

resistencia=int(input("Ingrese el valor de la resistencia en Ohm "))
print(resistencia)

voltaje=int(input("Ingrese el valor del voltaje de la fuenete en voltios "))
print(voltaje)

corriente=voltaje/resistencia
print(f"El valor de la corriente es de: {corriente}")

potencia=voltaje*corriente
print(f"El valor de la potencia es: {potencia}")
