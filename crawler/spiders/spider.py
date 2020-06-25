import scrapy
from scrapy.linkextractors import LinkExtractor


class Spider(scrapy.Spider):
    custom_settings = {
        'DEPTH_LIMIT': 10
    }

    visited_urls = set()
    link_extractor = LinkExtractor()

    def parse(self, response):
        """parse the html response"""
        self.visited_urls.add(response.url)
        yield self.processor(response)

        links = self.link_extractor.extract_links(response)
        for link in links:
            if link.url not in self.visited_urls and link.url not in self.ignore_urls:
                yield scrapy.Request(link.url)
