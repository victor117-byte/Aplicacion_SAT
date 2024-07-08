
# Ruta del ejecutable

# comandos para generar .exe
# pip install pyinstaller    
# pyinstaller --onefile script_AppSat.py

import subprocess
import pandas as pd

def ejecutar_script(exe_path, fecha_limite=""):
    try:
        # Ejecutar el archivo .exe con el parámetro
        subprocess.run([exe_path, '--fecha_limite', fecha_limite], check=True)
        # Si la ejecución no arroja excepciones, significa que fue exitosa
        return pd.DataFrame({'Resultado': [True]})
    except subprocess.CalledProcessError as e:
        # Si la ejecución arroja una excepción, significa que hubo un error
        print("Error:", e)
        return pd.DataFrame({'Resultado': [False]})

# Ruta del ejecutable
exe_path = r'C:\Users\proyectosat\Documents\Aplicacion_SAT\dist\script_AppSat.exe'

# Parámetro fecha límite
fecha_limite = "2024-06-24"

# Llamar a la función para ejecutar el script y obtener el DataFrame resultante
resultado_df = ejecutar_script(exe_path, fecha_limite)
# resultado_df = ejecutar_script(exe_path)

# Imprimir el DataFrame resultante
print(resultado_df)