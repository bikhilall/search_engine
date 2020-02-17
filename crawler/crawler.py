from datetime import datetime, timedelta
from typing import List

import pytz
import spiders
import parser
from scrapy.crawler import CrawlerProcess
from lib.encoder_api import encode
from search_engine_core import db
from search_engine_core.db import models as db_models


def page_processor(response):
    db_interface = db.DbInterface()
    page = parser.Page(response)
    page_vector = encode(page.content[:100])
    page_db = db_models.Pages(
        url=page.url,
        vector=page_vector
    )
    db_interface.merge(page_db)


def crawl(urls: List[str]):
    # build spiders
    Spider1 = spiders.build_spider(
        spider=spiders.Spider,
        name='spider_1',
        urls=urls,
        processor=page_processor
    )

    # Start the Crawler Process
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(Spider1)
    process.start()  # the script will block here until crawling is finished


if __name__ == '__main__':
    crawl(urls=['https://www.wikipedia.org'])
