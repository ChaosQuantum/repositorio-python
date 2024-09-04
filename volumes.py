import math
# Calculation to know the volume of several figures with for and while cycles.
# Volume cube

# For
n=3

for i in range(n):
    a=int(input(f"Ingrese el valor de uno de los lados del cubo {i+1}: "))
    V=a**3
    print(f"El volumen del cubo {i+1} es: {V} cm\u00B3")

# While
contador=0
n=3

while contador < n:
    a=int(input(f"Ingrese el valor de uno de los lados del cubo {contador+1}: "))
    V=a**3
    print(f"El volumen del cubo {contador+1} es: {V} cm\u00B3")
    contador += 1

# Rectangular prism volume

# For
n=3

for i in range(n):
    l=int(input(f"Ingrese el valor de la longitud del prisma rectangular {i+1}: "))
    w=int(input(f"Ingrese el valor del ancho del prisma rectangular {i+1}: "))
    h=int(input(f"Ingrese el valor de la altura del prisma rectangular {i+1}: "))
    V=l*w*h
    print(f"El volumen del prisma rectangular {i+1} es: {V} cm\u00B3")

# While
contador=0
n=3

while contador < n:
    l=int(input(f"Ingrese el valor de la longitud del prisma rectangular {contador+1}: "))
    w=int(input(f"Ingrese el valor del ancho del prisma rectangular {contador+1}: "))
    h=int(input(f"Ingrese el valor de la altura del prisma rectangular {contador+1}: "))
    V=l*w*h
    print(f"El volumen del prisma rectangular {contador+1} es: {V} cm\u00B3")
    contador += 1

# Pyramid volume
# For
n=3

for i in range(n):
    b=int(input(f"Ingrese el valor de la base de la pirámide {i+1}: "))
    h=int(input(f"Ingrese el valor de la altura de la pirámide {i+1}: "))
    B=b*b
    V=(B*h)/3
    print(f"El volumen de la pirámide {i+1} es: {V} cm\u00B3")

# While
contador=0
n=3

while contador < n:
    b=int(input(f"Ingrese el valor de la base de la pirámide {contador+1}: "))
    h=int(input(f"Ingrese el valor de la altura de la pirámide {contador+1}: "))
    B=b*b
    V=(B*h)/3
    print(f"El volumen de la pirámide {contador+1} es: {V} cm\u00B3")
    contador += 1

# Cone volume
# For
n=3

for i in range(n):
    r=int(input(f"Ingrese el valor del radio de la base del cono {i+1}: "))
    h=int(input(f"Ingrese el valor de la altura del cono {i+1}: "))
    V=(math.pi*(r**2)*h)/3
    print(f"El volumen del cono {i+1} es: {V} cm\u00B3")

# While
contador=0
n=3

while contador < n:
    r=int(input(f"Ingrese el valor del radio de la base del cono {contador+1}: "))
    h=int(input(f"Ingrese el valor de la altura del cono {contador+1}: "))
    V=(math.pi*(r**2)*h)/3
    print(f"El volumen del cono {contador+1} es: {V} cm\u00B3")
    contador += 1

# Truncated cone volume
# For
n=3

for i in range(n):
    R=int(input(f"Ingrese el valor del radio de la base mayor del cono truncado {i+1}: "))
    r=int(input(f"Ingrese el valor del radio de la base menor del cono truncado {i+1}: "))
    h=int(input(f"Ingrese la altura del cono truncado {i+1}: "))
    V=((1/3)*math.pi*h)*(R**2+R*r+r**2)
    print(f"El volumen del cono truncado {i+1} es: {V} cm\u00B3")

# While
contador=0
n=3

while contador < n:
    R=int(input(f"Ingrese el valor del radio de la base mayor del cono truncado {contador+1}: "))
    r=int(input(f"Ingrese el valor del radio de la base menor del cono truncado {contador+1}: "))
    h=int(input(f"Ingrese la altura del cono truncado {contador+1}: "))
    V=((1/3)*math.pi*h)*(R**2+R*r+r**2)
    print(f"El volumen del cono truncado {contador+1} es: {V} cm\u00B3")
    contador += 1


# Sphere volume
# For
n=3

for i in range(n):
    r=int(input(f"Ingrese el radio de la esfera {i+1}: "))
    V=(4*math.pi*(r**3))/3
    print(f"El volumen de la esfera {i+1} es: {V} cm\u00B3")

# While
contador=0
n=3

while contador < n:
    r=int(input(f"Ingrese el radio de la esfera {contador+1}: "))
    V=(4*math.pi*(r**3))/3
    print(f"El volumen de la esfera {contador+1} es: {V} cm\u00B3")
    contador += 1