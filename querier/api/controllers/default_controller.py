from api.models.web_page import WebPage
from app.queriers import SimpleQuerier
from api.translators import DbToApi

querier = SimpleQuerier()

def query(text):
    page_db = querier.get(text)
    db_to_api = DbToApi()
    page_api = db_to_api.page(page_db)
    return page_api
