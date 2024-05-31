"""
El banco “Pueblo desconocido” ha decidido aumentar el límite de crédito de
las tarjetas de crédito de sus clientes, para esto considera que si su cliente
tiene tarjeta tipo 1, el aumento será de 25 %; si tiene tipo 2, será de 35 %;
si tiene tipo 3, de 40 %, y para cualquier otro tipo, de 50 %. Ahora bien, si la
persona cuenta con más de una tarjeta, sólo se considera la de tipo mayor
o la que el cliente indique.
"""

tipo_tarjeta=int(input("Ingrese el tipo de tarjeta: "))

limite_credito=int(input("Ingrese el limite de su credito: "))

if tipo_tarjeta == 1:
    aumento=limite_credito+(limite_credito*0.25)
    nuevo_cre=limite_credito+aumento
    print(aumento)
    print(nuevo_cre)     # probar con elif
elif tipo_tarjeta==2:
        aumento=limite_credito+(limite_credito*0.35)
        nuevo_cre=limite_credito+aumento
        print(aumento)
        print(nuevo_cre)
elif tipo_tarjeta==3:
           aumento=limite_credito+(limite_credito*0.40)
           nuevo_cre=limite_credito+aumento
           print(aumento)
           print(nuevo_cre)
else:
           tipo_tarjeta==4
           aumento=limite_credito+(limite_credito*0.25)
           nuevo_cre=limite_credito+aumento
           print(aumento)
           print(nuevo_cre)

