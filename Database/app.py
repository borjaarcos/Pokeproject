from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permitir peticiones externas (como desde Spring Boot)

# Cargar los datos
dat_base = pd.read_csv("pokemon_data_mod.csv")
dat_base = dat_base.astype({
    "name": "string",
    "types": "string",
    "abilities": "string",
    "moves": "string",
    "stats": "string",
    "primary_type": "string",
    "secondary_type": "string",
    "move_1": "string",
    "move_2": "string",
    "move_3": "string",
    "move_4": "string",
    "move_5": "string",
    "hp": "string",
    "attack": "string",
    "defense": "string",
    "special-attack": "string",
    "special-defense": "string",
    "speed": "string"
})

# Ruta para obtener todos los Pokémon
@app.route('/pokemons/getAllPokemons', methods=['GET'])
def get_pokemons():
    return jsonify(dat_base.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
