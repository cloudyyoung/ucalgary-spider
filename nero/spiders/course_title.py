import scrapy
import jsonlines
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from nero.items import CourseTitle, CourseInfo
from bs4 import BeautifulSoup

class MySpider(CrawlSpider):
    name = 'course-titles'
    allowed_domains = ['www.ucalgary.ca']
    start_urls = [
        'https://www.ucalgary.ca/pubs/calendar/current/course-by-faculty.html'
    ]

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
            faculty_title = faculty_dom.select_one(".generic-title").get_text(strip=True)
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_url = course_title_dom.get("href")
                if course_url == "medical-science.html":
                    yield response.follow(course_url, self.parse_course_introduction)

                course_code = course_title_dom.get_text(strip=True)
                course_title = course_title_dom.previous_element.strip()
                course_title_obj = CourseTitle(title=course_title, code=course_code, faculty=faculty_title)
                yield course_title_obj


    def parse_course_introduction(self, response):

        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        code = soup.select_one(".page-title").string.split(" ")[-1]

        courses_dom = soup.select("#ctl00_ctl00_pageContent .item-container table[bgcolor][cellpadding][align]")
        for course_dom in courses_dom:

            cid = self.cid(course_dom=course_dom)
            title, number, topic = self.key(course_dom=course_dom)
            description, sub_topics = self.description(course_dom=course_dom)
            prereq, coreq, antireq, notes, aka = self.requirements(course_dom=course_dom)
            # print(prereq, coreq)

            course_obj = CourseInfo(cid=cid, code=code, number=number, topic=topic, description=description, sub_topics=sub_topics)
            yield course_obj
        
        self.logger.warning(response.url)


    def convert_link(self, doms):
        for dom in doms.select("a.link-text"):
            href = dom.get("href").split("#")[-1]
            dom.attrs = {"cid": href}
            dom.name = "course"
        return doms

    def cid(self, course_dom):
        return int(course_dom.previous_element.attrs['name'])

    def key(self, course_dom):
        keys = course_dom.select(".course-code")
        title = keys[0].get_text(strip=True)
        number = int(keys[1].get_text(strip=True))
        topic = keys[2].get_text(strip=True)
        return (title, number, topic)

    def description(self, course_dom):
        description_dom = course_dom.select_one(".course-desc")
        self.convert_link(description_dom)

        # print(description_dom)

        description = []
        sub_topics = {}
        concat_text = " "

        for description_dom in description_dom.contents:
            sub_topics_reg = r"[0-9]{3}\.([0-9]{2})[\.]? ([A-Za-z \,\(\)\'\-][^0-9<]*)"
            sub_topics_reg_res_all = re.findall(sub_topics_reg, str(description_dom))

            if sub_topics_reg_res_all: # Contain sub topics
                for sub_topics_reg_res in sub_topics_reg_res_all:
                    decimal = sub_topics_reg_res[0]
                    topic = sub_topics_reg_res[1].strip()
                    sub_topics[decimal] = topic
                concat_text = "<br>"
            elif description_dom.name == "a": # Link
                description.append(str(description_dom))
            elif description_dom.string: # Pure string
                description.append(str(description_dom.string.strip()))
            else:
                description.append(description_dom.decode_contents())
        pass

        description = concat_text.join(description)

        if not description:
            description = None

        if not sub_topics:
            sub_topics = None

        return (description, sub_topics)


    def requirements(self, course_dom):
        req = ["prereq", "coreq", "antireq", "notes", "aka"]
        res = {}

        for each in req:
            req_dom = course_dom.select_one(".course-" + each)
            self.convert_link(req_dom)

            inner_html = req_dom.decode_contents()

            if inner_html:
                res[each] = inner_html
            else:
                res[each] = None

        return (res["prereq"], res["coreq"], res["antireq"], res["notes"], res["aka"])
