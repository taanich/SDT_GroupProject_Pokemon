from fastapi import APIRouter
from app.services.graph_service import get_all_nodes, get_books
from app.services.pokeapi_service import get_pokemon

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Pokémon Multi-Model API is running!"}

@router.get("/nodes")
def read_nodes(limit: int = 10):
    return get_all_nodes(limit)

@router.get("/books")
def read_books():
    return get_books()

@router.get("/pokemon/{name}")
def read_pokemon(name: str):
    return get_pokemon(name)