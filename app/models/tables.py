"""
📊 DAX Training Project - Data Models (Tabeller)

🎯 SYFTE:
Denna fil definierar de tre huvudtabellerna i vårt DAX-projekt:
- Units (Dimensionstabell)
- Clients (Dimensionstabell)
- Visits (Faktatabell)

🔄 ÅTERANVÄNDBAR DEL:
Strukturen med dataclasses och tabelldesign är samma i alla projekt.
Endast kolumnnamn och business-logik ändras.

🆕 UNIK DEL:
Kolumnnamnen (UnitName, Active, Minutes) är specifika för Vård & Omsorg.
"""

from dataclasses import dataclass
from datetime import date

@dataclass
class Unit:
    unit_id: int
    unit_name: str

@dataclass
class Client:
    client_id: int
    name: str
    unit_id: int
    active: str

    def is_active(self) -> bool:
        return str(self.active).lower() == "yes"

@dataclass
class Visit:
    visit_id: int
    client_id: int
    date: date
    minutes: int
