#pylint: disable=invalid-name
"""""Module permite utilizar la funcion sys para agregar archivo desde la linea de comandos"""""
import sys
import time

try:
    #Agregando archivos desde la línea de comandos
    file_names = sys.argv[1:]
    if not file_names:
        raise ValueError("Error: Debes agregar al menos un archivo.")
except ValueError as ve:
    print(ve)
    sys.exit(1)
print("\n** wordCount.py **")

start_time = time.time()
try:
    with open("WordCountResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write("Nombre de Archivo\tPalabra\tFrecuencia\n")
        for file_name in file_names:
            print(f"\nProcesando archivo: {file_name}")
            words_count = {}

            with open(file_name, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    words = line.strip().split()

                    for word in words:
                        words_count[word] = words_count.get(word, 0) + 1
            print("\nResultados:")
            for word, frequency in words_count.items():
                print(f"{word}: {frequency} veces")

            # Escribir resultados en WordCountResults.txt con título del archivo
            for word, frequency in words_count.items():
                result_file.write(f"{file_name}\t{word}\t{frequency}\n")

except FileNotFoundError:
    print("Error: Uno o más archivos no se encontraron.")
    sys.exit(1)
except ImportError as e:
    print(f"Error inesperado: {e}")
    sys.exit(1)
elapsed_time = (time.time() - start_time) * 1000
print(f"\nTiempo de procesamiento: {elapsed_time:.2f} milisegundos")# pylint: disable=missing-final-newline