from api.models.web_page import WebPage
from app.queriers import SimpleQuerier
from api.translators import DbToApi

querier = SimpleQuerier()

def query(body):
    page_db = querier.get(body)
    db_to_api = DbToApi()
    page_api = db_to_api.page(page_db)
    return page_api
