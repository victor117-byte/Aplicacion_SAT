import pandas as pd
import numpy as np


user = "juan"
passw = "juan"

if user == "martin" and passw == "martin":

    # DataFrame con datos aleatorios
    data = {'Nombre': ['Juan', 'María', 'Pedro', 'Luis', 'Ana'],
        'Edad': [10, 3, 5, 240, 245],
        'Puntuación': [70, 30, 65, 15, 195]}
    df1 = pd.DataFrame(data)
    print("DataFrame 1:")
    df1
    
else:
    
    # DataFrame con datos predefinidos
    data = {'Nombre': ['Juan', 'María', 'Pedro', 'Luis', 'Ana'],
        'Edad': [25, 30, 35, 40, 45],
        'Puntuación': [80, 90, 75, 85, 95]}
    df1 = pd.DataFrame(data)
    print("DataFrame 2:")
    df1