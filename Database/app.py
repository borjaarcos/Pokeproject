from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from calcularDano import simular_dano, efectividad

app = Flask(__name__)
CORS(app)  # Permitir peticiones externas (como desde Spring Boot)

# Cargar los datos
dat_base = pd.read_csv("pokemon_data_mod.csv")

info_movimientos = pd.read_csv("movimientos_pokemon_info.csv")
img_pokemons = pd.read_csv("pokemons_img_url.csv")

#Metemos la url de los pokémons en la base de datos
dat_base['url'] = img_pokemons['img_url']


# Rellenar valores nulos para evitar problemas
dat_base = dat_base.fillna("")


# Definir tipos adecuados
tipos = {
    "name": "string",
    "abilities": "string",
    "primary_type": "string",
    "secondary_type": "string",
    "move_1": "string",
    "move_2": "string",
    "move_3": "string",
    "move_4": "string",
    "move_5": "string",
    "hp": "Int64",
    "attack": "Int64",
    "defense": "Int64",
    "special-attack": "Int64",
    "special-defense": "Int64",
    "speed": "Int64",
    "url": "string"
}
dat_base = dat_base.astype(tipos)

#dat_base.info()
#print("Cantidad de nulos por columna:")
#print(dat_base.isnull().sum())

# ---------------------- ENDPOINTS ---------------------- #
# Ruta para obtener el daño de un Pokémon
@app.route('/pokemons/calculateDamage', methods=['POST'])
def calcular_dano_pokemon():
    data = request.get_json()
    nombre = data.get("nombre")

    if not nombre:
        return jsonify({"error": "Nombre de Pokémon no proporcionado"}), 400

    # Buscar el Pokémon atacante
    pokemon_test = dat_base[dat_base["name"].str.lower() == nombre.lower()]
    if pokemon_test.empty:
        return jsonify({"error": f"Pokémon '{nombre}' no encontrado"}), 404

    pokemon_test = pokemon_test.iloc[0]

    # Calcular el daño estimado
    df_resultado = simular_dano(pokemon_test, dat_base, info_movimientos, efectividad)
    df_resultado = df_resultado.fillna("")

    tipos_resultado = {
    "pokemon_atacante": "string",
    "pokemon_defensor": "string",
    "nombre_mov": "string",
    "movimiento_tipo": "string",
    "clase_daño": "string",
    "tipos_defensor": "string",
    }
    df_resultado = df_resultado.astype(tipos_resultado)
    
    # Devolver resultados
    return jsonify(df_resultado.to_dict(orient="records"))

# Ruta para obtener todos los Pokémon
@app.route('/pokemons/getAllPokemons', methods=['GET'])
def get_pokemons():
    return jsonify(dat_base.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
