#pylint: disable=invalid-name
"""""Module permite utilizar la funcion sys para agregar archivo desde la linea de comandos"""""
import sys
import time

try:
    # Agregando archivos desde la línea de comandos
    file_names = sys.argv[1:]

    if not file_names:
        raise ValueError("Error: Debes agregar almenos archivo.")

    with open("StatisticsResults.txt", "w",  encoding="utf8") as result_file:
        result_file.write("File Name\tcount\tMean\tMedian\tMode\tStandard Deviation\tVariance\tProcessing Time (ms)\n") # pylint: disable=line-too-long

        for file_name in file_names:
            print(f"\nProcesando archivo: {file_name}")

            start_time = time.time()
            try:
                with open(file_name, "r",  encoding="utf8") as f:
                    numeros = []
                    for line_number, line in enumerate(f, start=1):
                        line = line.strip()
                        try:
                            numero = round(float(line), 2)
                            numeros.append(numero)
                        except ValueError:
                            print(f"Error en la línea {line_number}: '{line}'"
                                  f"no es un número válido. Se omitirá.")
                count = len(numeros)
                total = sum(numeros)
                mean = total / len(numeros)
                numeros_ordenados = sorted(numeros)

                n = len(numeros_ordenados)
                if n % 2 == 0:
                    mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
                else:
                    mediana = numeros_ordenados[n // 2]

                frecuencias = {}
                for num in numeros:
                    frecuencias[num] = frecuencias.get(num, 0) + 1
                moda = max(frecuencias, key=frecuencias.get)

                media = sum(numeros) / len(numeros)

                suma_cuadrados_diff = sum((x - media) ** 2 for x in numeros)
                desviacion_estandar = (suma_cuadrados_diff / len(numeros)) ** 0.5

                varianza = suma_cuadrados_diff / len(numeros)

                elapsed_time = (time.time() - start_time) * 1000

                print(f"Resultados para {file_name}:")
                print(f"Count: {count},"
                      f"Mean: {mean:.2f},"
                        f"Median: {mediana:.2f},"
                        f"Mode: {moda:.2f},"
                        f"Standard Deviation: {desviacion_estandar:.2f},"
                        f"Variance: {varianza:.2f}")
                print(f"Tiempo de procesamiento: {elapsed_time:.2f} milisegundos")

                result_file.write(f"{file_name}\t"
                                  f"{count}\t"
                                  f"{mean:.2f}\t"
                                  f"{mediana:.2f}\t"
                                  f"{moda:.2f}\t"
                                  f"{desviacion_estandar:.2f}\t"
                                  f"{varianza:.2f}\t"
                                  f"{elapsed_time:.2f}\n")
                print("Resultados escritos en StatisticsResults.txt")

            except FileNotFoundError:
                print(f"Error: No se pudo encontrar el archivo '{file_name}'."
                      f" Continuando con el siguiente archivo.")
            except ValueError as ve:
                print(f"Error: {ve}. Continuando con el siguiente archivo.")
            except ImportError as e:
                print(f"Error inesperado: {e}. Continuando con el siguiente archivo.")

except ValueError as ve:
    print(ve)
    sys.exit(1) # pylint: disable=missing-final-newline