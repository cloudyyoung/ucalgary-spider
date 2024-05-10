import json
import re
from scrapy import Spider, Request
from nero.items import SubjectCode


class SubjectCodeSpider(Spider):
    name = "subject-codes"

    def start_requests(self):
        url = "https://app.coursedog.com/api/v1/ca/ucalgary_peoplesoft/search-configurations/3HheDcKChSNwS1Wr1Khr"
        url_extra = "https://calendar.ucalgary.ca/courses?page=1&cq="

        # print(url)
        # yield Request(
        #     url=url,
        #     callback=self.parse,
        #     method="GET",
        #     headers={"Content-Type": "application/json"},
        # )

        print(url_extra)
        yield Request(
            url=url_extra,
            callback=self.parse_extra,
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

            yield SubjectCode(
                code=code,
                title=title,
            )

    def parse_extra(self, response):
        body = str(response.body, encoding="utf-8")
        start_string = 'Subject","Derived field from Subject code and Manual Input of Subject name",'
        end_string = "));"

        start = body.find(start_string)
        end = body.find(end_string, start)

        content = body[start + len(start_string) : end]

        # Find all strings within double quotes and decode unicode escapes
        strings = re.findall(r'"([^"]*)"', content)
        strings = [s.encode().decode("unicode_escape") for s in strings]

        # Filter ones that has <p> tags
        strings = [s for s in strings if "<p>" in s]

        for string in strings:
            code, title = re.findall(r"^<p>([A-Z]+) - (.+)</p>", string)[0]
            print(code, title)

            yield SubjectCode(
                code=code,
                title=title,
            )
