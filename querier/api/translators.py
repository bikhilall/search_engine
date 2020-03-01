from api.models.web_page import WebPage as ApiPage
from search_engine_core.db.models import Pages as DbPage


class DbToApi:
    def page(self, page: DbPage) -> ApiPage:
        return ApiPage(
            url=page.url,
            title=page.title
        )
