"""
Un empleado de la tienda “Tiki Taka” realiza N ventas durante el día, se requiere
saber cuántas de ellas fueron mayores a $1000, cuántas fueron mayores
a $500 pero menores o iguales a $1000, y cuántas fueron menores o
iguales a $500. Además, se requiere saber el monto de lo vendido en cada
categoría y de forma global.
"""

ven_may_1000=0
total_ven_1000=0

ven_501_1000=0
total_ven_501_1000=0

ven_menigu_500=0
total_ven_500=0

ventas_can=input("Ingrese el total de ventas: ")
ventas=[int(x.strip()) for x in ventas_can.split(",")]
print("Lista resultante: ", ventas)

i=0

while i < len(ventas):
    
    ven=ventas[i]

    if ven > 1000:
        ven_may_1000 += 1
        total_ven_1000 += ven
    elif 501 <= ven <= 1000:
        ven_501_1000 += 1
        total_ven_501_1000 +=ven
    else:
        ven_menigu_500 += 1
        total_ven_500 +=ven

    i += 1

total=total_ven_1000+total_ven_501_1000+total_ven_500

print(f"Ventas mayores a $1000: {ven_may_1000}, monto total: ${total_ven_1000}")
print(f"Ventas mayores $500 y menores o iguales a $1000: {ven_501_1000}, monto total: ${total_ven_501_1000}")
print(f"Ventas menores o iguales a $500: {ven_menigu_500}, monto total: ${total_ven_500}")
print(f"Monto total de todas las ventas: ${total}")