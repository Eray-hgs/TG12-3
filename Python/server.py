from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError
from model import Spieler 
import json
import os

dateiname = "spieler.json"

if os.path.exists(dateiname):
    with open(dateiname, "r", encoding="utf-8") as f:
        daten = json.load(f)
    spieler_liste = [Spieler(**s) for s in daten]
    print("📂 Geladene Spieler:")
    for s in spieler_liste:
        print(s)
else:
    print(f"⚠️ Datei '{dateiname}' wurde nicht gefunden.")
    print("Es wird eine leere Spielerliste erstellt.")
    spieler_liste = []


app = Flask(__name__)

# Route für die Hauptseite
@app.route('/')
def home():
    
    response_attributes = attribute()
    return jsonify({"attributes": response_attributes})


@app.route('/profil')
def impressum():
    return "<html><body><body><h1>Gym</h1><p>Lukas hat schwache Schultern.</p></body></html>"

# Route zum Empfangen von Nachrichten
@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")
    print(attribute())
    response_message = f"Echo: {message}"
    return jsonify({"response": response_message})

@app.route("/spieler", methods=["POST"])
def handle_spieler():
    """Erstellt einen Spieler aus JSON-Daten und prüft es mit Pydantic."""
    try:
        data = request.get_json()
        s = Spieler(**data)
        spieler_liste.append(s)

        with open("spieler.json", "w", encoding="utf-8") as f:
            json.dump([s.model_dump() for s in spieler_liste], f, ensure_ascii=False, indent=4)
        print("✅ Spieler wurden in 'spieler.json' gespeichert")

        return jsonify({
            "status": "ok",
            "message": "Spieler erfolgreich erstellt",
            "spieler": s.model_dump()
        }), 201
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Validierung fehlgeschlagen",
            "details": e.errors()
        }), 400

@app.route('/spielerdaten')
def Test_Ausgabe():
    daten = ""
    for s in spieler_liste:
        daten = (f"{daten} <br> {s}")
    print (daten)
    return (f"{daten}")

def attribute():
   return f"""
       methode: {request.method}
       args: {request.args}
       form: {request.form}
       data: {request.data}
       headers: {request.headers}
       cookies: {request.cookies}
       path: {request.path}
       url: {request.url}
       remote_addr: {request.remote_addr}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten
    

   
# Zum Starten des Servers: python server.py