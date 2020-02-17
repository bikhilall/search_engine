import scrapy
from scrapy.linkextractors import LinkExtractor

class Spider(scrapy.Spider):
    custom_settings = {
        'DEPTH_LIMIT': 10
    }

    link_extractor = LinkExtractor()

    def parse(self, response):
        yield self.processor(response)

        links = self.link_extractor.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url)