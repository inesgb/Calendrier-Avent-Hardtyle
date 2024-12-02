import os
import json
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# Exemple de route pour vérifier que le serveur fonctionne
@app.route("/")
def home():
    return "Le backend fonctionne !"

@app.route("/musics", methods=["GET"])
def get_musics():
    with open("musics.json", "r") as file:
        return jsonify(json.load(file))

if __name__ == "__main__":
    # Flask écoute sur le port défini par Render via la variable d'environnement `PORT`
    port = int(os.environ.get("PORT", 5000))  # 5000 est une valeur par défaut
    app.run(host="0.0.0.0", port=port, debug=True)
