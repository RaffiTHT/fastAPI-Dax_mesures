📌 README.md (Minimal + Pedagogisk)
# 📊 DAX Training Project (FastAPI + CSV)

Ett minimalt träningsprojekt för att förstå:

- Hur man bygger **dimension & faktatabeller**
- Hur man laddar data från **CSV**
- Hur man skapar DAX-liknande beräkningar i Python
- Hur data flödar genom **FastAPI → Services → Measures**

Perfekt som grund innan man bygger större projekt med SQL och Power BI.

---

# 📁 Projektstruktur


    my-dax-training/
    │
    ├── app/
    │   ├── main.py
    │   │
    │   ├── api/v1/endpoints.py
    │   │
    │   ├── models/tables.py
    │   │
    │   ├── services/
    │   │   ├── data_loader.py
    │   │   └── dax_measures.py
    │   │
    │   └── data/raw/
    │       ├── units.csv
    │       ├── clients.csv
    │       └── visits.csv
    │
    ├── requirements.txt
    └── README.med

---

# 🚀 Installation


pip install -r requirements.txt
uvicorn app.main:app --reload

---

# 📚 API Endpoints

## RAW-data (som en datamodell)
- `/v1/raw/clients`
- `/v1/raw/visits`

## DAX-liknande measures
- `/v1/measures/total_minutes`  
- `/v1/measures/minutes_per_client`  
- `/v1/measures/minutes_per_unit`  
- `/v1/measures/active_clients`

---

# 🧠 Vad du lär dig i detta projekt

## 1. Datamodell (Star Schema)
- Units (dimension)
- Clients (dimension)
- Visits (fakta)

## 2. DAX-liknande beräkningar
- SUM
- GROUPBY
- COUNTROWS
- Relationer (Clients → Units)

## 3. API-design
Hur endpoints hämtar data → kör measures → returnerar resultat.

---

# 🎯 Nästa steg
1. Lägg till fler KPI:er  
2. Koppla SQL istället för CSV  
3. Bygg frontend som läser API-datan  
4. Skapa dashboards i Power BI utifrån samma CSV  

---

Done.  
Nu har du ett *rent, minimalt och proffsigt träningsprojekt*.  


⭐ Vill du att jag nu:


lägger allt i en GitHub-klar zip-struktur?


skriver en tutorial steg för steg hur varje fil fungerar?


bygger en frontend som visar KPI:erna?


Säg bara till — vi fortsätter!