import scrapy
import csv


class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = []

    def parse(self, response):

        rows = []
        filename = "data.csv"

        SET_SELECTOR = 'li.k-content'
        category = None
        news = []

        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::text'
            category = brickset.css(NAME_SELECTOR).extract()
            if category and len(category) > 0:
                category = category[0]

        SET_SELECTOR = '.has-content-area'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'p ::text'
            news = brickset.css(NAME_SELECTOR).extract()

        for item in news:
            if len(item) > 50:
                rows.append([item, category if category is not None else "busad"])

        with open(filename, 'a+') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the data rows
            csvwriter.writerows(rows)
