from typing import List
from datetime import datetime, timedelta

import pytz
import spiders
import parser
from scrapy.crawler import CrawlerProcess
from lib.encoder_api import encode
from search_engine_core import db
from search_engine_core.db.models import models as db_models


def page_processor(response, domain, *kws, **kwargs):
    db_interface = db.DbInterfaceSingleton()
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
    active_spiders = []
    for domain in domains:
        visited_pages = db.query.query_pages(domain)
        ignore_urls = [
            page.url
            for page in visited_pages
            # if page.update_datetime < datetime.now(tz=pytz.utc) - timedelta(days=2)
        ]
        active_spiders.append(
            spiders.build_spider(
                spider=spiders.Spider,
                name=f'spider_{domain.id}',
                domain=domain,
                ignore_urls=ignore_urls,
                processor=page_processor
            )
        )

    # Start the Crawler Process
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    for SpiderClass in active_spiders:
        process.crawl(SpiderClass)

    process.start()  # the script will block here until crawling is finished


if __name__ == '__main__':
    from search_engine_core.db import create_all

    db_interface = db.DbInterfaceSingleton(local=True)
    create_all()

    crawl(domains=[db_models.Domaines(id=1, url='https://en.wikipedia.org/wiki/Main_Page')])
