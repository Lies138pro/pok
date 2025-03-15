from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Pokemon
from pydantic import BaseModel
from supabase import create_client

app = FastAPI()

# Dépendance pour la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modèle Pydantic
class PokemonSchema(BaseModel):
    name: str
    type: str

# Route d'accueil
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Pokémon avec Supabase !"}

# Ajouter un Pokémon
@app.post("/pokemons/")
def create_pokemon(pokemon: PokemonSchema, db: Session = Depends(get_db)):
    new_pokemon = Pokemon(name=pokemon.name, type=pokemon.type)
    db.add(new_pokemon)
    db.commit()
    db.refresh(new_pokemon)
    return {"message": f"Pokémon {new_pokemon.name} ajouté avec succès !"}

# Lister tous les Pokémon
@app.get("/pokemons/")
def get_pokemons(db: Session = Depends(get_db)):
    pokemons = db.query(Pokemon).all()
    return pokemons

# Filtrer par type
@app.get("/pokemons/{type}")
def get_pokemons_by_type(type: str, db: Session = Depends(get_db)):
    pokemons = db.query(Pokemon).filter(Pokemon.type == type).all()
    return pokemons

# Supprimer un Pokémon
@app.delete("/pokemons/{name}")
def delete_pokemon(name: str, db: Session = Depends(get_db)):
    pokemon = db.query(Pokemon).filter(Pokemon.name == name).first()
    if pokemon:
        db.delete(pokemon)
        db.commit()
        return {"message": f"Pokémon {name} supprimé avec succès !"}
    return {"error": "Pokémon non trouvé"}