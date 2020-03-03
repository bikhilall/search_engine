import logging
from typing import List
import numpy as np
from search_engine_core.db.models import Pages as DbPage


def find_similar_pages(vector: List[float], pages: List[DbPage]) -> List[DbPage]:
    similar_page = None
    shortest_distance = float('inf')

    Pages_distance = [
        {
            "page": page,
            "distance": np.linalg.norm(np.asarray(vector) - np.asarray(page.title_vector))
        } for page in pages
    ]

    sorted_pages = sorted(Pages_distance, key=lambda k: k['distance'])
    logging.info("Best search result"+str(sorted_pages[0]))
    return [p_d['page'] for p_d in sorted_pages[0:5]]
