import os

def print_files_in_directory(path):
    try:
        # Verificar si la ruta es un directorio válido
        if os.path.isdir(path):
            # Obtener la lista de archivos en el directorio
            files = os.listdir(path)
            if files:
                print("Archivos en la ruta '{}':".format(path))
                for file_name in files:
                    print(file_name)
            else:
                print("No hay archivos en la ruta '{}'.")
        else:
            print("La ruta '{}' no es un directorio válido.".format(path))
    except OSError as e:
        print("Error al acceder a la ruta '{}': {}".format(path, e))

if __name__ == "__main__":
    ruta = r"\\192.168.1.201\avisos al rfc"  # Ruta a la que deseas acceder
    print_files_in_directory(ruta)
