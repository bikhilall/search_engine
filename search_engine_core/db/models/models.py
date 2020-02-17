from sqlalchemy import Column, String, JSON, Integer, DateTime
from sqlalchemy.sql import func
from search_engine_core.db.models.base import Base


class Domaines(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100))


class Pages(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1000))
    language = Column(String(50))
    vector = Column(JSON())
    title = Column(String(100))
    update_datetime = Column(DateTime(timezone=True), default=func.now())
