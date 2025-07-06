import pandas as pd

#tabla efectividad tipos
efectividad = {
    'normal':   {'rock': 0.5, 'ghost': 0.0, 'steel': 0.5},
    'fire':     {'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'ice': 2.0, 'bug': 2.0, 'rock': 0.5, 'dragon': 0.5, 'steel': 2.0},
    'water':    {'fire': 2.0, 'water': 0.5, 'grass': 0.5, 'ground': 2.0, 'rock': 2.0, 'dragon': 0.5},
    'electric': {'water': 2.0, 'electric': 0.5, 'grass': 0.5, 'ground': 0.0, 'flying': 2.0, 'dragon': 0.5},
    'grass':    {'fire': 0.5, 'water': 2.0, 'grass': 0.5, 'poison': 0.5, 'ground': 2.0, 'flying': 0.5, 'bug': 0.5, 'rock': 2.0, 'dragon': 0.5, 'steel': 0.5},
    'ice':      {'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'ice': 0.5, 'ground': 2.0, 'flying': 2.0, 'dragon': 2.0, 'steel': 0.5},
    'fighting': {'normal': 2.0, 'ice': 2.0, 'poison': 0.5, 'flying': 0.5, 'psychic': 0.5, 'bug': 0.5, 'rock': 2.0, 'ghost': 0.0, 'dark': 2.0, 'steel': 2.0, 'fairy': 0.5},
    'poison':   {'grass': 2.0, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'ghost': 0.5, 'steel': 0.0, 'fairy': 2.0},
    'ground':   {'fire': 2.0, 'electric': 2.0, 'grass': 0.5, 'poison': 2.0, 'flying': 0.0, 'bug': 0.5, 'rock': 2.0, 'steel': 2.0},
    'flying':   {'electric': 0.5, 'grass': 2.0, 'fighting': 2.0, 'bug': 2.0, 'rock': 0.5, 'steel': 0.5},
    'psychic':  {'fighting': 2.0, 'poison': 2.0, 'psychic': 0.5, 'dark': 0.0, 'steel': 0.5},
    'bug':      {'fire': 0.5, 'grass': 2.0, 'fighting': 0.5, 'poison': 0.5, 'flying': 0.5, 'psychic': 2.0, 'ghost': 0.5, 'dark': 2.0, 'steel': 0.5, 'fairy': 0.5},
    'rock':     {'fire': 2.0, 'ice': 2.0, 'fighting': 0.5, 'ground': 0.5, 'flying': 2.0, 'bug': 2.0, 'steel': 0.5},
    'ghost':    {'normal': 0.0, 'psychic': 2.0, 'ghost': 2.0, 'dark': 0.5},
    'dragon':   {'dragon': 2.0, 'steel': 0.5, 'fairy': 0.0},
    'dark':     {'fighting': 0.5, 'psychic': 2.0, 'ghost': 2.0, 'dark': 0.5, 'fairy': 0.5},
    'steel':    {'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'ice': 2.0, 'rock': 2.0, 'steel': 0.5, 'fairy': 2.0},
    'fairy':    {'fire': 0.5, 'fighting': 2.0, 'poison': 0.5, 'dragon': 2.0, 'dark': 2.0, 'steel': 0.5},
}

# Tabla de efectividad tipo vs tipo (ya la tienes definida como `efectividad`)
# Puedes pasarla como argumento a las funciones

def obtener_datos_movimientos(pokemon, info_movimientos):
    lista_moves = [pokemon[f"move_{i}"] for i in range(1, 6)]
    df_moves = pd.DataFrame()
    
    for mov in lista_moves:
        fila = info_movimientos[info_movimientos['name'] == mov]
        if not fila.empty:
            df_moves = pd.concat([df_moves, fila], ignore_index=True)
        else:
            print(f"Movimiento {mov} no encontrado en info_movimientos")
    
    df_moves = df_moves[df_moves["power"].notna()].reset_index(drop=True)
    return df_moves

def anadir_stab(df_moves, tipo_ataque):
    stab_values = []
    for _, row in df_moves.iterrows():
        mov_type = row["type"]
        stab = 1.5 if mov_type in tipo_ataque else 1.0
        stab_values.append(stab)
    df_moves["stab"] = stab_values
    return df_moves

def obtener_multiplicador(tipo_movimiento, tipos_defensor, efectividad):
    if tipo_movimiento is None or tipo_movimiento != tipo_movimiento:  # NaN
        return 1.0
    multiplicador = 1.0
    for tipo_def in tipos_defensor:
        if tipo_def is None or tipo_def != tipo_def:
            continue
        mult = efectividad.get(tipo_movimiento, {}).get(tipo_def, 1.0)
        multiplicador *= mult
    return multiplicador

def generar_tabla_efectos(pokemon_test, df_moves, dat_base, efectividad):
    filas = []
    for _, mov in df_moves.iterrows():
        tipo_mov = mov['type']
        nombre_mov = mov['name']
        stab = mov['stab']
        poder = mov['power']
        clase_daño = mov['damage_class']
        
        for _, poke in dat_base.iterrows():
            nombre_poke = poke['name']
            tipos_defensor = [poke['primary_type'], poke['secondary_type']]
            defensa = poke['defense']
            def_esp = poke['special-defense']
            mult = obtener_multiplicador(tipo_mov, tipos_defensor, efectividad)

            filas.append({
                "pokemon_defensor": nombre_poke,
                "nombre_mov": nombre_mov,
                "movimiento_tipo": tipo_mov,
                "stab": stab,
                "poder": poder,
                "clase_daño": clase_daño,
                "tipos_defensor": tipos_defensor,
                "def": defensa,
                "def_esp": def_esp,
                "multiplicador": mult
            })
    
    return pd.DataFrame(filas)

def calcular_dano_base(nivel, poder, ataque_atacante, defensa_defensor, multiplicador_total):
    return (((2 * nivel / 5 + 2) * poder * ataque_atacante / defensa_defensor) / 50 + 2) * multiplicador_total

def simular_dano(pokemon_test, dat_base, info_movimientos, efectividad, nivel=50):
    nombre_ataque = pokemon_test["name"]
    ataque = pokemon_test["attack"]
    ataque_esp = pokemon_test["special-attack"]
    tipo_ataque = [pokemon_test["primary_type"], pokemon_test["secondary_type"]]

    print(f"\n→ Calculando daño causado por {nombre_ataque}:\n")

    df_moves = obtener_datos_movimientos(pokemon_test, info_movimientos)
    df_moves = anadir_stab(df_moves, tipo_ataque)
    df_mult = generar_tabla_efectos(pokemon_test, df_moves, dat_base, efectividad)

    filas = []
    for _, poke in df_mult.iterrows():
        nombre_defensa = poke["pokemon_defensor"]
        poder = poke["poder"]
        clase_daño = poke["clase_daño"]
        defensa = poke["def"]
        defensa_esp = poke["def_esp"]
        mult = poke["multiplicador"]
        stab = poke["stab"]
        multiplicador_total = mult * stab

        if clase_daño == "physical":
            dano = calcular_dano_base(nivel, poder, ataque, defensa, multiplicador_total)
        else:
            dano = calcular_dano_base(nivel, poder, ataque_esp, defensa_esp, multiplicador_total)

        filas.append({
            "pokemon_atacante": nombre_ataque,
            "pokemon_defensor": nombre_defensa,
            "nombre_mov": poke["nombre_mov"],
            "movimiento_tipo": poke["movimiento_tipo"],
            "stab": stab,
            "poder": poder,
            "clase_daño": clase_daño,
            "tipos_defensor": poke["tipos_defensor"],
            "def": defensa,
            "def_esp": defensa_esp,
            "multiplicador": mult,
            "multiplicador_total": multiplicador_total,
            "daño_estimado": dano
        })
    print(f"\n→ Proceso finalizado\n")
    
    return pd.DataFrame(filas)