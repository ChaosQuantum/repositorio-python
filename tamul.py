'''
Realice un algoritmo para obtener la tabla de multiplicar de un entero
K comenzando desde el 1.
'''

def tabla_de_multiplicar(K, hasta=10):
    tabla = []
    for i in range(1, hasta + 1):
        resultado = K * i
        tabla.append((K, i, resultado))
    return tabla

# Ejemplo de uso:
K = 5  # valor del entero K para obtener la tabla de multiplicar
hasta = 10  # límite superior para la tabla de multiplicar

tabla = tabla_de_multiplicar(K, hasta)

print(f"Tabla de multiplicar del {K}:")
for multiplicando, multiplicador, resultado in tabla:
    print(f"{multiplicando} x {multiplicador} = {resultado}")