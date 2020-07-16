import scrapy


class MySpider(scrapy.Spider):
    name = 'course-titles'
    allowed_domains = ['www.ucalgary.ca']
    start_urls = [
        'https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html'
    ]

    def parse(self, response):
        # page = response.url.split("/")[-1]
        # filename = page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        pass
