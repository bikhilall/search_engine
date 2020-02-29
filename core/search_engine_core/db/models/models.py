from sqlalchemy import Column, String, JSON, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from .base import Base


class Domaines(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100), unique=True)


class Pages(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    domain_id = Column(
        # ForeignKey(Domaines.id,onupdate="CASCADE",ondelete="CASCADE")
        Integer
    )
    url = Column(String(1000), nullable=False)
    language = Column(String(50))
    vector = Column(JSON(), nullable=False)
    title = Column(String(100), nullable=False)
    update_datetime = Column(DateTime(timezone=True), default=func.now())
