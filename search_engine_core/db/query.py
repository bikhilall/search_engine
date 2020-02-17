from .models.models import Pages, Domaines
from .interface import DbInterface

db_interface = DbInterface()


def query_pages(domain: str):
    with db_interface.session_scope() as session:
        data = session.query(
            Pages
        ).all()
        session.expunge_all()

    return data


def query_domains():
    with db_interface.session_scope() as session:
        data = session.query(
            Domaines
        ).all()
        session.expunge_all()

    return data
