import os
from modules.file_manager import organize_files
from modules.logger import log_action

#pide ingresar la ruta de la carpeta de los archivoz a organizar
def main():
    print("===  Automatizador de Archivos Inteligente ===")
    target_folder = input(" Ingresá la ruta de la carpeta a organizar: ").strip()
# Comprobacion de la existencia de la ruta
    if not os.path.exists(target_folder):
        print(" X Error: La carpeta no existe.")
        return
# Llama la funcion "organize_file" y guarda registro de los archivos movidos"
#Muestra mensaje por pantalla de los archivos movidos
    files_moved = organize_files(target_folder)
    log_action(f"Organización completada. {files_moved} archivos movidos.")
    print(f" O
