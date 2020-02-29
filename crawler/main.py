import time
from datetime import datetime, timedelta

import pytz
from search_engine_core import db
from search_engine_core.db import models as db_models
from search_engine_core.config import Config

from crawler import crawl


def initiate():
    # Get Config
    config = Config()
    config.read('config.ini')
    # create all tables
    db_interface = db.DbInterfaceSingleton(host='mysql')
    db.create_all()

    # Add some domains to db
    domain = db_models.Domaines(url='https://en.wikipedia.org/wiki/Main_Page')
    db_interface.merge([domain])


def main():
    initiate()
    config = Config()

    crawl_interval = timedelta(
        minutes=int(config['settings']['crawl_interval_minutes'])
    )

    last_update = datetime(1, 1, 1, tzinfo=pytz.utc)

    # Get urls to crawl
    domains = db.query.query_domains()

    while datetime.now(tz=pytz.utc) - last_update >= crawl_interval:
        # crawl all Urls
        crawl(domains)
        time.sleep(1)


if __name__ == '__main__':
    main()
