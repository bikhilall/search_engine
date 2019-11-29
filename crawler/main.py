from scrapy.crawler import CrawlerProcess
from crawler import spiders
from crawler import parser


def page_processor(response):
    page = parser.Page(response)
    print(page.content[:100])


Spider1 = spiders.build_spider(
    spider=spiders.Spider,
    name='spider_1',
    urls=[
        'http://quotes.toscrape.com/',
    ],
    processor=page_processor
)

# Start the Crawler Process
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(Spider1)
process.start()  # the script will block here until the crawling is finished
