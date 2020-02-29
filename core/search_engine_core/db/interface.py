from typing import List
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class DbInterface:
    def __init__(self, driver: str = 'mysql+pymysql', host: str = 'mysql', schema: str = 'search_engine',
                 user: str = 'user', password: str = 'password', port: int = 3306, local: bool = False):
        if local:
            url = 'sqlite:///db.db'
        else:
            url = f'{driver}://{user}:{password}@{host}:{port}/{schema}'

        self._engine = create_engine(url)
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
    def session_scope(self) -> Session:
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


class DbInterfaceSingleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        """ __new__ is Always a class method. """
        if not cls.instance:
            cls.instance = DbInterface(*args, **kwargs)
        return cls.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
