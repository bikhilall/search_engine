from sqlalchemy import Column, String
from .base import Base

class Pages(Base):
    __tablename__ = 'pages'
    vector = None
    page_url = Column(String(50))
    language = Column(String(50))