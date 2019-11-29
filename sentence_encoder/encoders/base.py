from abc import abstractmethod
from typing import List


class Base:
    @abstractmethod
    def encode(self, sentences: List[str]) -> List[float]:
        pass
