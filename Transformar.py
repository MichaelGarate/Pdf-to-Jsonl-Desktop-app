import os
import json
import threading
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
from PDF_TXT import extraer_texto
from TXT_JSON import crear_archivo_jsonl
from train_Json import entrenar_jsonl

archivo_txt = os.path.abspath('archivosTXT/PDF_text.txt')


def extraer_texto_con_mensaje(mensaje):
    # Extraer texto del archivo PDF
    extraer_texto()
    mensaje.config(text="Creando archivo JSON...")

    # Verificar si el archivo TXT existe
    if os.path.exists(archivo_txt):
        # Obtener la ruta seleccionada por el usuario
        ruta_seleccionada = filedialog.askdirectory()
        # Si se selecciona una ruta, crear el archivo JSONL en esa ruta
        if ruta_seleccionada:
            ruta_archivo_jsonl = os.path.join(os.path.normpath(ruta_seleccionada), 'archivo.jsonl')
            ruta_absoluta_jsonl = os.path.abspath(ruta_archivo_jsonl)
            crear_archivo_jsonl(archivo_txt, ruta_absoluta_jsonl)
            mensaje.config(text="¡Archivo JSONL creado en {}!".format(ruta_archivo_jsonl))
        else:
            mensaje.config(text="No se ha seleccionado ninguna carpeta")
    else:
        mensaje.config(text="No se encontró el archivo de texto TXT.")

def entrenar_json_con_mensaje(mensaje):
    # Solicitar el archivo JSONL al usuario
    mensaje.config(text="Selecciona un archivo JSONL...")
    ruta_jsonl = filedialog.askopenfilename(filetypes=[("JSONL files", "*.jsonl")])

    if ruta_jsonl:
        # Solicitar el archivo PDF al usuario
        mensaje.config(text="Selecciona un archivo PDF...")
        ruta_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if ruta_pdf:
            mensaje.config(text="Creando archivo JSONL...")

            nombre_archivo_jsonl = os.path.basename(ruta_jsonl)
            nombre_archivo_txt = os.path.splitext(os.path.basename(ruta_pdf))[0] + ".txt"

            # Extraer texto del archivo PDF
            extraer_texto(ruta_pdf, nombre_archivo_txt)

            # Obtener la ruta de salida para el archivo JSONL modificado
            ruta_salida_jsonl = filedialog.asksaveasfilename(filetypes=[("JSONL files", "*.jsonl")], defaultextension=".jsonl")

            # Entrenar el archivo JSONL con las preguntas y respuestas
            entrenar_jsonl(nombre_archivo_txt, ruta_jsonl, ruta_salida_jsonl)

            mensaje.config(text="¡Archivo JSONL modificado creado en {}!".format(ruta_salida_jsonl))
        else:
            mensaje.config(text="No se ha seleccionado ningún archivo PDF")
    else:
        mensaje.config(text="No se ha seleccionado ningún archivo JSONL")


def ventana_tkinter():  
    #Color de fondo
    color = '#DCDADA'
    #crear ventana  
    ventana = tk.Tk()
    ventana.configure(bg=color)

    #ventana no redimensionable
    ventana.resizable(False, False)

    #crear un Frame para los widgets de las imágenes
    frame_imagenes = tk.Frame(ventana)
    frame_imagenes.pack(side=tk.TOP, pady=40)

    #carga la primera imagen y redimensiona
    image1 = Image.open("img-pdf.png")
    new_image1 = image1.resize((100,100))
    tk_image1 = ImageTk.PhotoImage(new_image1)

    #mostrar la primera imagen en el Frame
    label1 = tk.Label(frame_imagenes, image=tk_image1)
    label1.pack(side=tk.LEFT, padx=20)  # Agregar padx=10 para el margen a la izquierda

    # carga la segunda imagen y redimensiona
    image2 = Image.open("img-flecha.png")
    new_image2 = image2.resize((100, 100))
    tk_image2 = ImageTk.PhotoImage(new_image2)

    # crea un widget Label para mostrar la segunda imagen en el Frame
    label2 = tk.Label(frame_imagenes, image=tk_image2)
    label2.pack(side=tk.LEFT, padx=20)  

    # carga la tercera imagen y redimensiona
    image3 = Image.open("img-json.png")
    new_image3 = image3.resize((100, 100))
    tk_image3 = ImageTk.PhotoImage(new_image3)

    # crea un widget Label para mostrar la tercera imagen en el Frame
    label3 = tk.Label(frame_imagenes, image=tk_image3)
    label3.pack(side=tk.LEFT, padx=20)  

    # crear un Frame para el botón
    frame_boton = tk.Frame(ventana, pady=0)
    frame_boton.pack(side=tk.TOP, pady=20)

    # Agregar botón "Extraer texto"
    botonExtraer = tk.Button(frame_boton, text="Archivo PDF", command=lambda: extraer_texto_con_mensaje(mensaje), width=10, height=2, padx=10, pady=0)
    botonExtraer.pack(side=tk.LEFT, padx=5, pady=10)
    
    # Agregar botón "Entrenar JSON"
    botonEntrenar = tk.Button(frame_boton, text="Entrenar JSON", command=lambda: entrenar_json_con_mensaje(mensaje), width=10, height=2, padx=10, pady=0)
    botonEntrenar.pack(side=tk.RIGHT, padx=5, pady=10)

    #Agregar mensaje
    frame_mensaje = tk.Frame(ventana)
    frame_mensaje.pack(side=tk.TOP, pady=10)
    mensaje = tk.Label(frame_mensaje, text="")
    mensaje.pack(pady=10)

    #Establecer el icono de la ventana
    ventana.iconbitmap('img-app.ico')

    ventana.title("Extractor de texto de PDF")

    #Centrar la ventana
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 450
    alto_ventana = 400
    x = int((ancho_pantalla - ancho_ventana) / 2)
    y = int((alto_pantalla - alto_ventana) / 2)
    
    ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

    #Background color
    frame_imagenes.configure(bg=color)
    label1.configure(bg=color)
    label2.configure(bg=color)
    label3.configure(bg=color)
    frame_boton.configure(bg=color)
    mensaje.configure(bg=color)
    frame_mensaje.configure(bg=color)
    #Iniciar la ventana
    ventana.mainloop()

# Iniciar la ventana de tkinter en un hilo separado (para crear archivo TXT)
thread = threading.Thread(target=ventana_tkinter)
thread.start()

