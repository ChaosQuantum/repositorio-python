"""
Una empresa les paga a sus empleados con base en las horas trabajadas en
la semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
"""

numero_empleados=int(input("Ingrese el número de empleados: "))

tarifa_hora=1500

total_pago=0

i=1

for i in range(numero_empleados):
    horas_trabajadas = int(input(f"Ingrese las horas trabajadas {i}: "))
    sueldo_semana = horas_trabajadas * tarifa_hora
    total_pago += sueldo_semana
    print(f"El sueldo semanal del empleado {i} es: ${sueldo_semana}")
    i+=1

print(f"La empresa paga por {numero_empleados} empleados un total de: ${total_pago}")