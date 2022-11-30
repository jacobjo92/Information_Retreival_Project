import scrapy


class EdxSpider(scrapy.Spider):
    name = 'viator'

    def start_requests(self):
        yield scrapy.Request(url="https://www.viator.com/Netherlands/d60-ttd",
                             callback=self.parse)

    def parse(self, response):
        for tour_href in response.xpath('//*[@class="product-card-row-title mb-0 pt-md-4"]/a/@href').getall():
            yield response.follow(tour_href, callback=self.parse_one_tour)

    def parse_one_tour(self, tour_page_response):
        xs = tour_page_response.css('.title2__C3R7::text').getall()
        title = xs[0]
        price = tour_page_response.css('.defaultColor__1NL9::text').get()
        price = price.replace('CHF\u00a0', '')
        description = tour_page_response.xpath('//*[@class="overviewWrapper__bMs4"]/div/div/text()').extract()
        rating = tour_page_response.css('.averageRatingValue__Q1ep::text').get()      

        yield {
            "title": title,
            "description": description,
            "price": price,
            "rating": rating,
        }

