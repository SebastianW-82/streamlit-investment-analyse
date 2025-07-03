
# EET Datenanalyse-App

Diese Streamlit-App ermöglicht eine grafische und statistische Analyse von EET-Daten anhand einer ISIN.

## 🔍 Funktionsumfang

- Upload einer Excel-Datei mit den Spalten:
  - `ISIN`
  - `Vorvertragliche nachhaltige Mindestinvestitionen (in %)`
  - `Tatsächliche nachhaltige Mindestinvestitionen (in %)`
  - `CO2 Ausstoß (in MT)`
- Eingabe einer ISIN zur Analyse
- Darstellung der Werte in:
  - Histogramm
  - Boxplot
- Statistische Kennzahlen:
  - Mittelwert
  - Median
  - Prozentualer Vergleich zum Rest der Werte

## ▶️ Verwendung

1. Lade die Datei `EET_Beispieldaten.xlsx` hoch (oder verwende eigene Daten im gleichen Format).
2. Gib eine ISIN aus der Tabelle ein.
3. Die App analysiert alle drei Kennzahlen und stellt sie grafisch dar.

## 📂 Dateien

- `app.py` – Streamlit-App
- `requirements.txt` – Python-Abhängigkeiten
- `EET_Beispieldaten.xlsx` – Beispieldatensatz

## 🚀 Deployment auf Streamlit Cloud

1. Repository auf GitHub erstellen
2. Diese drei Dateien hochladen
3. Bei [Streamlit Cloud](https://streamlit.io/cloud) anmelden
4. Neues Projekt erstellen und `app.py` als Startdatei wählen

