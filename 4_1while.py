"""
Se requiere un algoritmo para obtener la suma de diez cantidades mediante
la utilización de un ciclo “Mientras”.
"""

suma=0
cont=0

while cont<=9:
    num=int(input("Ingrese el número siguiente "))
    suma=suma+num
    cont+=1
    print(suma)