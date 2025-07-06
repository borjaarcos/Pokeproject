from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permitir peticiones externas (como desde Spring Boot)

# Cargar los datos
dat_base = pd.read_csv("pokemon_data_mod.csv")

img_pokemons = pd.read_csv("pokemons_img_url.csv")

dat_base['url'] = img_pokemons['img_url']


# Rellenar valores nulos para evitar problemas
dat_base = dat_base.fillna("")

dat_base.info()

# Definir tipos adecuados (solo ejemplo, ajusta según tu CSV)
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

# Ruta para obtener todos los Pokémon
@app.route('/pokemons/getAllPokemons', methods=['GET'])
def get_pokemons():
    return jsonify(dat_base.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
