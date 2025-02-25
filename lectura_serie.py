import serial, time

ard = serial.Serial("COM5", 9600)

def lectura_Serie():
    # Leer una línea del puerto serie
    linea = ard.readline().decode('utf-8').strip()  # Decodificar y limpiar espacios
    
    # Verificar si la línea sigue el formato esperado
    if linea.startswith("X,Y,Z:"):
        # Eliminar "X,Y,Z:" y dividir los valores
        valores = linea.replace("X,Y,Z:", "").split(",\t")
        
        # Convertir a enteros
        try:
            x, y, z = map(int, valores)
            # print(f"X: {x}, Y: {y}, Z: {z}")  # Mostrar los valores filtrados
            return x,y,z
        except ValueError:
            print("Error al convertir los valores")