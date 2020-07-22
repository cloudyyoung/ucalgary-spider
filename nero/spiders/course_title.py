import scrapy
import jsonlines
import htmlmin
import re
import unidecode
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
        body = unidecode.unidecode(body)
        body = re.sub(r"<span>(.*?)<\/span>", r"\1", body)
        body = re.sub(r'<a class="link-text" href="[a-z-]*?\.html#[0-9]{4,5}?"><\/a>', "", body)
        body = body.replace("\r", "").replace("\n", "").replace("  ", " ")
        body = htmlmin.minify(body, remove_empty_space=True, remove_all_empty_space=True)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")

        for faculty_dom in faculties_dom:
            faculty_title = faculty_dom.select_one(".generic-title").get_text(strip=True)
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_url = course_title_dom.get("href")
                if course_url == "physics.html":
                    yield response.follow(course_url, self.parse_course_introduction)

                course_code = course_title_dom.get_text(strip=True)
                course_title = course_title_dom.previous_element.strip()
                course_title_obj = CourseTitle(title=course_title, code=course_code, faculty=faculty_title)
                yield course_title_obj


    def parse_course_introduction(self, response):

        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode.unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        code = soup.select_one(".page-title").string.split(" ")[-1]

        courses_dom = soup.select("#ctl00_ctl00_pageContent .item-container table[bgcolor][cellpadding][align]")

        for course_dom in courses_dom:

            cid = int(course_dom.previous_element.attrs['name'])

            keys = course_dom.select(".course-code")
            number = keys[1].get_text(strip=True)

            description = course_dom.select_one(".course-desc").string
            sub_topics = {}
            if description is not None:
                description = description.strip()
            else:
                description = ""
                description_dom = course_dom.select_one(".course-desc").contents

                for description_dom in description_dom:
                    sub_topics_reg = r"[0-9]{3}\.([0-9]{2})[\.]? ([A-Za-z \,\(\)\'\-][^0-9]*)"
                    sub_topics_reg_res_all = re.findall(sub_topics_reg, description_dom.get_text())

                    if sub_topics_reg_res_all:
                        for sub_topics_reg_res in sub_topics_reg_res_all:
                            decimal = int(sub_topics_reg_res[0])
                            topic = sub_topics_reg_res[1].strip()
                            sub_topics[decimal] = topic
                    elif description_dom.string:
                        description += str(description_dom.string.strip())
                    else:
                        self.convert_link(description_dom)
                        description += str(description_dom)

            course_obj = Course(cid=cid, code=code, number=number, description=description, sub_topics=sub_topics)
            yield course_obj
            pass
        
        self.logger.warning(response.url)


    def convert_link(self, doms):
        for dom in doms.select("a"):
                if dom.name == "a":
                    href = dom.get("href").split("#")[-1]
                    dom.attrs = {"cid": href}
        return doms
