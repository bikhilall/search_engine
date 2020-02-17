from .models.models import Base
from .interface import DbInterface


def create_all():
    db = DbInterface()
    Base.metadata.create_all(db._engine)
