import random
from pyfiglet import Figlet

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()
    
    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()
    
    # Solicitar al usuario el nombre de una fuente
    fuente_seleccionada = input("Ingrese el nombre de una fuente (o presione Enter para usar una fuente aleatoria): ")
    
    # Si el usuario no ingresa una fuente, se selecciona una aleatoria
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)
    
    # Establecer la fuente seleccionada
    try:
        figlet.setFont(font=fuente_seleccionada)
    except ValueError:
        print(f"La fuente '{fuente_seleccionada}' no es válida. Se usará una fuente aleatoria.")
        figlet.setFont(font=random.choice(fuentes_disponibles))
    
    # Solicitar al usuario el texto a imprimir
    texto_imprimir = input("Ingrese el texto a convertir en arte ASCII: ")
    
    # Imprimir el texto en arte ASCII usando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()

