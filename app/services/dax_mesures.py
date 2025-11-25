from app.models.tables import Client, Unit, Visit
from typing import List, Dict

def total_minutes_all(visits: List[Visit]) -> int:
    """SUM(Visits[Minutes])"""
    return sum(v.minutes for v in visits)

def total_minutes_per_client(clients: List[Client], visits: List[Visit]) -> Dict[str, int]:
    """GROUPBY client -> SUM minutes"""
    result = {}
    for client in clients:
        result[client.name] = sum(v.minutes for v in visits if v.client_id == client.client_id)
    return result

def total_minutes_per_unit(units: List[Unit], clients: List[Client], visits: List[Visit]) -> Dict[str, int]:
    """GROUPBY unit -> SUM minutes for all clients in unit"""
    result = {}
    for unit in units:
        client_ids = [c.client_id for c in clients if c.unit_id == unit.unit_id]
        result[unit.unit_name] = sum(v.minutes for v in visits if v.client_id in client_ids)
    return result

def active_clients_count(clients: List[Client]) -> int:
    """COUNTROWS( FILTER(Clients, Clients[Active] = 'Yes') )"""
    return len([c for c in clients if c.is_active()])
