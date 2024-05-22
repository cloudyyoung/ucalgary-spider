import json
import re
import htmlmin
from scrapy import Spider, Request
from nero.items import SubjectCode
from unidecode import unidecode
from bs4 import BeautifulSoup


class SubjectCodeSpider(Spider):
    name = "subject-codes"

    # List of titles that have been processed
    subject_codes = []

    def start_requests(self):
        url = "https://app.coursedog.com/api/v1/ca/ucalgary_peoplesoft/search-configurations/3HheDcKChSNwS1Wr1Khr"
        url_extra = "https://calendar.ucalgary.ca/courses"
        url_archive = (
            "https://www.ucalgary.ca/pubs/calendar/archives/%s/course-by-faculty.html"
        )

        print(url)
        yield Request(
            url=url,
            callback=self.parse,
            method="GET",
            headers={"Content-Type": "application/json"},
        )

        print(url_extra)
        yield Request(
            url=url_extra,
            callback=self.parse_extra,
            method="GET",
            headers={"Content-Type": "application/json"},
        )

        for year in range(2009, 2023):
            print(url_archive % year)
            yield Request(
                url=url_archive % year,
                callback=self.parse_archive,
                method="GET",
                headers={"Content-Type": "application/json"},
            )

        yield Request(
            url="https://google.com",
            callback=self.yield_additional_codes,
            method="GET",
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

            if code in self.subject_codes:
                continue

            yield SubjectCode(
                code=code,
                title=title,
            )

            self.subject_codes.append(code)

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

            if code in self.subject_codes:
                continue

            yield SubjectCode(
                code=code,
                title=title,
            )
            self.subject_codes.append(code)

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

        faculties_dom = soup.select("#ctl00_ctl00_pageContent .item-container")

        print(response.url)

        for faculty_dom in faculties_dom:
            course_titles_dom = faculty_dom.select(".generic-body .link-text")

            for course_title_dom in course_titles_dom:
                course_code = course_title_dom.get_text(strip=True)
                course_title = str(course_title_dom.previous_element).strip()

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

                if course_code in self.subject_codes:
                    continue

                self.subject_codes.append(course_code)

                yield SubjectCode(
                    code=course_code,
                    title=course_title,
                )

    def yield_additional_codes(self, _):
        # Additional codes
        yield SubjectCode(
            code="COMS",
            title="Communications Studies",
        )

        yield SubjectCode(
            code="MDSC",
            title="Medical Sciences",
        )

        yield SubjectCode(
            code="ENSF",
            title="Software Engineering for Software Engineers",
        )
        
        yield SubjectCode(
            code="ASHA",
            title="Arts and Science Honours Academy",
        )
