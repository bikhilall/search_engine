from scrapy import Spider
from search_engine_core.db.models import models as db_models


def build_spider(spider: Spider, name: str, processor, domain: db_models.Domaines, ignore_urls: set = set()):
    """ build spider """
    spider.name = name
    spider.domain = domain
    spider.start_urls = [domain.url]
    spider.ignore_urls = ignore_urls

    def _processor(self, response, *kws, **kwargs):
        return processor(response, *kws, domain=self.domain, **kwargs)

    spider.processor = _processor

    return spider
