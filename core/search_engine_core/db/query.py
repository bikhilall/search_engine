from .models.models import Pages, Domaines
from .interface import DbInterfaceSingleton


def query_pages(domain: str):
    db_interface = DbInterfaceSingleton()
    with db_interface.session_scope() as session:
        data = session.query(
            Pages
        ).all()
        session.expunge_all()

    return data


def query_domains():
    db_interface = DbInterfaceSingleton()
    with db_interface.session_scope() as session:
        data = session.query(
            Domaines
        ).all()
        session.expunge_all()

    return data
