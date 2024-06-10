
# Ruta del ejecutable

# comandos para generar .exe
# pip install pyinstaller    
# pyinstaller --onefile script_AppSat.py

import subprocess
import pandas as pd

def ejecutar_script(exe_path, fecha_limite=""):
    try:
        # Ejecutar el archivo .exe con el parámetro y capturar la salida
        result = subprocess.run([exe_path, '--fecha_limite', fecha_limite], capture_output=True, text=True)
        # Verificar si la ejecución fue exitosa
        if result.returncode == 0:
            # Si la ejecución fue exitosa, devolver un DataFrame con valor 1
            return pd.DataFrame({'Resultado': [1]})
        else:
            # Si hubo algún problema en la ejecución, devolver un DataFrame con valor 0
            return pd.DataFrame({'Resultado': [0]})
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la ejecución
        print("Error:", e)
        return pd.DataFrame({'Resultado': [0]})

# Ruta del ejecutable
exe_path = r'C:\Users\proyectosat\Documents\Aplicacion_SAT\dist\script_AppSat.exe'

# Parámetro fecha límite
fecha_limite = "2024-01-01"

# Llamar a la función para ejecutar el script y obtener el DataFrame resultante
resultado_df = ejecutar_script(exe_path, fecha_limite)
# resultado_df = ejecutar_script(exe_path)

# Imprimir el DataFrame resultante
print(resultado_df)
