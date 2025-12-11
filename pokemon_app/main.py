from dotenv import load_dotenv
import os
from fastapi import FastAPI

# load env vars
load_dotenv()

app = FastAPI(
    title="Pokémon Multi-Model API",
    description="Service Layer for Neo4j + PokeAPI + (future Oracle Spatial)",
    version="1.0"
)

# Import router and include it
from pokemon_app.routes import router
app.include_router(router)