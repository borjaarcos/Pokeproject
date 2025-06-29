from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permitir peticiones externas (como desde Spring Boot)

# Cargar los datos
dat_base = pd.read_csv("pokemon_data.csv")

# Ruta para obtener todos los Pokémon
@app.route('/pokemons/getAllPokemons', methods=['GET'])
def get_pokemons():
    return jsonify(dat_base.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
