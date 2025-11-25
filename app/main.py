import os
import requests
from routes import *
from dotenv import load_dotenv

BASE_URL = os.getenv("BASE_URL")

def main():
    print("\n🌐 Testing FastAPI Endpoints...\n")

    # Root
    r = requests.get(f"{BASE_URL}/")
    print("Root:", r.json())

    # Nodes
    r = requests.get(f"{BASE_URL}/nodes?limit=5")
    print("\nNodes:", r.json())

    # Books
    r = requests.get(f"{BASE_URL}/books")
    print("\nBooks:", r.json())

    # PokeAPI
    r = requests.get(f"{BASE_URL}/pokemon/pikachu")
    print("\nPikachu:", r.json())

if __name__ == "__main__":
    main()