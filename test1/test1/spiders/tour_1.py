import scrapy


class EdxSpider(scrapy.Spider):
    name = 'getyourguide'

    def start_requests(self):
        yield scrapy.Request(url="https://www.getyourguide.co.uk/en-GB/s/?q=London&lc=l57&searchSource=4",
                             callback=self.parse)

    def parse(self, response):
        for tour_href in response.css('.list-element a::attr(href)').getall():
            yield response.follow(tour_href, callback=self.parse_one_tour)

    def parse_one_tour(self, tour_page_response):
        title = tour_page_response.css('.js-title::text').get()
        title = title.replace('\n         ','')
        title = title.replace('\n  ','')

        description = tour_page_response.css(
            '.activity-overview__content--certified::text').get()
        description = description.replace('\n    ','')

        if description == None:
            description = tour_page_response.css(
                '.activity-overview__content::text').get()

        price = tour_page_response.css(
            '.price-block__price-actual span::text').get()
        price = price.replace('£', '')

        rating = tour_page_response.css(
            '.activity__rating--totals::text').get()
        rating =rating.replace('\n      ','')
        rating =rating.replace('\n    ','')
      

        provider = tour_page_response.css('.supplier-name__link::text').get()
        provider = provider.replace('\n    ','')
        provider = provider.replace('\n  ','')
        yield {
            "title": title,
            "Description ": description,
            "price": price,
            "rating": rating,
            "provider": provider
        }
        # correctify(title, description, price, rating, provider)

        # def correctify(title, description, price, rating, provider):
        #     if tie
