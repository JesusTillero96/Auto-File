import os
import shutil
from datetime import datetime
from modules.logger import log_action

# Extensiones organizadas por categoría
from modules.utils import load_config

config = load_config()

  
#Contador de archivos movidos
def organize_files(folder_path):
    files_moved = 0
#Recorremos todos los archivos
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
#Verificamos si es un archivo (no una carpeta)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)
            dest_folder = os.path.join(folder_path, category)

            os.makedirs(dest_folder, exist_ok=True)
            new_path = os.path.join(dest_folder, filename)

            shutil.move(file_path, new_path)
            files_moved += 1
            log_action(f"Movido: {filename} → {category}")

    return files_moved


def get_category(extension):
    for category, extensions in config.items():
        if extension.lower() in extensions:
            return category
    return "Otros"

