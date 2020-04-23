import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = [
        'example.com'
    ]

    global_urls = []

    def parse(self, response):

        file1 = open("./URLs/urls.txt", "a+")

        SET_SELECTOR = 'li.post'

        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::attr(href)'
            url = brickset.css(NAME_SELECTOR).extract()
            if url and len(url) > 0:
                if url[0] not in self.global_urls:
                    self.global_urls.append(url[0])
                    file1.write(", '{0}'".format(url[0]))
        file1.close()
