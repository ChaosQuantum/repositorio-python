"""
“La langosta ahumada” es una empresa dedicada a ofrecer banquetes; sus
tarifas son las siguientes: el costo de platillo por persona es de $95.00,
pero si el número de personas es mayor a 200 pero menor o igual a 300,
el costo es de $85.00. Para más de 300 personas el costo por platillo es de
$75.00. Se requiere un algoritmo que ayude a determinar el presupuesto
que se debe presentar a los clientes que deseen realizar un evento.
"""

comensales=int(input("Ingrese la cantidad de comensales: "))
print(comensales)

if comensales>200 or comensales<=300:
    precio=comensales*85.00
    print(f"La cuenta a pagar es de: {precio}")
else:
    if comensales>300:
        precio=comensales*75.00
        print(f"La cuenta a pagar es de: {precio}")
    else:
        precio=comensales*95.00
        print(f"La cuenta a pagar es de: {precio}")