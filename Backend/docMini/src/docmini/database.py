
# Retrieve DB_URL variable from .env (M1-- Note : M1 -> ALternative Method)
# DB_URL = os.getenv("DB_URL")
#
# Handle the case where we made mistake by writing dotenv variable
# if DB_URL is None:
#     raise ValueError("DB_URL is not defined in the environment")

# engine = create_engine(DB_URL) -- CREATE THE ENGINE

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

# Load .env variables
env_path = Path(__file__).resolve().parents[2] / ".env" # Relative where dotenv file is . 
load_dotenv(dotenv_path=env_path, override=True)

# Create the DB URL 
db_url = URL.create(
    drivername = os.getenv("DB_DRIVER"),
    username = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    port = int(os.getenv("DB_PORT")),
    database = os.getenv("DB_NAME")
)

# Create the engine
engine = create_engine(db_url)

# Create SessionLocal by using sessionmaker --<>
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False, 
    expire_on_commit= False # Attributes are available after commit () because ORM object are stored in session memory
)

db = SessionLocal()

# FastAPI dependance
def get_db():
    "Create a session. It will use later in api "
    
    db = SessionLocal()

    try :
        yield db

    finally:
        db.close()

# Open a connection just to test
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT version()"))

# print(result.scalar())

