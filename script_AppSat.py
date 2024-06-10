import sys, os
import argparse
from funciones_AppSat import Clasificador_Archivos

def main(fecha_limite=None):
    # Ruta PDF's'
    root = r"\\192.168.1.201\avisos al rfc"
    # Carpeta PDF´s
    path = os.path.join(root, "avisos al rfc")

    # Path Raiz Proyecto
    path_raiz_proyecto = r'C:\Users\proyectosat\Documents\Aplicacion_SAT\dataframe'
    EJERCICIO = "2024"
    cliente = "LH"
    path_raiz_cliente = path_raiz_proyecto+"/"+cliente+"/"
    dir_excel = path_raiz_proyecto+"/Dataframes/"

    # rutas provicionales
    path_declaraciones = r"\\192.168.1.201\declaraciones\Presentadas en el ejercicio 2024"
    path_info_contribuyente = r"\\192.168.1.201\avisos al rfc\INFORMACION_CONTRIBUYENTE"

    rutas = [path_declaraciones, path_info_contribuyente]

    # Crear instancia de Clasificador_Archivos con fecha_limite como parámetro si se proporciona
    if fecha_limite:
        Archivos = Clasificador_Archivos(rutas, path_raiz_cliente, fecha_limite=fecha_limite)
    else:
        Archivos = Clasificador_Archivos(rutas, path_raiz_cliente)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Procesa archivos con una fecha límite.')
    parser.add_argument('--fecha_limite', help='Fecha límite en formato YYYY-MM-DD')
    args = parser.parse_args()

    main(args.fecha_limite)
