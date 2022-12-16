import scrapy


class EdxSpider(scrapy.Spider):
    name = 'switzerlandtours'

    def start_requests(self):
        yield scrapy.Request(url="https://www.switzerland-tours.ch/tours/all-tours/",
                             callback=self.parse)

    def parse(self, response):
        for tour_href in response.css('.title a::attr(href)').getall():
            yield response.follow(tour_href, callback=self.parse_one_tour)

    def parse_one_tour(self, tour_page_response):
        title = tour_page_response.css('h1::text').get()
        xs = tour_page_response.css('td::text').getall()
        price = xs[5]
        description = tour_page_response.css('p::text').get()
        url = tour_page_response.url
        inclusions = tour_page_response.xpath('//*[@class="inclusions"]/ul/li//text()').getall()
        exclusions = tour_page_response.xpath('//*[@class="exclusions"]/ul/li//text()').getall()
        know_before_you_go = tour_page_response.xpath('//*[@class="knowbeforeyougo"]/ul/li//text()').getall()
      

        yield {
            "title": title,
            "price": price,
            "url":url,
            "description": description,
            "inclusions": inclusions,
            "exclusions": exclusions,
            "know_before_you_go": know_before_you_go
        }

