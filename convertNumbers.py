#pylint: disable=invalid-name
"""""Module permite utilizar la funcion sys para agregar archivo desde la terminarl"""""
import sys
import time

try:
    # Jalando archivos desde la línea de comando
    file_names = sys.argv[1:]
    if len(file_names) < 1:
        raise IndexError("Error: Agrega al menos un archivo para procesar.")
except IndexError as ie:
    print(ie)
    sys.exit(1)

print("\n** convertNumbers.py **")

start_time = time.time()

try:
    with open("ConvertionResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write("Nombre de archivo\tDecimal\tBinario\tHexadecimal\n")
        for file_name in file_names:
            print(f"\nProcesando archivo: {file_name}")

            numbers = []
            invalid_lines = []

            # Convertir los números a binarios y hexadecimal
            with open(file_name, "r",encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()
                    try:
                        number = int(line)
                        binary = bin(number)[2:]
                        hexadecimal = hex(number)[2:]
                        numbers.append((number, binary, hexadecimal))
                    except ValueError:
                        invalid_lines.append(line_number)
                        print(f"Error en línea {line_number}: '{line}'"
                              f"es un número no válido. Omitir.")
            if invalid_lines:
                print("\nSe encontró información inválida en el archivo.Omitir las siguientes líneas:") #pylint: disable=line-too-long
                for line_number in invalid_lines:
                    print(f"Línea {line_number}")
            print("\nResultados:")
            for number, binary, hexadecimal in numbers:
                print(f"Decimal: {number}, Binario: {binary}, Hexadecimal: {hexadecimal}")
            result_file.write(f"{file_name}\t")
            for number, binary, hexadecimal in numbers:
                result_file.write(f"{number}\t{binary}\t{hexadecimal}\n")

except FileNotFoundError:
    print(f"Error: Uno o más {file} no se encontraron.")
except ImportError as e:
    print(f"Error inesperado: {e}")

# Calcular tiempo de procesamiento en milisegundos
elapsed_time = (time.time() - start_time) * 1000
print(f"\nTiempo de procesamiento: {elapsed_time:.2f} milisegundos") #pylint: disable=missing-final-newline