from typing import List
import numpy
from search_engine_core.db.models import Pages as DbPage


def find_similar_page(vector: List[float], pages: List[DbPage]) -> DbPage:
    similar_page = None
    shortest_distance = float('inf')

    for page in pages:
        distance = numpy.linalg.norm(vector - page.vector)

        if distance < shortest_distance:
            similar_page = page
            shortest_distance = distance

    return similar_page
