import serial
import serial.tools
import serial.tools.list_ports

port_Descriptions = ["arduino", "usb", "ttyacm0", "uart", "cp210", "ch340", "silicon labs", "ftdi"] # Posibles descripciones del puerto

def buscar_Puerto():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port.description)
        description = port.description.lower()
        if description in port_Descriptions:
            print("PUERTO: " + port.device)
            return port.device
        
ard = serial.Serial(buscar_Puerto(), 9600)


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
            print(f"X: {x}, Y: {y}, Z: {z}")  # Mostrar los valores filtrados
            return x,y,z
        except ValueError:
            print("Error al convertir los valores")
            