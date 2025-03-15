from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Définir la base de données
DATABASE_URL = os.getenv("https://ogwvmdajomoojvatfusu.supabase.co")  # L'URL de la base de données Supabase
# Exemple : postgresql://postgres:password@db.xxxx.supabase.co:5432/postgres

# Créer un moteur de base de données
engine = create_engine(DATABASE_URL)

# Créer une instance de base pour les modèles
Base = declarative_base()

# Définir la classe Pokemon
class Pokemon(Base):
    __tablename__ = "pokemons"  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)

# Créer une session locale pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fonction pour initialiser la base de données
def init_db():
    # Crée toutes les tables si elles n'existent pas déjà
    Base.metadata.create_all(bind=engine)