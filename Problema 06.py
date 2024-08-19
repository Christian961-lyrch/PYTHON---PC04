
#Problema 06. 

def contar_lineas_codigo(ruta_archivo):
    """Cuenta las líneas de código excluyendo comentarios y líneas en blanco."""
    try:
        # Verificar que el archivo tenga extensión .py
        if not ruta_archivo.endswith(".py"):
            print("El archivo no tiene extensión .py")
            return
        
        # Leer el archivo y contar las líneas de código
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        lineas_codigo = 0

        for linea in lineas:
            # Eliminar espacios en blanco al inicio y fin de la línea
            linea = linea.strip()

            # Ignorar líneas en blanco o comentarios
            if linea and not linea.startswith("#"):
                lineas_codigo += 1

        print(f"El archivo '{ruta_archivo}' tiene {lineas_codigo} líneas de código (excluyendo comentarios y líneas en blanco).")
    
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no se encontró.")
    except IOError:
        print(f"Hubo un problema al leer el archivo '{ruta_archivo}'.")

if __name__ == "__main__":
    # Solicitar la ruta del archivo al usuario
    ruta = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta)