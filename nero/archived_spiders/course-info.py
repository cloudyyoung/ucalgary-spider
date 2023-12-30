import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from nero.archived_spiders.__parser import CourseInfoParser
from nero.items import CourseInfo


class CourseInfoSpider(CrawlSpider):
    name = 'course-info'
    allowed_domains = ['www.ucalgary.ca']
    start_urls = [
        'https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = str(response.body, encoding="utf-8")
        body = unidecode(body)
        body = re.sub(r"<span>(.*?)<\/span>", r"\1", body)
        body = re.sub(r'<a class="link-text" href="[a-z-]*?\.html#[0-9]{4,5}?"><\/a>', "", body)
        body = body.replace("\r", "").replace("\n", "").replace("  ", " ")
        body = htmlmin.minify(body, remove_empty_space=True, remove_all_empty_space=True)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")

        for faculty_dom in faculties_dom:
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_url = course_title_dom.get("href")
                yield response.follow(course_url, self.parse_course_introduction)

    def parse_course_introduction(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"),
                              remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        code = soup.select_one(".page-title").string.strip().split(" ")[-1]

        courses_dom = soup.select(
            "#ctl00_ctl00_pageContent .item-container table[bgcolor][cellpadding][align]")
        for course_dom in courses_dom:

            cp = CourseInfoParser(course_dom)

            cid = cp.calendar_id
            title, number, topic = cp.title_number_topic()
            description, sub_topics = cp.description_subtopics()
            prereq, coreq, antireq, notes, aka = cp.requisites()
            repeat, nogpa = cp.repeat_nogpa()
            units, credits, hours, time_length = cp.units_credits_hours_time_length()

            course_obj = CourseInfo(cid=cid, code=code, number=number, topic=topic,
                                    description=description, sub_topics=sub_topics,
                                    units=units, credits=credits, hours=hours,
                                    time_length=time_length, prereq=prereq, coreq=coreq,
                                    antireq=antireq, notes=notes, aka=aka,
                                    repeat=repeat, nogpa=nogpa)
            yield course_obj

        self.logger.warning(response.url)
