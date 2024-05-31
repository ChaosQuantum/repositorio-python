"""
Realice un diagrama de flujo y pseudocódigo que representen el algoritmo
para determinar aproximadamente cuántos meses, semanas,
días y horas ha vivido una persona.
"""

años=int(input("Ingrese su edad actual en años "))
print(años)

dias=años*365
print(f"Su edad en días es: {dias}")

semanas=años*52
print(f"Su edad en semanas es: {semanas}")

meses=años*12
print(f"Su edad en edad en meses es: {meses}")

horas=años*8760
print(f"Su edad en horas es: {horas}")