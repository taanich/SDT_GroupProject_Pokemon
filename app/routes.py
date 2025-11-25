from fastapi import FastAPI
from services.graph_service import get_all_nodes, get_books
from services.pokeapi_service import get_pokemon

app = FastAPI(
    title="Pokémon Multi-Model API",
    description="Service Layer for Neo4j + PokeAPI + (future Oracle Spatial)",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Pokémon Multi-Model API is running!"}

@app.get("/nodes")
def read_nodes(limit: int = 10):
    return get_all_nodes(limit)

@app.get("/books")
def read_books():
    return get_books()

@app.get("/pokemon/{name}")
def read_pokemon(name: str):
    return get_pokemon(name)