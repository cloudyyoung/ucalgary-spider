import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from nero.spiders.__utils import Utils
from nero.items import CourseCode


class CourseTitleSpider(CrawlSpider):
    name = 'course-code-title'
    allowed_domains = ['www.ucalgary.ca']
    titles_existed = []

    def start_requests(self):
        current_year = Utils.current_academic_year()
        base_url = "https://www.ucalgary.ca/pubs/calendar/archives/%s/course-by-faculty.html"

        # Past x years
        for t in range(10):
            year = current_year - t

            if(t == 0):
                url = "https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html"
            else:
                url = base_url % (year)

            yield scrapy.Request(url=url, callback=self.parse, meta={"year": year})

    def parse(self, response):
        body = str(response.body, encoding="utf-8")
        body = unidecode(body)
        body = re.sub(r"<span>(.*?)<\/span>", r"\1", body)
        body = re.sub(r'<a class="link-text" href="[a-z-]*?\.html#[0-9]{4,5}?"><\/a>', "", body)
        body = body.replace("\r", "").replace("\n", "").replace("  ", " ")
        body = htmlmin.minify(body, remove_empty_space=True, remove_all_empty_space=True)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")
        year = response.meta.get("year")

        print(response.url)

        for faculty_dom in faculties_dom:
            faculty_title = faculty_dom.select_one(".generic-title").get_text(strip=True)
            faculty_id = Utils.title_to_id(title=faculty_title, length=4)
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_code = course_title_dom.get_text(strip=True)
                course_title = course_title_dom.previous_element.strip()

                # For 2012-2013 calendar titles: "Communications Studies COMS ("
                regex = re.match(r"(.*) ([A-Z]{3,4})", course_title)
                if (regex):
                    course_title = regex.group(1)
                    course_code = regex.group(2)

                # For 2019 calendar title: "Innovation (AR, EN, HA, SC)"
                regex = re.match(r"(.*) \(.*\)", course_title)
                if(regex):
                    course_title = regex.group(1)

                # Check code and title
                regex_code = re.match(r"([A-Z]{3,4})", course_code)
                regex_title = re.match(r"([A-Z][a-z ,]*)", course_title)
                if(not regex_code or not regex_title):
                    continue

                if [course_code, course_title] in self.titles_existed:
                    continue

                self.titles_existed.append([course_code, course_title])

                course_title_obj = CourseCode(title=course_title, code=course_code, faculty=faculty_id, year=year)
                yield course_title_obj
