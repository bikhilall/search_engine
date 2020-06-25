from typing import List
from cachetools import cached, LRUCache, TTLCache

from search_engine_core import db
from search_engine_core.db.models import Pages as DbPages

from lib.encoder_api import encode
from lib.vector import find_similar_pages
from search_engine_core.db.models import Pages as DbPage
from .base import Querier


class SimpleQuerier(Querier):

    def get(self, text: str) -> List[DbPage]:
        """
        find similar pages to the given text using its vector.
        :param text:
        :return: list of pages
        """
        vector = encode(text=text)
        pages = self._query_all_pages()
        similar_pages = find_similar_pages(vector=vector, pages=pages)
        return similar_pages

    @cached(cache=TTLCache(maxsize=1024, ttl=600))
    def _query_all_pages(self):
        db_interface = db.DbInterfaceSingleton()
        with db_interface.session_scope() as session:
            all_pages = session.query(
                DbPages
            ).all()
            session.expunge_all()

        return all_pages
