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

        # yield Request(
        #     url="https://google.com",
        #     callback=self.yield_additional_departments,
        #     method="GET",
        # )

    def parse(self, response):
        body = str(response.body, encoding="utf-8")
        body = json.loads(body)

        for department in body.values():
            code = department["id"]
            name = department["name"]
            display_name = department["displayName"]
            active = department["status"] == "Active"

            if len(code) == 2 or code == "UCALG":
                # Two letters code is a faculty
                yield Faculty(
                    code=code,
                    name=name,
                    display_name=display_name,
                    is_active=active,
                )

            else:
                if code == "MDNS" and display_name == "Clinical Neurosciences":
                    display_name = "Neuroscience Medicine"
                    name = f"{display_name}; Department of"

                #  Four letters code is a department
                yield Department(
                    code=code,
                    name=name,
                    display_name=display_name,
                    is_active=active,
                )

    def yield_additional_departments(self, response):
        # Some departments are not in the API
        # This is a list of departments that are not in the API
        # but are in the course descriptions
        faculties = [
            {
                "code": "SS",
                "name": "Faculty of Social Sciences",
                "display_name": "Faculty of Social Sciences",
            },
        ]
        departments = []

        for faculty in faculties:
            yield Faculty(
                code=faculty["code"],
                name=faculty["name"],
                display_name=faculty["display_name"],
                is_active=False,
            )

        for department in departments:
            yield Department(
                code=department["code"],
                name=department["name"],
                display_name=department["display_name"],
                is_active=False,
            )
