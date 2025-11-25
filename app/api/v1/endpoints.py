"""
🌐 DAX Training Project - API Endpoints

🎯 SYFTE:
Exponera DAX measures via REST API
Detta gör att vi kan testa DAX-logiken utan Power BI

🔄 ÅTERANVÄNDBAR: API-strukturen
🆕 UNIK: Endpoints är specifika för vårddomänen
"""

from fastapi import APIRouter
from app.services.data_loader import DataLoader
from app.services.dax_mesures import (
    total_minutes_all,
    total_minutes_all,
    total_minutes_per_client,
    total_minutes_per_unit,
    active_clients_count
)

router = APIRouter()
loader = DataLoader()

# ---------- RAW data endpoints ----------
@router.get("/raw/units")
def get_units():
    units, _, _ = loader.load_all()
    # returnera list of dataclasses -> FastAPI serialiserar dem som dicts
    return units

@router.get("/raw/clients")
def get_clients():
    _, clients, _ = loader.load_all()
    return clients

@router.get("/raw/visits")
def get_visits():
    _, _, visits = loader.load_all()
    return visits


# ---------- DAX-like measure endpoints ----------
@router.get("/measures/total_minutes")
def get_total_minutes():
    _, _, visits = loader.load_all()
    return {"total_minutes": total_minutes_all(visits)}

@router.get("/mesures/minutes_per_client")
def get_minutes_per_client():
    _, clients, visits = loader.load_all()
    return total_minutes_per_client(clients, visits)

@router.get("/mesures/minutes_per_unit")
def get_minutes_per_unit():
    units, clients, visits = loader.load_all()
    return total_minutes_per_unit(units, clients, visits)

@router.get("/measures/active_clients")
def get_active_clients():
    _, clients, _ = loader.load_all()
    return {"active_clients": active_clients_count(clients)}


