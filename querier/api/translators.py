from typing import List
from api.models.web_page import WebPage as ApiPage
from search_engine_core.db.models import Pages as DbPage


class DbToApi:
    def pages(self, pages: List[DbPage]) -> List[ApiPage]:
        return [self.page(p) for p in pages]

    def page(self, page: DbPage) -> ApiPage:
        return ApiPage(
            url=page.url,
            title=page.title
        )
