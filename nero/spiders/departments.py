import json
from scrapy import Spider, Request
from nero.items import Department, Faculty


class DepartmentsSpider(Spider):
    name = "departments"

    def start_requests(self):
        url = "https://app.coursedog.com/api/v1/ucalgary_peoplesoft/departments"
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

        for department in body.values():
            id = department["id"]
            name = department["name"]
            display_name = department["displayName"]

            active = department["status"] == "Active"

            if len(id) == 2:
                # Two letters code is a faculty
                yield Faculty(
                    id=id,
                    name=name,
                    display_name=display_name,
                    active=active,
                )

            else:
                #  Four letters code is a department
                yield Department(
                    id=id,
                    name=name,
                    display_name=display_name,
                    active=active,
                )
