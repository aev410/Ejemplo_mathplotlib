import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


from lectura_serie import lectura_Serie

# Datos iniciales para almacenar las coordenadas del joystick
x_datos = []
y_datos = []

LECTURA_MAX = 685

# Crear la figura y los ejes para la gráfica
fig, ax = plt.subplots()
scatter = ax.scatter([], [], label="Datos")  # Gráfico de dispersión
linea, = ax.plot([], [], 'r-', label="Regresión Lineal")  # Línea de regresión
ax.set_xlim(0, LECTURA_MAX)  # Establecer los límites del eje X
ax.set_ylim(0, LECTURA_MAX)  # Establecer los límites del eje Y
ax.set_xlabel("X")  # Etiqueta del eje X
ax.set_ylabel("Y")  # Etiqueta del eje Y
ax.legend()  # Mostrar la leyenda

# Función para actualizar la gráfica en tiempo real
def actualizar(frame):
    # Limitar el número de datos almacenados a 100
    if len(x_datos) > 100:
        x_datos.pop(0)
        y_datos.pop(0)
    
    # Añadir nuevos datos aleatorios dentro del rango del joystick
    x,y,z = lectura_Serie()
    x_datos.append(x)  # Sustituir con datos reales
    y_datos.append(y)  # Sustituir con datos reales
    
    # Actualizar la posición de los puntos en el gráfico
    scatter.set_offsets(np.column_stack((x_datos, y_datos)))
    
    # Calcular la regresión lineal usando np.poly1d
    if len(x_datos) > 1:
        coeficientes = np.polyfit(x_datos, y_datos, 1)  # Ajuste de grado 1 (lineal)
        polinomio = np.poly1d(coeficientes)  # Crear la función de la recta
        
        x_vals = np.array([min(x_datos), max(x_datos)])  # Valores extremos de X
        y_vals = polinomio(x_vals)  # Evaluar la función en esos puntos
        
        # Actualizar la línea de regresión en la gráfica
        linea.set_data(x_vals, y_vals)
    
    return scatter, linea

# Configurar la animación para actualizar la gráfica periódicamente
ani = animation.FuncAnimation(fig, actualizar, interval=100)
plt.show()  # Mostrar la gráfica
