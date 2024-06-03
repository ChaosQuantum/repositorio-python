"""
Se requiere un algoritmo para obtener la suma de diez cantidades mediante
la utilización de un ciclo “Mientras”.
"""

suma=0
cont=0

for cont in range(10):
    num=int(input("Ingrese el número siguiente: "))
    suma += num
    print("Suma actual: ", suma)