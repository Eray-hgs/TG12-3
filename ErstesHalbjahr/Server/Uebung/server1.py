from flask import Flask, request, jsonify  
from flask_cors import CORS  
from pydantic import ValidationError  
from model1 import Person
import json

personen_Liste = []
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"Home"})


@app.route('/personen', methods=['POST'])
def handle_Person():
    """"Erstellt eine Person aus JSON-Daten und Prüft es mit Pydentic """
    try:
        data = request.get_json()
        person = Person(**data)
        personen_Liste.append(person)

        with open('personen.json', 'w', encoding="utf-8") as f:     
            json.dump([person.model_dump() for person in personen_Liste], f, ensure_ascii=False, indent=4)
        return jsonify({
            "status":"ok",
            "person": person.model_dump()
        }), 201
    
    except ValidationError as e:
        return jsonify({
            "Fehler bei der Validierung",
            e.errors()
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)