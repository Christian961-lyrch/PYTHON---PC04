#Problema 09

import csv
import sys

def obtener_repeticiones_maximas(dna, str_sequence):
    """Devuelve la cantidad máxima de repeticiones consecutivas de `str_sequence` en `dna`."""
    max_repeticiones = 0
    length = len(str_sequence)
    i = 0

    while i < len(dna):
        count = 0
        while dna[i:i+length] == str_sequence:
            count += 1
            i += length
        if count > max_repeticiones:
            max_repeticiones = count
        i += 1

    return max_repeticiones

def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    
    # Archivos de entrada
    archivo_csv = sys.argv[1]
    archivo_txt = sys.argv[2]

    # Leer el archivo CSV
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        personas = []
        str_sequences = []
        
        # Leer la cabecera para STRs
        header = reader.fieldnames
        str_sequences = header[1:]  # Excluir la columna 'name'

        # Leer datos de las personas
        for row in reader:
            nombre = row['name']
            str_counts = {str_seq: int(row[str_seq]) for str_seq in str_sequences}
            personas.append({'name': nombre, 'str_counts': str_counts})

    # Leer la secuencia de ADN
    with open(archivo_txt) as file:
        dna = file.read().strip()

    # Obtener los recuentos de STR de la secuencia de ADN
    str_counts_dna = {str_seq: obtener_repeticiones_maximas(dna, str_seq) for str_seq in str_sequences}

    # Comparar con la base de datos
    for persona in personas:
        if persona['str_counts'] == str_counts_dna:
            print(persona['name'])
            return
    
    print("No match")

if __name__ == "__main__":
    main()