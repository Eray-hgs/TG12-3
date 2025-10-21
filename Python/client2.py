
import requests
import json

URL = "http://localhost:12345/spieler"

# 🚗 Beispiel-Daten
spieler_daten = {
    "name": str(input("Name:")),
    "jahrgang": int(input("Jahrgang:")),
    "staerke":  int(input("Stärke:")),
    "torschuss": int(input("Torschuss:")),
    "motivation": int(input("Motivation:")),
}

response = requests.post(URL, json=spieler_daten)
print("Statuscode:", response.status_code)


if response.status_code == 201:
    print("✅ Spieler erfolgreich erstellt:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print("❌ Fehler bei der Erstellung:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


