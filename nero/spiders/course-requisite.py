import json
import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from nero.utils import Utils
from nero.items import CourseRequisite, CourseTitle, CourseInfo


class CourseCalendar(CrawlSpider):
    name = 'course-requisite'
    allowed_domains = ['www.ucalgary.ca']
    start_urls = [
        'https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        count = 0

        course_info_file = open("data/course-info.jsonlines", "r")
        for line in course_info_file:
            count += 1
            if count < 100:
                continue
            elif count > 400:
                break

            course_info = json.loads(line)
            cid = course_info["cid"]
            code = course_info["code"]
            number = course_info["number"]
            prereq = course_info["prereq"]

            course_requisite_obj = CourseRequisite(cid=cid, code=code, number=number, prereq=prereq)
            yield course_requisite_obj

        course_info_file.close()
