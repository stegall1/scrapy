import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):

        all_the_books = response.xpath('//article')
        
        for book in all_the_books:
           title = book.xpath('.//h3/a/@title').extract_first()
           price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
           print(title)
           print(price)
