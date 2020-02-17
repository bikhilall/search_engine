import time
from datetime import datetime, timedelta

import pytz
from search_engine_core import db
from search_engine_core.db import models as db_models

from crawler import crawl


def inititate():
    # create all tables
    db.create_all()

    # Add some domains to db
    domain = db_models.Domaines(url='https://en.wikipedia.org/wiki/Main_Page')
    db_interface = db.DbInterface()
    db_interface.merge([domain])


def main():
    inititate()

    crawl_interval = timedelta(days=1)
    last_update = datetime(1, 1, 1, tzinfo=pytz.utc)

    # Get urls to crawl
    domains = db.query.query_domains()

    while datetime.now(tz=pytz.utc) - last_update >= crawl_interval:
        # crawl all Urls
        crawl(domains)
        time.sleep(1)


if __name__ == '__main__':
    main()
