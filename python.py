import csv

# Función para leer el archivo CSV y devolver los datos como lista de diccionarios
def leer_datos_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(dict(fila))
    return datos

# Función para imprimir la tabla de datos
def imprimir_tabla(datos):
    # Imprimir encabezados
    encabezados = datos[0].keys()
    encabezados_str = ' | '.join(encabezados)
    print(encabezados_str)
    print('-' * len(encabezados_str))

    # Imprimir datos
    for fila in datos:
        fila_str = ' | '.join(fila.values())
        print(fila_str)

if __name__ == '__main__':
    nombre_archivo = 'datos.csv'
    datos = leer_datos_csv(nombre_archivo)
    imprimir_tabla(datos)


