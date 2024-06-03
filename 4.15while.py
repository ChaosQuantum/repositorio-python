"""
Una empresa les paga a sus empleados con base en las horas trabajadas en
la semana. Para esto, se registran los días que laboró y las horas de cada
día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores
y además calcule cuánto pagó la empresa por los N empleados.
"""

numero_empleados=int(input("Ingrese el número de empleados: "))

tarifa_hora=1500

pago_total=0

i=1

while i <= numero_empleados:
    numero_dias=int(input(f"Días trabajados del empleado {i} en la semana: "))
    total_horas=0
    j=1
    while j <= numero_dias:
        horas_dia=int(input(f"Ingrese las horas trabajadas en el día {j} para el empleado {i}: "))
        total_horas+=horas_dia
        j+=1
    sueldo_semana=total_horas*tarifa_hora
    pago_total+=sueldo_semana
    print(f"El sueldo semanal del empleado {i} es: ${sueldo_semana}")
    i+=1

print(f"El pago total por la empresa para {numero_empleados} empleados es: ${pago_total}")
 
