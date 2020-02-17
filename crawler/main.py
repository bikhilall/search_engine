from datetime import datetime, timedelta

import pytz

from .crawler import crawl


def main():
    crawl_interval = timedelta(days=1)
    last_update = datetime(1, 1, 1, tzinfo=pytz.utc)

    # Get urls to crawl
    urls = ['https://www.wikipedia.org']

    while datetime.now(tz=pytz.utc) - last_update >= crawl_interval:
        # crawl all Urls
        crawl(urls)


if __name__ == '__main__':
    main()
