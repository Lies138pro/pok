import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Récupération de la clé Supabase depuis les variables d'environnement
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Vérification si la clé est bien chargée
print(f"SUPABASE_KEY: {SUPABASE_KEY}")

# Construction de l'URL de connexion PostgreSQL
DATABASE_URL = f"postgresql://postgres:{SUPABASE_KEY}@db.xxxxxx.supabase.co:5432/postgres?sslmode=require"

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles SQLAlchemy
Base = declarative_base()