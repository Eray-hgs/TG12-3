from flask import Flask, request, jsonify  
from flask_cors import CORS  
from pydantic import ValidationError  
from model2 import Auto  
import json  


app = Flask(__name__)
CORS(app)

auto_liste=[]

@app.route('/')
def home():
    return jsonify({"Home"})


@app.route('/auto', methods=['POST'])
def handle_Auto():
    """Erstellt ein neues Auto aus JSON-Daten und prüft es mit Pydantic."""
    try:
        data = request.get_json()
        auto = Auto(**data)
        auto_liste.append(auto)

        with open('autos.json', 'w', encoding="utf-8") as f:         #Öffnet die JSON-Datei zum Schreiben 'w' = write, encoding="utf-8" um Umlaute zu unterstützen, 'r' = read
            json.dump([auto.model_dump() for auto in auto_liste], f, ensure_ascii=False, indent=4) #Speichert die aktualisierte Spielerliste in einer JSON-Datei
        return jsonify({
            "Autos": auto.model_dump()
        }), 201
           
    except ValidationError as e:
        return jsonify({
           "Fehler":e.errors()
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)