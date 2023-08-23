import os
import sys
from cx_Freeze import setup, Executable

#archivos necesarios para funcionar
files = ['.env','img-flecha.png','img-pdf.png','img-json.png','img-app.ico','TXT_JSON.py','PDF_TXT.py']

#archivo py que ejecuta la app
exe = Executable(
    script='Transformar.py',
      base='Win32GUI',
      icon='img-app.ico'
      )

setup(
name = 'Transforma Pdf a Json',
version = '1.0',
description='Programa para crear archivos Jsonl a partir de un archivo PDF',
author = 'Michael Garate',
options ={'build_exe':{'include_files': files}},
executables = [exe]
)
