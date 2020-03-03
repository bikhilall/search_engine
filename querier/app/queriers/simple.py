from typing import List
from search_engine_core import db
from search_engine_core.db.models import Pages as DbPages

from lib.encoder_api import encode
from lib.vector import find_similar_pages
from search_engine_core.db.models import Pages as DbPage
from .base import Querier


class SimpleQuerier(Querier):

    def get(self, text: str) -> List[DbPage]:
        vector = encode(text=text)
        pages = self._query_all_pages()
        similar_pages = find_similar_pages(vector=vector, pages=pages)
        return similar_pages

    def _query_all_pages_cached(self):
        if not hasattr(self, '_db_pages_cache'):
            self._db_pages_cache = self._query_all_pages()
        return self._db_pages_cache

    def _query_all_pages(self):
        db_interface = db.DbInterfaceSingleton()
        with db_interface.session_scope() as session:
            all_pages = session.query(
                DbPages
            ).all()
            session.expunge_all()

        return all_pages
