import scrapy
import time
import math
from nero.utils import Utils


class CourseVsbSpider(scrapy.Spider):
    name = 'course-vsb'
    allowed_domains = ['vsb.my.ucalgary.ca']
    start_urls = ['https://vsb.my.ucalgary.ca']

    def parse(self, response):
        # Method break:
        # https://vsb.my.ucalgary.ca/js/common.js?v=7515
        # function nWindow()

        t = math.floor(time.time() / 60) % 1000
        e = t % 3 + t % 29 + t % 42
        term = Utils.term_to_long_id("w", 21)
        yield response.follow("getclassdata.jsp?term=" + term + "&course_3_0=CPSC-219&va_3_0=b11c&rq_3_0=&t=" + str(t) + "&e=" + str(e) + "&nouser=1", self.parse2)
        pass

    def parse2(self, response):
        print(response)
        pass
