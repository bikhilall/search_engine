from datetime import datetime
import pytz
from sqlalchemy import Column, String, JSON, Integer, DateTime, ForeignKey
from .base import Base


class Domaines(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100), unique=True)


class Pages(Base):
    __tablename__ = 'pages'
    url = Column(String(1000), primary_key=True)
    domain_id = Column(
        Integer,
        ForeignKey(Domaines.id, onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )

    language = Column(String(50))
    title_vector = Column(JSON(), nullable=False)
    content_vector = Column(JSON(), nullable=False)
    title = Column(String(100), nullable=False)
    update_datetime = Column(DateTime(timezone=True), default=datetime.now(tz=pytz.utc))
