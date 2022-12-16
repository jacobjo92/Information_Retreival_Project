import scrapy


class EdxSpider(scrapy.Spider):
    name = 'viator4'

    def start_requests(self):
        # k =["2","3","4","5","6","7","8","9","10"]
        n = 40
        for i in range(2,n):
            yield scrapy.Request(url="https://www.viator.com/Las-Vegas/d684-ttd/"+ str(i),
                             callback=self.parse)

    def parse(self, response):
        for tour_href in response.xpath('//*[@class="product-card-row-title mb-0 pt-md-4"]/a/@href').getall():
            yield response.follow(tour_href, callback=self.parse_one_tour)

    def parse_one_tour(self, tour_page_response):
        title = tour_page_response.css('.title2__C3R7::text').get()
        # title =xs[0]
        price = tour_page_response.css('.defaultColor__1NL9::text').get()
        price = price.replace('CHF\u00a0', '')
        url = tour_page_response.url
        description = tour_page_response.xpath('//*[@class="overviewWrapper__bMs4"]/div/div/text()').extract()
        # description = ds[0]
        rating = tour_page_response.css('.averageRatingValue__Q1ep::text').get()      

        yield {
            "title": title,
            "description": description,
            "url":url,
            "price": price,
            "rating": rating,
        }

