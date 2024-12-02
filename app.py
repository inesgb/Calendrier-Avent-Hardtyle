from flask import Flask, jsonify, request, send_from_directory
import json

app = Flask(__name__)

# Charger les musiques
def load_musics():
    with open("musics.json", "r") as file:
        return json.load(file)

# Sauvegarder les musiques
def save_musics(data):
    with open("musics.json", "w") as file:
        json.dump(data, file, indent=4)

# Route principale pour afficher index.html
@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

# Route pour servir les fichiers statiques (CSS et JS)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

# Route pour récupérer les musiques
@app.route("/musics", methods=["GET"])
def get_musics():
    return jsonify(load_musics())

# Route pour mettre à jour les musiques
@app.route("/musics", methods=["POST"])
def update_music():
    data = request.json
    musics = load_musics()
    musics[data["date"]] = {"url": data["url"]}
    save_musics(musics)
    return jsonify({"message": "Music updated successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
