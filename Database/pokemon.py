# =================== Cargar librerías ===================
import math as m
import numpy as np
import pandas as pd
import os

# =================== Cargar dataset ===================
dat_base = pd.read_csv("pokemon_data.csv")
dat_base.info()

# =================== Separar tipos ===================
# Separar la columna 'types' en 'type_1' y 'type_2' directamente en la copia
dat_base[['primary_type', 'secondary_type']] = dat_base['types'].str.split(',', n=1, expand=True)

# Limpiar espacios
dat_base['primary_type'] = dat_base['primary_type'].str.strip()
dat_base['secondary_type'] = dat_base['secondary_type'].str.strip()


# =================== Separar Movimientos ===================
# Separar la columna 'moves' en 'move_1', 'move_2', 'move_3', 'move_4' y 'move_5'
dat_base[['move_1', 'move_2', 'move_3', 'move_4', 'move_5']] = dat_base['moves'].str.split(',', n=4, expand=True)

# Limpiar espacios
dat_base['move_1'] = dat_base['move_1'].str.strip()
dat_base['move_2'] = dat_base['move_2'].str.strip()
dat_base['move_3'] = dat_base['move_3'].str.strip()
dat_base['move_4'] = dat_base['move_4'].str.strip()
dat_base['move_5'] = dat_base['move_5'].str.strip()

# =================== Separar Stats ===================
# Separar la columna 'stats' en columnas específicas
dat_base[['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']] = dat_base['stats'].str.split(',', n=5, expand=True)

# Limpiar espacios en las columnas de stats
dat_base['hp'] = dat_base['hp'].str.strip()
dat_base['attack'] = dat_base['attack'].str.strip()
dat_base['defense'] = dat_base['defense'].str.strip()
dat_base['special-attack'] = dat_base['special-attack'].str.strip()
dat_base['special-defense'] = dat_base['special-defense'].str.strip()
dat_base['speed'] = dat_base['speed'].str.strip()

# =================== Creación de lista de tipos y movimientos ===================
# Crear un set vacío para guardar los movimientos únicos
movimientos_unicos = set()

# Iterar por las columnas de movimientos
for col in ['move_1', 'move_2', 'move_3', 'move_4', 'move_5']:
    # Agregar los valores no nulos de cada columna al set
    movimientos_unicos.update(dat_base[col].dropna().str.strip())

# Crear un set vacío para guardar los tipos únicos
tipos_unicos = set()

# Iterar por las columnas de tipos
for col in ['primary_type','secondary_type']:
    # Agregar los valores no nulos de cada columna al set
    tipos_unicos.update(dat_base[col].dropna().str.strip())

# Mostrar resultados de la list
#Movimientos
lista_movimientos_unicos = sorted(list(movimientos_unicos))

#Tipos
lista_tipos_unicos = sorted(list(tipos_unicos))

#Lista pokemons
lista_pokemons = dat_base['name']

# =================== Cargar info de los movimientos sacada de la API ===================
lista_movimientos = pd.read_csv("movimientos_pokemon_info.csv")
print(lista_movimientos)

dat_base.to_csv("pokemon_data_mod.csv", index=False)

