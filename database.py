from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from supabase import create_client, Client

# Clés Supabase (remplace-les par les tiennes)
SUPABASE_URL = "https://xbwepivmoayrdiqvpvri.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhid2VwaXZtb2F5cmRpcXZwdnJpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIwMzM1MTgsImV4cCI6MjA1NzYwOTUxOH0.5FpccDGls_2vLE5d1WO5HqXLxmt3NtOwNOhAhAvXAuo"

# Connexion à Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Configuration de SQLAlchemy
DATABASE_URL = f"postgresql://postgres:{SUPABASE_KEY}@db.xxxxxx.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Modèle de la table Pokémon
class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False)

# Créer la table dans Supabase (si ce n'est pas déjà fait)
Base.metadata.create_all(bind=engine)