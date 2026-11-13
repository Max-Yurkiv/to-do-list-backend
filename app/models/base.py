from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, Session



class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key = True, default= lambda: str(uuid4()))
