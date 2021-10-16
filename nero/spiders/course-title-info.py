import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from nero.utils import Utils
from nero.items import CourseTitle, CourseInfo


class CourseCalendar(CrawlSpider):
    name = 'course-title-info'
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
            faculty_title = faculty_dom.select_one(".generic-title").get_text(strip=True)
            faculty_id = Utils.title_to_id(title=faculty_title, length=4)
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_url = course_title_dom.get("href")
                yield response.follow(course_url, self.parse_course_introduction)

                course_code = course_title_dom.get_text(strip=True)
                course_title = course_title_dom.previous_element.strip()
                course_title_obj = CourseTitle(
                    title=course_title, code=course_code, faculty=faculty_id)
                yield course_title_obj

    def parse_course_introduction(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"),
                              remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        code = soup.select_one(".page-title").string.strip().split(" ")[-1]

        courses_dom = soup.select(
            "#ctl00_ctl00_pageContent .item-container table[bgcolor][cellpadding][align]")
        for course_dom in courses_dom:

            cid = self.cid(course_dom=course_dom)
            title, number, topic = self.key(course_dom=course_dom)
            description, sub_topics = self.description(course_dom=course_dom)
            prereq, coreq, antireq, notes, aka = self.requirements(course_dom=course_dom)
            repeat, nogpa = self.repeat(course_dom=course_dom)
            units, credits, hours, time_length = self.hours(course_dom=course_dom)

            course_obj = CourseInfo(cid=cid, code=code, number=number, topic=topic,
                                    description=description, sub_topics=sub_topics,
                                    units=units, credits=credits, hours=hours,
                                    time_length=time_length, prereq=prereq, coreq=coreq,
                                    antireq=antireq, notes=notes, aka=aka,
                                    repeat=repeat, nogpa=nogpa)
            yield course_obj

        self.logger.warning(response.url)

    def convert_link(self, doms):
        for dom in doms.select("a.link-text"):
            href = dom.get("href").split("#")[-1].strip()
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

        description = []
        sub_topics = {}
        concat_text = " "

        for description_dom in description_dom.contents:
            sub_topics_reg = r"[0-9]{3}\.([0-9]{2})[\.]? ([A-Za-z \,\(\)\'\-][^0-9<]*)"
            sub_topics_reg_res_all = re.findall(
                sub_topics_reg, str(description_dom))

            if sub_topics_reg_res_all:  # Contain sub topics
                for sub_topics_reg_res in sub_topics_reg_res_all:
                    decimal = sub_topics_reg_res[0]
                    topic = sub_topics_reg_res[1].strip()
                    sub_topics[decimal] = topic
                concat_text = "<br>"
            elif description_dom.name == "a":  # Link
                description.append(str(description_dom).strip())
            elif description_dom.string:  # Pure string
                description.append(str(description_dom.string.strip()))
            else:
                description.append(description_dom.decode_contents().strip())
        pass

        description = concat_text.join(description)

        if not description:
            description = None

        if not sub_topics:
            sub_topics = None

        return (description, sub_topics)

    def requirements(self, course_dom):
        ret = {"prereq": None, "coreq": None, "antireq": None, "notes": None, "aka": None}

        for each in ret.keys():
            req_dom = course_dom.select_one(".course-" + each)
            self.convert_link(req_dom)

            inner_html = req_dom.decode_contents().strip()

            if inner_html:
                ret[each] = inner_html
            else:
                ret[each] = None

        return (ret["prereq"], ret["coreq"], ret["antireq"], ret["notes"], ret["aka"])

    def repeat(self, course_dom):
        ret = {"repeat": False, "nogpa": False}

        for each in ret.keys():
            repeat_dom = course_dom.select_one(".course-" + each)
            content = repeat_dom.get_text(strip=True)

            ret[each] = content != ""

        return (ret["repeat"], ret["nogpa"])

    def hours(self, course_dom):
        hours_text = course_dom.select_one(
            ".course-hours").get_text(strip=True)
        hours_reg = {
            "units": r"([0-9.]*?) units",  # units
            "credits": r"([0-9.]*?) credit[s]?",  # credits
            "hours": r"\((.*?[0-9A-Za-z\/]-.*?[0-9A-Z\/])\)",  # h(x-y)
            "time_length": r"\((.*?[0-9-] .*?[a-zA-Z])\)"  # x period
        }
        ret = {}  # [units, credits, h(x-y), x period]

        for (key, reg) in hours_reg.items():

            if not re.search(reg, hours_text):
                ret[key] = None
                continue

            hours_reg_res = re.findall(reg, hours_text)  # Find text
            hours_text = re.sub(reg, "", hours_text)  # Remove matched text

            if key == "units" or key == "credits":
                ret[key] = float(hours_reg_res[0])
            else:
                ret[key] = list(hours_reg_res)

        return (ret["units"], ret["credits"], ret["hours"], ret["time_length"])
