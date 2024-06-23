'''
Realice el algoritmo para determinar cuánto pagará una persona que
adquiere N artículos, los cuales están de promoción. Considere que
si su precio es mayor o igual a $200 se le aplica un descuento de 15%,
y si su precio es mayor a $100 pero menor a $200, el descuento es de
12%; de lo contrario, sólo se le aplica 10%. Se debe saber cuál es el
costo y el descuento que tendrá cada uno de los artículos y finalmente
cuánto se pagará por todos los artículos obtenidos.
'''

def calcular_total_articulos(n, precios):
    total_pago = 0
    detalles_articulos = []

    for precio in precios:
        if precio >= 200:
            descuento = 0.15
        elif precio > 100:
            descuento = 0.12
        else:
            descuento = 0.10

        descuento_aplicado = precio * descuento
        precio_final = precio - descuento_aplicado
        total_pago += precio_final

        detalles_articulos.append({
            'costo': precio,
            'descuento': descuento_aplicado,
            'precio_final': precio_final
        })

    return total_pago, detalles_articulos

# Ejemplo de uso:
n = 3  # número de artículos
precios = [250, 150, 90]  # lista de precios de los artículos

total_pago, detalles_articulos = calcular_total_articulos(n, precios)

print(f"Total a pagar por todos los artículos: ${total_pago:.2f}")
print("\nDetalles de cada artículo:")
for i, detalle in enumerate(detalles_articulos, start=1):
    print(f"Artículo {i}: Costo: ${detalle['costo']:.2f}, Descuento: ${detalle['descuento']:.2f}, Precio final: ${detalle['precio_final']:.2f}")
