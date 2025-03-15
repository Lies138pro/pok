from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db, Pokemon
from models import Pokemon as PokemonModel

# Créer une instance de l'API
app = FastAPI()

# Modèle Pydantic pour les requêtes
class PokemonSchema(BaseModel):
    name: str
    type: str

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Pokémon !"}

# Endpoint pour ajouter un Pokémon
@app.post("/pokemons/")
def create_pokemon(pokemon: PokemonSchema, db: Session = Depends(get_db)):
    new_pokemon = PokemonModel(name=pokemon.name, type=pokemon.type)
    db.add(new_pokemon)
    db.commit()
    db.refresh(new_pokemon)
    return {"message": f"Pokémon {new_pokemon.name} ajouté avec succès !"}

# Endpoint pour lister tous les Pokémon
@app.get("/pokemons/")
def get_pokemons(db: Session = Depends(get_db)):
    pokemons = db.query(PokemonModel).all()
    return pokemons

# Endpoint pour filtrer les Pokémon par type
@app.get("/pokemons/{type}")
def get_pokemons_by_type(type: str, db: Session = Depends(get_db)):
    pokemons = db.query(PokemonModel).filter(PokemonModel.type == type).all()
    return pokemons

# Endpoint pour supprimer un Pokémon par son nom
@app.delete("/pokemons/{name}")
def delete_pokemon(name: str, db: Session = Depends(get_db)):
    pokemon = db.query(PokemonModel).filter(PokemonModel.name == name).first()
    if pokemon:
        db.delete(pokemon)
        db.commit()
        return {"message": f"Pokémon {name} supprimé avec succès !"}
    return {"error": "Pokémon non trouvé"}