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



# Función para generar el archivo index.html
def generar_index_html(nombre_archivo):
    # Leer los datos del archivo CSV
    datos = leer_datos_csv(nombre_archivo)

    # Crear el contenido del archivo index.html
    contenido_html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabla de Datos</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Tabla de Datos</h1>
        <table>
            <thead>
                <tr>
                    {''.join(f'<th>{header}</th>' for header in datos[0].keys())}
                </tr>
            </thead>
            <tbody>
                {''.join(f'<tr>{"".join(f"<td>{value}</td>" for value in row.values())}</tr>' for row in datos)}
            </tbody>
        </table>
    </body>
    </html>
    '''

    # Escribir el contenido en el archivo index.html
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(contenido_html)

if __name__ == '__main__':
    nombre_archivo = 'datos.csv'
    generar_index_html(nombre_archivo)
