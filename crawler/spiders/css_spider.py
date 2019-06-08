import scrapy


class CSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for div in response.css("div"):
            yield self.get_content(div)

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def get_content(self, div):
        return {
            'text': div.css("span.text::text").extract(),
            'h1': div.css("small.author::text").extract_first(),
            'tags': div.css("div.tags > a.tag::text").extract()
            }
