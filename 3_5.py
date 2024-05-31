"""
Se requiere determinar cuál de tres cantidades proporcionadas es la
mayor.
"""

cant_1=int(input("Ingrese el valor de la cantidad 1 "))
print(cant_1)

cant_2=int(input("Ingrese el valor de la cantidad 2 "))
print(cant_2)

cant_3=int(input("Ingrese el valor de la cantidad 3 "))
print(cant_3)

if cant_1>cant_2 and cant_1>cant_3:
    print(f"El valor mayor es: {cant_1}")
else:
    if cant_2>cant_3 and cant_2>cant_3:
        print(f"El valor mayor es: {cant_2}")
    else:
        print(f"El valor mayor es: {cant_3}")

