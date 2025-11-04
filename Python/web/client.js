// client.js

document.getElementById("spielerForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Seite soll nicht neu geladen werden

    // Formulardaten sammeln
    const spieler = {
        spieler: document.getElementById("spieler").value,
        jahrgang: parseInt(document.getElementById("jahrgang").value),
        staerke: parseInt(document.getElementById("staerke").value),
        torschuss: parseInt(document.getElementById("torschuss").value),
        motivation: parseInt(document.getElementById("motivation").value)
    };

    // Daten an den Server senden
    const response = await fetch("https://ominous-engine-r4p756wg5xjjh4vv-12345.app.github.dev/spieler", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(spieler)
    });

    // Antwort anzeigen
    const ergebnis = await response.json();
    document.getElementById("serverAntwort").textContent = JSON.stringify(ergebnis, null, 2);
});