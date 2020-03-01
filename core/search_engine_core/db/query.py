from .models.models import Pages, Domaines
from .interface import DbInterfaceSingleton


def query_pages(domain: Domaines):
    db_interface = DbInterfaceSingleton()
    with db_interface.session_scope() as session:
        data = session.query(
            Pages
        ).filter(
            Pages.domain_id == domain.id
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
