import scrapy

class SiteSpider(scrapy.Spider):
    name = 'info'
    start_urls = [
        'http://localhost:8000/car'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/samll/text()').get(),
                'text': quote.css('span.text::text').get(),
            }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
