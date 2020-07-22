import scrapy
import jsonlines
import htmlmin
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from nero.items import CourseTitle, Course
from bs4 import BeautifulSoup

class MySpider(CrawlSpider):
    name = 'course-titles'
    allowed_domains = ['www.ucalgary.ca']
    start_urls = [
        'https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html'
    ]

    def parse(self, response):
    
        body = str(response.body, encoding="utf-8")
        body = re.sub("<span>(.*?)<\/span>", r"\1",body)
        body = re.sub('<a class="link-text" href="[a-z-]*?\.html#[0-9]{4,5}?"><\/a>', "", body)
        body = body.replace("\r", "").replace("\n", "").replace("  ", " ")
        body = htmlmin.minify(body, remove_empty_space=True, remove_all_empty_space=True)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")

        for faculty_dom in faculties_dom:
            faculty_title = faculty_dom.select_one(".generic-title").get_text(strip=True)
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_url = course_title_dom.get("href")
                if course_url == "art.html":
                    yield response.follow(course_url, self.parse_course_introduction)

                course_code = course_title_dom.get_text(strip=True)
                course_title = course_title_dom.previous_element.strip()
                course_title_obj = CourseTitle(title=course_title, code=course_code, faculty=faculty_title)
                yield course_title_obj

    def parse_course_introduction(self, response):

        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        soup = BeautifulSoup(body, 'html.parser')

        courses_dom = soup.select("#ctl00_ctl00_pageContent .item-container table[bgcolor][cellpadding][align]")

        for course_dom in courses_dom:

            description = course_dom.select_one(".course-desc").get_text(strip=True)
            cid = int(course_dom.previous_element.attrs['name'])

            course_obj = Course(cid=cid, description=description)
            yield course_obj
            pass
        
        self.logger.warning(response.url)
