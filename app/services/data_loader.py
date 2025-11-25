"""
📂 Data Loader - Läser CSV-filer

🎯 SYFTE:
Laddar data från CSV-filer istället för hårdkodad data

🔄 ÅTERANVÄNDBAR: CSV-läsning fungerar i alla projekt
🆕 UNIK: Filnamn och kolumnmappning är projektspecifika
"""
import csv
from pathlib import Path
from datetime import datetime
from app.models.tables import Unit, Client, Visit
from typing import List, Tuple

class DataLoader:
    def __init__(self, data_path: str = "app/data/raw"):
        self.data_path = Path(data_path)

    def _read_csv(self, filename: str):
        with open(self.data_path / filename, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def load_units(self) -> List[Unit]:
        rows = self._read_csv("units.csv")
        return [Unit(unit_id=int(r["UnitID"]), unit_name=r["UnitName"]) for r in rows]

    def load_clients(self) -> List[Client]:
        rows = self._read_csv("clients.csv")
        return [
            Client(
                client_id=int(r["ClientID"]),
                name=r["Name"],
                unit_id=int(r["UnitID"]),
                active=r["Active"]
            )
            for r in rows
        ]

    def load_visits(self) -> List[Visit]:
        rows = self._read_csv("visits.csv")
        return [
            Visit(
                visit_id=int(r["VisitID"]),
                client_id=int(r["ClientID"]),
                date=datetime.strptime(r["Date"], "%Y-%m-%d").date(),
                minutes=int(r["Minutes"])
            )
            for r in rows
        ]

    def load_all(self) -> Tuple[List[Unit], List[Client], List[Visit]]:
        return (self.load_units(), self.load_clients(), self.load_visits())
