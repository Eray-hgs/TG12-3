import requests
import json

URL = "http://localhost:12345/auto"

auto_liste = []
# 🚗 Beispiel-Daten
auto_daten = {
    "marke":str (input("Marke:")),
    "baujahr":int (input("Baujahr:")),
    "ps":int (input("PS:")),
}

response = requests.post(URL, json=auto_daten)
print(response.status_code)


if response.status_code == 201:
    print("👍",json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print("👎",json.dumps(response.json(), indent=4, ensure_ascii=False))