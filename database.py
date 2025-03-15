import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Récupérer les variables d'environnement pour Supabase
SUPABASE_URL = os.getenv("https://ogwvmdajomoojvatfusu.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9nd3ZtZGFqb21vb2p2YXRmdXN1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MjAzMzA5NCwiZXhwIjoyMDU3NjA5MDk0fQ.tvF3XkMQMqpriP3_XcyRsB1Ep8hr95_R82sDl4D0BmQ")

# Vérifier si les variables d'environnement sont définies
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Les variables d'environnement SUPABASE_URL et SUPABASE_KEY doivent être définies.")

# Créer l'URL de connexion PostgreSQL avec les informations de Supabase
DATABASE_URL = f"postgresql://postgres:{SUPABASE_KEY}@{SUPABASE_URL.split('//')[1]}/postgres"

# Créer l'engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Créer la session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer une base de données de classe
Base = declarative_base()

# Fonction pour obtenir une session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()