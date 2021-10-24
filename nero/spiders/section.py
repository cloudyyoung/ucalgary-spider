
import scrapy
import htmlmin
from unidecode import unidecode
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from nero.spiders.__parser import FacultyDirectoryParser, CourseDirectoryParser
from nero.spiders.__utils import Utils
from nero.items import Section


class SectionSpider(CrawlSpider):
    name = 'section'
    allowed_domains = ['contacts.ucalgary.ca']
    start_urls = [
        'http://contacts.ucalgary.ca/directory/faculties',
        'http://contacts.ucalgary.ca/directory/departments'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select(".primary-row")
        for faculty_dom in faculties_dom:
            fdp = FacultyDirectoryParser(faculty_dom)
            title, code = fdp.title()
            directory = fdp.directory_of_people()
            parent_title, parent_type = fdp.parent()

            if directory and code != None and parent_title != None and parent_type != None:  # If has contact directory
                year = Utils.current_academic_year()
                yield response.follow("/info/%s/courses/%s" % (code, "f" + str(year)), self.parse_course_term_section)  # Fall
                yield response.follow("/info/%s/courses/%s" % (code, "w" + str(year + 1)), self.parse_course_term_section)  # Winter
                # yield response.follow("/info/%s/courses/%s" % (code, "p" + str(year + 1)), self.parse_course_term_block)  # Spring
                # yield response.follow("/info/%s/courses/%s" % (code, "s" + str(year + 1)), self.parse_course_term_block)  # Summer

    def parse_course_term_section(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        term = Utils.abbr_to_term(response.url.split("/")[-1][0])
        year = response.url.split("/")[-1][1:]

        print(response.url)

        courses_dom = soup.select(".unitis-courses.primary-row")
        for course_dom in courses_dom:
            detail_dom = course_dom.next_sibling

            cdp = CourseDirectoryParser(course_dom)
            key, topic = cdp.title()

            for (name, time, room, sid, directory_id, note) in cdp.sections():
                section_obj = Section(key=key, topic=topic, year=year, term=term, name=name, time=time, room=room, sid=sid, directory_id=directory_id, note=note)
                yield section_obj
