import csv
import sqlite3
import requests

# Paso 1: Crear y poblar la base de datos SQLite con datos de tipo de cambio

def crear_y_poblar_db(db_name='base.db', start_date='2023-01-01', end_date='2023-12-31'):
    # Obtener datos del tipo de cambio
    def obtener_tipo_cambio(start_date, end_date):
        url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
        params = {'start_date': start_date, 'end_date': end_date}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Asegura que la solicitud fue exitosa
        return response.json()

    datos_2023 = obtener_tipo_cambio(start_date, end_date)
    
    # Crear y poblar la base de datos SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Crear tabla
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT PRIMARY KEY,
        compra REAL,
        venta REAL
    )
    ''')

    # Insertar datos
    for item in datos_2023:
        fecha = item['fecha']
        compra = item['compra']
        venta = item['venta']
        cursor.execute('''
        INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
        ''', (fecha, compra, venta))

    conn.commit()
    conn.close()

# Paso 2: Obtener el tipo de cambio desde SQLite
def obtener_tipo_cambio(fecha, db_name='base.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('SELECT compra FROM sunat_info WHERE fecha = ?', (fecha,))
    resultado = cursor.fetchone()
    
    conn.close()
    
    if resultado:
        return resultado[0]
    else:
        raise ValueError(f"No hay tipo de cambio para la fecha: {fecha}")

# Paso 3: Procesar el archivo CSV y calcular los totales
def procesar_ventas(csv_file, db_name='base.db'):
    ventas_totales = {}

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        
        for fila in reader:
            producto = fila['producto']
            cantidad = int(fila['cantidad'])
            precio_dolares = float(fila['precio_dolares'])
            fecha_compra = fila['fecha_compra']
            
            # Obtener tipo de cambio
            tipo_cambio = obtener_tipo_cambio(fecha_compra, db_name)
            
            # Calcular precios
            precio_total_dolares = precio_dolares * cantidad
            precio_total_soles = precio_total_dolares * tipo_cambio
            
            if producto not in ventas_totales:
                ventas_totales[producto] = {'total_dolares': 0, 'total_soles': 0}
            
            ventas_totales[producto]['total_dolares'] += precio_total_dolares
            ventas_totales[producto]['total_soles'] += precio_total_soles
    
    return ventas_totales

# Paso 4: Mostrar los resultados
def mostrar_resultados(ventas_totales):
    for producto, totales in ventas_totales.items():
        print(f"Producto: {producto}")
        print(f"  Total en Dólares: {totales['total_dolares']:.2f}")
        print(f"  Total en Soles: {totales['total_soles']:.2f}")
        print()

def main():
    csv_file = 'ventas.csv'
    db_name = 'base.db'
    
    # Crear y poblar la base de datos SQLite
    crear_y_poblar_db(db_name)
    
    # Procesar las ventas
    ventas_totales = procesar_ventas(csv_file, db_name)
    
    # Mostrar los resultados
    mostrar_resultados(ventas_totales)

if __name__ == '__main__':
    main()