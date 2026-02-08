import json
import os
# Modulo que define las caracteristicas  de los archivos a ordenar
config_path = "config.json"

default_config = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Hojas de cálculo": [".xls", ".xlsx", ".csv"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Otros": []
}

def load_config():
    #Carga la configuración desde config.json o crea una por defecto si no existe.
    if not os.path.exists(config_path):
        save_config(default_config)
        return default_config

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(" - Error: config.json está dañado. Se usará la configuración por defecto.")
        return default_config


def save_config(config):
    #Guarda la configuración actual en config.json.
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4, ensure_ascii=False)
