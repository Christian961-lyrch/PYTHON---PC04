#Problema 03. El problema descarga una imagen de la página URl y, luego, lo comprime en un ZIP. Finalmente, lo desconprime

import requests # Importar respuesta
import zipfile  # Importar zipfile
import os       # Importar os
# el siguien cpodigo nos da la página dónde se descargrá la imagen
URL = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Nombre del archivo para la imagen
nombre_imagen = "imagen_descargada.jpg"

# Nombre del archivo zip
nombre_zip = "imagen_comprimida.zip"

# Descargar la imagen
try:
    response = requests.get(URL)
    response.raise_for_status()  # Realiza una excepción para códigos de estado HTTP no exitosos
    with open(nombre_imagen, 'wb') as file:
        file.write(response.content)
    print(f"La imagen obtenida del IURL ha sido descargada y guardada como {nombre_imagen}")
except requests.RequestException as e:
    print(f"No se ha descargado correctamente la imagen: {e}")

# Comprimir la imagen en un archivo ZIP
try:
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(nombre_imagen)
    print(f"La imagen ha sido comprimida en el archivo {nombre_zip}")
except Exception as e:
    print(f"Error al comprimir la imagen: {e}")