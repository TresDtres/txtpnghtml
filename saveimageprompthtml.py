import os
import shutil


def generate_table_row(png_file, txt_file):
    # Leer contenido del archivo de texto
    with open(txt_file, 'r') as txt_file_obj:
        content = txt_file_obj.read()

    # Obtener solo el nombre del archivo de texto sin la ruta completa
    txt_file_name = os.path.basename(txt_file)

    # Crear la fila de la tabla HTML con la imagen y el contenido del texto
    row = (
    f'\n'
    f'        <tr>\n'
    f'            <td><img src="{png_file}" alt="{txt_file_name}" style="max-height:200px; max-width:200px;"></td>\n'
    f'            <td style="background-color: #fffbe6; padding: 1px;" onclick="copyToClipboard(this)">\n'
    f'            <pre>{content}</pre></td>\n'
    f'        </tr>\n'
    f''
)


    return row


# Ruta de la carpeta que contiene los archivos (por defecto, el directorio actual)
folder = os.getcwd()

# Ruta del archivo "clipboard.min.js" en el directorio actual
clipboard_file_src = os.path.join(folder, 'clipboard.min.js')
# Ruta de destino del archivo "clipboard.min.js"
clipboard_file_dst = os.path.join(folder, 'archivo_resultante', 'clipboard.min.js')

# Copiar el archivo "clipboard.min.js" al directorio de destino

#shutil.copy(clipboard_file_src, clipboard_file_dst)

# Obtener todos los archivos en la carpeta
files = os.listdir(folder)

# Crear una lista para almacenar las filas de la tabla generadas
table_rows = []

# Recorrer todos los archivos en la carpeta
for file in files:
    if file.endswith('.png'):
        png_file = os.path.join(folder, file)
        txt_file = os.path.join(folder, file[:-4] + '.txt')

        # Verificar si existe el archivo de texto correspondiente al archivo PNG
        if os.path.isfile(txt_file):
            row = generate_table_row(png_file, txt_file)
            table_rows.append(row)

# Crear el archivo HTML resultante
with open('archivo_resultante.html', 'w') as html_file:
    # Escribir la estructura de la tabla HTML
    html_file.write('''
        <html>
        <head>
            <script src="clipboard.min.js"></script>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }
                img{
                    max-height: 200px;
                    max-width: 200px;
                }
                td:nth-child(2) {
                    background-color: #fffbe6;
                    padding: 10px;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 5px 10px;
                    border: none;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
                #disclaimer {
                    font-size: 12px;
                    color: #888;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
        <table>
    ''')

    # Escribir el contenido de la tabla en el archivo HTML
    html_file.write(''.join(table_rows))

    # Escribir el contenido adicional
    html_file.write('''
        </table>
        <div id="disclaimer">
            <p>Descargo de responsabilidad: Por favor, utilice esta información de manera responsable.</p>
        </div>
        <script>
            // Función para copiar el contenido del elemento al portapapeles
            function copyToClipboard(element) {
                var text = element.textContent || element.innerText;
                var tempInput = document.createElement('textarea');
                tempInput.value = text;
                document.body.appendChild(tempInput);
                tempInput.select();
                document.execCommand('copy');
                document.body.removeChild(tempInput);
                alert('Texto copiado al portapapeles');
            }
        </script>
        </body>
        </html>
    ''')

print("El archivo HTML resultante se ha generado correctamente.")
