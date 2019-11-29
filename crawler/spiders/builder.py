from typing import List
from scrapy import Spider


def build_spider(spider: Spider, name: str, urls: List[str], processor):
    spider.name = name
    spider.start_urls = urls

    def _processor(self, *kws, **kwargs):
        return processor(*kws, **kwargs)

    spider.processor = _processor

    return spider
