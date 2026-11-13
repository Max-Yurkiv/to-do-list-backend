from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url)
SessionL = sessionmaker(bind=engine)


def get_db():
    db = SessionL()
    try:
        yield db
    finally:
        db.close()