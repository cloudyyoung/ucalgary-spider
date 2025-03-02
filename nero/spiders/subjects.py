import json
import re
import htmlmin
from scrapy import Spider, Request
from nero.items import Subject, Department
from unidecode import unidecode
from bs4 import BeautifulSoup


class SubjectCodeSpider(Spider):
    name = "subjects"

    # List of titles that have been processed
    subject_codes = []

    def start_requests(self):
        url = "https://app.coursedog.com/api/v1/ca/ucalgary_peoplesoft/search-configurations/3HheDcKChSNwS1Wr1Khr"
        url_extra = "https://calendar.ucalgary.ca/courses"
        url_archive = (
            "https://www.ucalgary.ca/pubs/calendar/archives/%s/course-by-faculty.html"
        )
        url_catalog_questions = "https://app.coursedog.com/api/v1/ucalgary_peoplesoft/general/courseTemplate/questions"

        print(url)
        yield Request(
            url=url,
            callback=self.parse,
            method="GET",
            headers={"Content-Type": "application/json"},
        )

        # print(url_extra)
        # yield Request(
        #     url=url_extra,
        #     callback=self.parse_extra,
        #     method="GET",
        #     headers={"Content-Type": "application/json"},
        # )

        # for year in range(2009, 2023):
        #     print(url_archive % year)
        #     yield Request(
        #         url=url_archive % year,
        #         callback=self.parse_archive,
        #         method="GET",
        #         headers={"Content-Type": "application/json"},
        #         meta={"year": year},
        #     )

        # yield Request(
        #     url="https://google.com",
        #     callback=self.yield_additional_subjects,
        #     method="GET",
        # )

        print(url_catalog_questions)
        yield Request(
            url=url_catalog_questions,
            callback=self.parse_catalog_questions,
            method="GET",
            headers={"Content-Type": "application/json"},
        )

    def parse(self, response):
        body = str(response.body, encoding="utf-8")
        body = json.loads(body)

        filters = body["filters"]
        subject_code_filter = filters[0]
        options = subject_code_filter["config"]["options"]

        for option in options:
            value = str(option["value"])
            label = str(option["label"])
            code, title = label.split(" - ", 1)
            yield from self.yield_subject(code, title)

    def parse_extra(self, response):
        body = str(response.body, encoding="utf-8")
        start_string = 'Subject","Derived field from Subject code and Manual Input of Subject name",'
        end_string = "));"

        start = body.find(start_string)
        end = body.find(end_string, start)

        content = body[start + len(start_string) : end]

        # Find all strings within double quotes and decode unicode escapes
        strings = re.findall(r'"([^"]*)"', content)
        strings = [str(s).encode().decode("unicode_escape") for s in strings]

        # Filter ones that has <p> tags
        strings = [s for s in strings if "<p>" in s]

        for string in strings:
            code, title = re.findall(r"^<p>([A-Z]+) - (.+)</p>", string)[0]
            title = title.replace("&amp;", "&")
            yield from self.yield_subject(code, title)

    def parse_archive(self, response):
        body = str(response.body, encoding="utf-8")
        body = unidecode(body)
        body = re.sub(r"<span>(.*?)<\/span>", r"\1", body)
        body = re.sub(
            r'<a class="link-text" href="[a-z-]*?\.html#[0-9]{4,5}?"><\/a>', "", body
        )
        body = body.replace("\r", "").replace("\n", "").replace("  ", " ")
        body = htmlmin.minify(
            body, remove_empty_space=True, remove_all_empty_space=True
        )
        soup = BeautifulSoup(body, "html.parser")

        year = response.meta["year"]

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")

        print(response.url)

        for faculty_dom in faculties_dom:
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_code = course_title_dom.get_text(strip=True)
                course_title = str(course_title_dom.previous_element).strip()
                course_title = re.sub(r"\s+", " ", course_title)

                # For 2012-2013 calendar titles: "Communications Studies COMS ("
                regex = re.match(r"(.*) ([A-Z]{3,4})", course_title)
                if regex:
                    course_title = regex.group(1)
                    course_code = regex.group(2)

                # For 2019 calendar title: "Innovation (AR, EN, HA, SC)"
                regex = re.match(r"(.*) \(.*\)", course_title)
                if regex:
                    course_title = regex.group(1)

                # Check code and title
                regex_code = re.match(r"([A-Z]{3,4})", course_code)
                regex_title = re.match(r"([A-Z][a-z ,]*)", course_title)
                if not regex_code or not regex_title:
                    continue

                yield from self.yield_subject(course_code, course_title, year)

    def parse_catalog_questions(self, response):
        body = str(response.body, encoding="utf-8")
        body = json.loads(body)

        w3rO8 = body["w3rO8"]
        actions = w3rO8["actions"]

        for action in actions:
            effects = action["effects"]

            for effect in effects:
                value = str(effect["value"])
                value = value.replace("<p>", "")
                value = value.replace("</p>", "")

                if " - " not in value:
                    print("Skipping value:", value)
                    continue

                subject_code, title = value.split(" - ", 1)
                yield from self.yield_subject(subject_code, title)

    def yield_additional_subjects(self, _):
        # Additional codes
        yield from self.yield_subject("ENGG", "Engineering")
        yield from self.yield_subject("COMS", "Communications Studies")
        yield from self.yield_subject("MDSC", "Medical Sciences")
        yield from self.yield_subject(
            "ENSF", "Software Engineering for Software Engineers"
        )
        yield Subject(
            code="ASHA",
            title="Arts and Science Honours Academy",
        )
        yield Department(
            code="ASHA",
            name="Arts and Science Honours Academy",
            display_name="Arts and Science Honours Academy",
            is_active=False,
        )

    def yield_subject(self, subject_code, title, year=None):
        if subject_code == "NRSG":
            title = "Nursing (Graduate)"

        if (subject_code, title) in self.subject_codes:
            return

        # if title exists but with different subject code
        # name = f"{title}; Subject of"
        # display_name = title
        # if title in [t for _, t in self.subject_codes]:
        #     if year:
        #         name = f"{title} ({year}); Subject of"

        yield Subject(
            code=subject_code,
            title=title,
        )

        # yield Department(
        #     code=subject_code,
        #     name=name,
        #     display_name=display_name,
        #     is_active=False,
        # )

        self.subject_codes.append((subject_code, title))
