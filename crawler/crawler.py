import os
from typing import List

import spiders
import parser
from scrapy.crawler import CrawlerProcess
from lib.encoder_api import encode, EncoderApi
from search_engine_core import db
from search_engine_core.db.models import models as db_models

db_interface = db.DbInterfaceSingleton()


def encode_all(texts: List[str]) -> List[float]:
    encoder_api = EncoderApi(base_url=os.environ['ENCODER_API_BASE_URL'])
    return encoder_api.encode(texts)


def page_processor(response, domain, *kws, **kwargs):
    page = parser.Page(response)
    content_vector = encode(page.content[:1000])
    title_vector = encode(page.title)
    page_db = db_models.Pages(
        domain_id=domain.id,
        url=page.url,
        title=page.title,
        title_vector=title_vector,
        content_vector=content_vector
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
