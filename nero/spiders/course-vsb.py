import scrapy
import time


class CourseVsbSpider(scrapy.Spider):
    name = 'course-vsb'
    allowed_domains = ['vsb.my.ucalgary.ca']
    start_urls = ['https://vsb.my.ucalgary.ca']

    def parse(self, response):
        yield response.follow("getclassdata.jsp?term=32211&course_3_0=CPSC-219&va_3_0=b11c&rq_3_0=&t=133&e=25&nouser=1&_=" + str(int(time.time())), self.parse2)
        pass

    def parse2(self, response):
        print(response)
        pass
