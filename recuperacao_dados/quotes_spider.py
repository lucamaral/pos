import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes.toscape.com'

    start_urls = ['http://quotes.toscrape.com/']

    def parse_author(self, response):
        bornDate = response.css('.author-born-date::text').get()
        dados = response.meta['dados']
        dados["bornDate"] = bornDate
        return dados


    def parse (self, response):
        for quote in response.css('.quote'):
            text = quote.css('.text::text').get()
            author = quote.css('.author::text').get()
            href = quote.css('.author + a::attr(href)').get()
            yield response.follow(
                                href, 
                                dont_filter = true,
                                callback = self.parse_author, 
                                meta = {
                                    'dados' : {
                                      'text' : text,
                                      'author' : author
                                    }
                                })
        for next_page in response.css('.next a'):
            yield response.follow(next_page, self.parse)