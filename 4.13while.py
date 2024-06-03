"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes
pagó $10, el segundo $20, el tercero $40 y así sucesivamente. Realice un
algoritmo para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses.
"""

meses=21

pago_inicial=10

mes=1

pago_actual=pago_inicial

pago_total=0



while mes < meses:
    print(f"Mes {mes}: pago {pago_actual}")
    pago_total += pago_actual
    pago_actual *= 2
    mes += 1

print(f"Total pago despues de {meses} meses: ${pago_total}")
    