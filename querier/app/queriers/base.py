from abc import abstractmethod
from search_engine_core.db.models import Pages as DbPage

class Querier:
    @abstractmethod
    def get(self, text: str) -> DbPage:
        pass
