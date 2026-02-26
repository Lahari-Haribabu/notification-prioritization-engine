import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://npe:npe@localhost:5432/npe_db"
)