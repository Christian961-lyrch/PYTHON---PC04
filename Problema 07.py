import requests
import sqlite3
from pymongo import MongoClient
from datetime import datetime

# Función para obtener datos del API de SUNAT
def obtener_tipo_cambio(start_date, end_date):
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    params = {
        'start_date': start_date,
        'end_date': end_date
    }
    response = requests.get(url, params=params)
    return response.json()

# Función para almacenar datos en SQLite
def almacenar_en_sqlite(datos, db_name='base.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT PRIMARY KEY,
        compra REAL,
        venta REAL
    )
    ''')

    # Insertar datos
    for item in datos:
        fecha = item['fecha']
        compra = item['compra']
        venta = item['venta']
        cursor.execute('''
        INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
        ''', (fecha, compra, venta))

    conn.commit()
    conn.close()

# Función para almacenar datos en MongoDB
def almacenar_en_mongodb(datos, db_name='base', collection_name='sunat_info'):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]

    # Insertar datos
    collection.insert_many(datos)

# Función para mostrar el contenido de la tabla en SQLite
def mostrar_contenido_sqlite(db_name='base.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()

def main():
    # Obtener datos del 2023
    datos_2023 = obtener_tipo_cambio('2023-01-01', '2023-12-31')

    # Asegurarse de que los datos están en el formato correcto
    datos_formateados = [
        {
            'fecha': item['fecha'],
            'compra': item['compra'],
            'venta': item['venta']
        }
        for item in datos_2023
    ]

    # Almacenar en SQLite
    almacenar_en_sqlite(datos_formateados)

    # Almacenar en MongoDB
    almacenar_en_mongodb(datos_formateados)

    # Mostrar contenido de la tabla en SQLite
    mostrar_contenido_sqlite()

if __name__ == '__main__':
    main()

#Requisitos Previos
#Instalar las dependencias: Asegúrate de tener las bibliotecas necesarias instaladas. Puedes hacerlo usando pip:

#bash
#Copiar código
#pip install requests pymongo
#Tener MongoDB en funcionamiento: Debes tener MongoDB instalado y ejecutándose en tu máquina local en el puerto por defecto (27017).