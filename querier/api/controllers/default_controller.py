from api.models.web_page import WebPage
from app.queriers import SimpleQuerier
from api.translators import DbToApi

querier = SimpleQuerier()

def query(text):
    """
    query similar pages given a text
    :param text:
    :return: pages
    """
    pages_db = querier.get(text)
    db_to_api = DbToApi()
    pages_api = db_to_api.pages(pages_db)
    return pages_api
