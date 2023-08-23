import fitz
from unidecode import unidecode
import os
from tkinter import filedialog

def extraer_texto():
    # seleccionar archivo PDF
    nombrePDF = filedialog.askopenfilename(filetypes=[("Archivo PDF", "*.pdf")])

    # verificar si se seleccionó un archivo
    if nombrePDF:
        archivoPdf = fitz.open(nombrePDF)

        # Iterar las paginas del PDF y extraer el texto
        texto = ''  # almacenar el texto

        # pasar cada pag y extraer el texto
        numPags = archivoPdf.page_count

        for pag in range(numPags):
            pagPdf = archivoPdf[pag]  # Pagina actual
            page_text = pagPdf.get_text()  # Extraer el texto de la pagina
            texto += page_text

        archivoPdf.close()  # Cerrar el archivo PDF para liberar recursos

        # Transformar a minúsculas y reemplazar letras con acento
        texto = texto.lower()
        texto = unidecode(texto)

        # Guardar el texto en archivo TXT en la carpeta
        carpetaTxt = "archivosTXT"
        if not os.path.exists(carpetaTxt):
            os.makedirs(carpetaTxt)
        file_path = os.path.join(carpetaTxt, 'PDF_text.txt')
        with open(file_path, 'w') as file:
            file.write(texto)
    else:
        # En caso de no seleccionar un archivo PDF, mostrar un mensaje
        print("No se seleccionó ningún archivo PDF.")
