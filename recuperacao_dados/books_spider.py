# nome do livro
# descricao

import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books.toscape.com'

    start_urls = ['http://books.toscrape.com/']

    def parse_book(self, response):
        name = response.css('.product_main h1::text').get()
        price = response.css('.product_main .price_color::text').get()
        star_rating = response.css('.product_main .star-rating::attr(class)').get().replace('star-rating','')
        description = response.css('#product_description + p::text').get()
        return {
            'name' : name,
            'price' : price,
            'star_rating' : star_rating,
            'description' : description
        }


    def parse (self, response):
        for book in response.css('article.product_pod'):
            href = book.css('a::attr(href)').get()
            yield response.follow(
                                href, 
                                callback = self.parse_book)
        for next_page in response.css('.next a'):
            yield response.follow(next_page, self.parse)