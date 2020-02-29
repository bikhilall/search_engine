from .models.models import Base
from .interface import DbInterfaceSingleton


def create_all():
    db = DbInterfaceSingleton()
    Base.metadata.create_all(db._engine)
