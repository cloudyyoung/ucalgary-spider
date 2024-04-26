import json
from scrapy import Spider, Request
from nero.items import SubjectCode


class SubjectCodeSpider(Spider):
    name = "subject-code"

    def start_requests(self):
        url = "https://app.coursedog.com/api/v1/ca/ucalgary_peoplesoft/search-configurations/3HheDcKChSNwS1Wr1Khr"
        print(url)

        yield Request(
            url=url,
            callback=self.parse,
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
