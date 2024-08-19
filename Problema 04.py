#Problema 04. LEE FICHEROS, CALCULA TEMPERATURAS PROMEDIOS, MÁXIMA Y MÍNINMA. FINALMENTE, ESCRIBE LOS RESULTADOS EN UN FICHERO RESUMEN_TEMPERATURAS.TXT
import csv
import requests

# URL del archivo dónde se obtendrá información de las temperaturas en formato CSV.

url = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202407/main/Modulo4/src/temperaturas.txt"


# Ahora se descarga del enlace "url" 

try:
    response = requests.get(url)
    response.raise_for_status()  # Realiza un levantamiento una excepción para respuestas con errores HTTP
    contenido = response.text
except requests.RequestException as e:
    print(f"Error al descargar el archivo: {e}")
    exit()

# Convertir el contenido descargado en una lista de líneas para procesarlo como CSV
lineas = contenido.splitlines()

# Inicializar variables
temperaturas = []

# Leer y procesar las líneas del archivo descargado
for linea in csv.reader(lineas):
    try:
        fecha, temp = linea
        temperaturas.append(float(temp))
    except ValueError:
        print(f"Error al procesar la línea: {linea}")

# Calcular estadísticas
if temperaturas:
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    temp_promedio = sum(temperaturas) / len(temperaturas)
else:
    print("No se encontraron datos de temperatura.")
    exit()

# Escribir los resultados en un nuevo archivo
archivo_salida = "resumen_temperaturas.txt"
try:
    with open(archivo_salida, 'w') as archivo:
        archivo.write(f"Temperatura máxima: {temp_max:.2f}°C\n")
        archivo.write(f"Temperatura mínima: {temp_min:.2f}°C\n")
        archivo.write(f"Temperatura promedio: {temp_promedio:.2f}°C\n")
    print(f"El resumen ha sido guardado en {archivo_salida}.")
except IOError:
    print(f"No se pudo escribir en el archivo {archivo_salida}.")