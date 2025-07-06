import math as m
import numpy as np
import pandas as pd


# =================== Cargar dataset ===================
dat_base = pd.read_csv("pokemon_data_mod.csv")

# =================== Creación de lista de tipos y movimientos ===================
# Crear un set vacío para guardar los movimientos únicos
movimientos_unicos = set()

# Iterar por las columnas de movimientos
for col in ['move_1', 'move_2', 'move_3', 'move_4', 'move_5']:
    # Agregar los valores no nulos de cada columna al set
    movimientos_unicos.update(dat_base[col].dropna().str.strip())

# Crear un set vacío para guardar los tipos únicos
tipos_unicos = set()

# Mostrar resultados de la list
#Movimientos
lista_movimientos_unicos = sorted(list(movimientos_unicos))
print(f'Total movimientos únicos: {len(lista_movimientos_unicos)}')
print(lista_movimientos_unicos)


### Sacar info de los movimientos de la API
#pip install requests
import requests
import time

# Tu lista de movimientos únicos (reemplaza con la tuya si ya la tienes)
#lista_movimientos_unicos_prueba = lista_movimientos_unicos[:5]

# Lista para guardar los datos
moves_data = []

for move in lista_movimientos_unicos:
    try:
        url = f"https://pokeapi.co/api/v2/move/{move.strip().lower()}/"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            move_info = {
                "name": data["name"],
                "power": data["power"],
                "accuracy": data["accuracy"],
                "pp": data["pp"],
                "priority": data["priority"],
                "type": data["type"]["name"],
                "damage_class": data["damage_class"]["name"]
            }
            moves_data.append(move_info)
        else:
            print(f"No encontrado: {move}")
    except Exception as e:
        print(f"Error con {move}: {e}")
    time.sleep(0.2)  # Para no saturar la API

# Convertir a DataFrame
df_moves = pd.DataFrame(moves_data)
print(df_moves.head())

#Guardamos la info obtenida de la api
df_moves.to_csv("movimientos_pokemon_info.csv", index=False)