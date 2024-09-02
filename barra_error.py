import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = np.array([10, 12, 9, 11, 10, 13, 12, 14, 11, 10])

# Calcular la media
media = np.mean(datos)
print("Media:", media)

# Calcular la desviación estándar
desviacion_estandar = np.std(datos, ddof=1)
print("Desviación Estándar:", desviacion_estandar)

# Calcular el error estándar de la media (SEM)
sem = desviacion_estandar / np.sqrt(len(datos))
print("Error Estándar de la Media:", sem)

# Nivel de confianza (95%)
z = 1.96

# Calcular las barras de error
barras_de_error = z * sem
print("Barras de Error (95% de confianza):", barras_de_error)

# Visualización con Matplotlib
x = np.arange(1, len(datos) + 1)

# Crear una figura y un eje
fig, ax = plt.subplots()

# Graficar con barras de error
ax.errorbar(x, datos, yerr=barras_de_error, fmt='o', capsize=5)

# Mostrar la gráfica
plt.show()
