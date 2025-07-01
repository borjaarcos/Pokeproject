import pandas as pd

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


if '=' in str(dat_base["hp"].iloc[0]):
    dat_base["hp"] = dat_base["hp"].str.split('=').str[1].astype('int64')
if '=' in str(dat_base["attack"].iloc[0]):
    dat_base["attack"] = dat_base["attack"].str.split('=').str[1].astype('int64')
if '=' in str(dat_base["defense"].iloc[0]):
    dat_base["defense"] = dat_base["defense"].str.split('=').str[1].astype('int64')
if '=' in str(dat_base["special-attack"].iloc[0]):
    dat_base["special-attack"] = dat_base["special-attack"].str.split('=').str[1].astype('int64')
if '=' in str(dat_base["special-defense"].iloc[0]):
    dat_base["special-defense"] = dat_base["special-defense"].str.split('=').str[1].astype('int64')
if '=' in str(dat_base["speed"].iloc[0]):
    dat_base["speed"] = dat_base["speed"].str.split('=').str[1].astype('int64')

# Eliminar columnas separadas
cols_to_drop = ['types', 'moves', 'stats']
cols_presentes = [col for col in cols_to_drop if col in dat_base.columns]

if cols_presentes:
    dat_base = dat_base.drop(cols_presentes, axis=1)

# Quitar valores NA
dat_base = dat_base.fillna("")

# Guardar como CSV
dat_base.to_csv("pokemon_data_mod.csv", index=False)

db = pd.read_csv("pokemon_data.csv")
db.info()