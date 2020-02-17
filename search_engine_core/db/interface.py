from typing import List
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DbInterface:
    def __init__(self, host: str = '0.0.0.0', user: str = 'root', key: str = 'password'):
        self._engine = create_engine('sqlite:///db.db')
        self._Session = sessionmaker(bind=self._engine)

    def _get_conn(self):
        conn = self._engine.connect()
        return conn

    @classmethod
    def conn(cls):
        if not hasattr(cls, '_conn'):
            cls._conn = cls._get_conn()

        return cls._conn

    def execute(self, queries: List) -> List:
        trans = self.conn.begin()
        results = []

        try:
            for query in queries:
                results.append(self.conn.execute(query))
            trans.commit()

        except Exception as e:
            trans.rollback()
            raise e

        return results

    def get_session(self) -> Session:
        return self._Session()

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.get_session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def merge(self, objs: List):
        with self.session_scope() as session:
            for obj in objs:
                session.merge(obj)

    def bulk_save_objects(self, objs: List):
        with self.session_scope() as session:
            session.bulk_save_objects(objs)

    def add(self, obj):
        with self.session_scope() as session:
            session.add(obj)
