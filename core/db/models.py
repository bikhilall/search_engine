from sqlalchemy import Column, String, JSON, INT
from .base import Base

class Pages(Base):
    __tablename__ = 'pages'
    vector = Column(JSON())
    page_url = Column(String(50))
    language = Column(String(50))