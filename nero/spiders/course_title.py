import scrapy
import jsonlines
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from nero.items import CourseTitle
from bs4 import BeautifulSoup

class MySpider(CrawlSpider):
    name = 'course-titles'
    allowed_domains = ['www.ucalgary.ca']
    start_urls = [
        'https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html'
    ]

    def parse(self, response):
    
        body = str(response.body).strip()
        soup = BeautifulSoup(body, 'html.parser')

        # Wash - Prettify
        [x.unwrap() for x in soup.find_all((lambda tag: not tag.contents and tag.name == 'a'))]  # Remove empty <a>
        [x.unwrap() for x in soup.select(".generic-body span")] # Take out content from <span>

        # Wash - Remove Spaces
        body = str(soup.prettify()).strip().replace("\r", "").replace("\n", "").replace(
            "\t", "").replace("\\r", "").replace("\\n", "").replace("\\t", "").replace("\\", "").replace("  ", "")
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")
        faculties = {}

        for faculty_dom in faculties_dom:
            faculty_title = faculty_dom.select_one(".generic-title").get_text(strip=True)
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_url = course_title_dom.get("href")
                yield response.follow(course_url, self.parse_course_introduction)

                course_code = course_title_dom.get_text(strip=True)
                course_title = course_title_dom.previous_element.strip()
                course_title_obj = CourseTitle(title=course_title, code=course_code, faculty=faculty_title)
                yield course_title_obj

    def parse_course_introduction(self, response):

        self.logger.warning(response.url)
