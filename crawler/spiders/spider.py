import scrapy

class Spider(scrapy.Spider):
    def parse(self, response):
        yield self.processor(response)

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))