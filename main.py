import json
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict

# -----------------------------------------------------------------------------------#

with open("cards.json", "r") as f:
    data = json.load(f)
    all_cards = data["cards"]


class Card(BaseModel):
    expansion: str
    deck: str
    territory: str | None
    name: str
    type: str
    details: str | None
    picture: str | None

    model_config = ConfigDict(from_attributes=True)


# -----------------------------------------------------------------------------------#
app = FastAPI(title="Gwent Cards API")


@app.get("/cards", response_model=List[Card], summary="Obtener todas las cartas")
def read_cards():
    """Recupera todas las cartas almacenadas en la base de datos."""
    return all_cards


@app.get("/cards/{deck_name}", response_model=List[Card], summary="Obtener cartas por mazo")
def read_cards_by_deck(deck_name: str):
    """Recupera todas las cartas para un mazo específico (ej: 'Nilfgaard', 'Monsters')."""
    cards = [card for card in all_cards if card["deck"].lower() == deck_name.lower()]
    if not cards:
        raise HTTPException(status_code=404, detail=f"No se encontraron cartas para el mazo '{deck_name}'")
    return cards


@app.get("/cards/search/{card_name}", response_model=Card, summary="Buscar carta por nombre")
def read_card_by_name(card_name: str):
    """Busca una carta por nombre exacto."""
    for card in all_cards:
        if card["name"].lower() == card_name.lower():
            return card
    raise HTTPException(status_code=404, detail=f"Carta '{card_name}' no encontrada")
