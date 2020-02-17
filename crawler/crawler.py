from typing import List

import spiders
import parser
from scrapy.crawler import CrawlerProcess
from lib.encoder_api import encode
from search_engine_core import db
from search_engine_core.db.models import models as db_models


def page_processor(response, domain, *kws, **kwargs):
    db_interface = db.DbInterface()
    page = parser.Page(response)
    page_vector = encode(page.content[:1000])
    page_db = db_models.Pages(
        domain_id=domain.id,
        url=page.url,
        title=page.title,
        vector=page_vector
    )
    db_interface.merge([page_db])


def crawl(domains: List[db_models.Domaines], ignore_urls: List[str] = []):
    # build spiders
    for domain in domains:
        Spider1 = spiders.build_spider(
            spider=spiders.Spider,
            name='spider_1',
            domain=domain,
            ignore_urls=[],
            processor=page_processor
        )

    # Start the Crawler Process
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(Spider1)
    process.start()  # the script will block here until crawling is finished


if __name__ == '__main__':
    from search_engine_core.db.build import create_all

    create_all()
    crawl(urls=['https://en.wikipedia.org/wiki/Main_Page'])
