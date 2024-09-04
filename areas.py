import math
# Calculation using for and while cycles to calculate the area of various shapes
# Square and rectangle areas

# For
n = 3

for i in range(n):
    l1 = int(input(f"Insertar el lado 1 del cuadrado {i + 1}: "))
    l2 = int(input(f"Insertar el lado 2 del cuadrado {i + 1}: "))
    a = l1 * l2
    print(f"El área del cuadrado {i + 1} es: {a} cm\u00B2")

#While
contador = 0
n = 3

while contador < n:
    l1 = int(input(f"Insertar el lado 1 del cuadrado {contador + 1}: "))
    l2 = int(input(f"Insertar el lado 2 del cuadrado {contador + 1}: "))
    a = l1 * l2
    print(f"El área del cuadrado {contador + 1} es: {a} cm\u00B2")
    
    contador += 1

# Circle area
# For
n = 3

for i in range(n):
    r = int(input(f"Insertar el valor del radio {i + 1}: "))
    a = math.pi*(r**2)
    print(f"El área del circulo {i + 1} es: {a} cm\u00B2")

# While
contador = 0
n = 3

while contador < n:
    r = int(input(f"Insertar el valor del radio {contador + 1}: "))
    a = math.pi*(r**2)
    print(f"El área del circulo {contador + 1} es: {a} cm\u00B2")
    contador += 1

# Triangle area knowing base and height
# For
n=3

for i in range(n):
    b=int(input(f"Inserte la base del triángulo {i+1}: "))
    al=int(input(f"Inserte la altura del triángulo {i+1}: "))
    a=(b*al)/2
    print(f"El área del triángulo {i+1} es: {a} cm\u00B2")

# While
contador=0
n=3

while contador < n:
    b=int(input(f"Inserte la base del triángulo {contador+1}: "))
    al=int(input(f"Inserte la altura del triángulo {contador+1}: "))
    a=(b*al)/2
    print(f"El área del triángulo {contador+1} es: {a} cm\u00B2")
    contador += 1

# Area of the triangle without knowing the base and height, only the length of the sides.
# For

n=3
for i in range(n):
    a=int(input(f"Inserte el primer lado del triángulo {i+1}: "))
    b=int(input(f"Inserte el segundo lado del triángulo {i+1}: "))
    c=int(input(f"Inserte el tercer lado del triángulo {i+1}: "))
    s=(a+b+c)/2
    a=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"El área del triángulo {i+1} es: {a}cm\u00B2")

# While

contador=0
n=3

while contador < n:
    a=int(input(f"Inserte el primer lado del triángulo {contador+1}: "))
    b=int(input(f"Inserte el segundo lado del triángulo {contador+1}: "))
    c=int(input(f"Inserte el tercer lado del triángulo {contador+1}: "))
    s=(a+b+c)/2
    a=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"El área del triángulo {contador+1} es: {a}cm\u00B2")
    contador += 1

# Area of a trapezoid
# For

n=3

for i in range(n):
    b1=int(input(f"Inserte la primera base del trapecio{i+1}: "))
    b2=int(input(f"Inserte la segunda base del trapecio{i+1}: "))
    h=int(input(f"Ingrese la altura del trapecio {i+1}: "))
    a=(b1+b2)*h/2
    print(f"El área del trapecio {i+1} es de: {a}cm\u00B2")

# While
contador=0
n=3

while contador < n:
    b1=int(input(f"Inserte la primera base del trapecio{contador+1}: "))
    b2=int(input(f"Inserte la segunda base del trapecio{contador+1}: "))
    h=int(input(f"Ingrese la altura del trapecio {contador+1}: "))
    a=(b1+b2)*h/2
    print(f"El área del trapecio {contador+1} es de: {a}cm\u00B2")
    contador += 1