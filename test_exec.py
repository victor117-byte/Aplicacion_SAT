import subprocess

# Ruta del ejecutable

# comandos para generar .exe
# pip install pyinstaller    
# pyinstaller --onefile script_AppSat.py

exe_path = r'C:\Users\proyectosat\Documents\Aplicacion_SAT\dist\script_AppSat.exe'

# Parámetro fecha límite
fecha_limite = "2024-01-01"

# Ejecutar el archivo .exe con el parámetro
subprocess.run([exe_path, '--fecha_limite', fecha_limite])
