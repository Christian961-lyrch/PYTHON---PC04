# Problema 05. 

import os

def guardar_tabla(n):
    """Guarda la tabla de multiplicar de n en un archivo."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla del {n} guardada en {nombre_archivo}.")
    except IOError:
        print("Hubo un problema al guardar la tabla.")

def leer_tabla(n):
    """Lee la tabla de multiplicar de n desde un archivo y la muestra por pantalla."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Contenido de {nombre_archivo}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except IOError:
        print("Hubo un problema al leer la tabla.")

def mostrar_linea_tabla(n, m):
    """Muestra la línea m de la tabla de multiplicar de n desde un archivo."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m} de {nombre_archivo}: {lineas[m-1]}")
            else:
                print(f"La línea {m} no está en el rango válido de la tabla.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except IOError:
        print("Hubo un problema al leer la tabla.")

def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Mostrar línea específica de una tabla")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            n = int(input("Ingrese un número entre 1 y 10 para generar su tabla de multiplicar: "))
            if 1 <= n <= 10:
                guardar_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        
        elif opcion == '2':
            n = int(input("Ingrese un número entre 1 y 10 para leer su tabla de multiplicar: "))
            if 1 <= n <= 10:
                leer_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        
        elif opcion == '3':
            n = int(input("Ingrese un número entre 1 y 10 para leer su tabla de multiplicar: "))
            m = int(input("Ingrese el número de la línea a mostrar: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea_tabla(n, m)
            else:
                print("Ambos números deben estar entre 1 y 10.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()