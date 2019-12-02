from sqlalchemy import Column, String, JSON, Integer
from .base import Base

class Pages(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vector = Column(JSON())
    url = Column(String(50))
    language = Column(String(50))