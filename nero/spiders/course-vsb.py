import scrapy


class CourseVsbSpider(scrapy.Spider):
    name = 'course-vsb'
    allowed_domains = ['vsb.my.ucalgary.ca']
    start_urls = ['http://ucalgary.ca/']

    def parse(self, response):
        pass
