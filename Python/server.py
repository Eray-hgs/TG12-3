from flask import Flask, request, jsonify
from pydantic import BaseModel, Field, ValidationError
from model import Spieler 

spielerliste = []
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
        spieler = Spieler(**data)
        spielerliste.append(spieler)
        return jsonify({
            "status": "ok",
            "message": "Spieler erfolgreich erstellt",
            "spieler": spieler.model_dump()
        }), 201
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Validierung fehlgeschlagen",
            "details": e.errors()
        }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten



   
# Zum Starten des Servers: python server.py