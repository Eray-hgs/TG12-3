import requests
import json

URL = "http://localhost:12345/personen"

personen_Liste = []
# 🚗 Beispiel-Daten
personen_daten = {
    "name" : str (input("Name:")),
    "alter": int (input("Alter:")),

}

response = requests.post(URL, json=personen_daten)
print(response.status_code)


if response.status_code == 201:
    print("👍",json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print("👎",json.dumps(response.json(), indent=4, ensure_ascii=False))