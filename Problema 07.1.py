import requests
import sqlite3

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?start=2023-01-01&end=2023-12-31"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except