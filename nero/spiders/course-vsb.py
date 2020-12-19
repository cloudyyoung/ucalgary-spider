import scrapy
import time
import math
import xmltodict
import json
from nero.utils import Utils
from unidecode import unidecode


class CourseVsbSpider(scrapy.Spider):
    name = 'course-vsb'
    allowed_domains = ['vsb.my.ucalgary.ca']
    start_urls = ['https://vsb.my.ucalgary.ca/criteria.jsp']

    def parse(self, response):
        # Method break:
        # https://vsb.my.ucalgary.ca/js/common.js?v=7515
        # function nWindow()

        t = math.floor(time.time() / 60) % 1000
        e = t % 3 + t % 29 + t % 42
        term = Utils.term_to_long_id("w", 21)
        yield response.follow("getclassdata.jsp?term=" + term + "&course_3_0=CHEM-201&va_3_0=b11c&rq_3_0=&t=" + str(t) + "&e=" + str(e) + "&nouser=1", self.parse2)
        pass

    def parse2(self, response):
        # print(response.body)
        body = str(response.body, encoding="utf-8")
        body = unidecode(body)
        body = xmltodict.parse(body)
        print(body['addcourse']['classdata']['course']['uselection'])

        blocks = {}

        uselectionGroup = body['addcourse']['classdata']['course']['uselection']
        if type(uselectionGroup) is not list:
            uselectionGroup = [uselectionGroup]

        for uselection in uselectionGroup:
            selectionGroup = uselection['selection']

            if type(selectionGroup) is not list:
                selectionGroup = [selectionGroup]

            for selection in selectionGroup:
                blockGroup = selection['block']
                
                for block in blockGroup:
                    key = block['@cartid']



        # print(body['addcourse']['classdata']['course']['uselection']['selection'][0]['block'][0]['@key'])
        # print(body['addcourse']['classdata']['course']['uselection']['selection'][0]['block'][1]['@key'])
        pass
