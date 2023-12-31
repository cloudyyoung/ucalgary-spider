import json
from scrapy import Spider, Request
from nero.items import CourseInfo


class QuotesSpider(Spider):
    name = "course-info"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses/search/$filters?catalogId=SGrVclL1qqlruuZrIFIi&skip={skip}&limit={limit}&orderBy=code&formatDependents=true&effectiveDatesRange=2024-06-21,2024-06-30"

        url = base_url.format(skip=0, limit=999)
        print(url)

        yield Request(
            url=url,
            callback=self.parse,
            method="POST",
            body=json.dumps(REQUEST_BODY),
            headers={"Content-Type": "application/json"},
        )

    def parse(self, response):
        body = str(response.body, encoding="utf-8")
        body = json.loads(body)
        data = body["data"]

        for course in data:
            cid = course["customFields"]["rawCourseId"]
            coursedog_id = course["id"]
            code = course["subjectCode"]
            number = float(course["courseNumber"])
            name = course["name"]
            long_name = course["longName"]
            description = course["description"]
            credits = float(course["credits"]["numberOfCredits"])
            grade_mode = course["gradeMode"]
            nogpa = NOGPA_TEXT.upper() in description.upper()
            repeatable = bool(course["credits"]["repeatable"])
            active = course["status"] == "Active"
            departments = course["departments"]

            yield CourseInfo(
                cid=cid,
                coursedog_id=coursedog_id,
                code=code,
                number=number,
                name=name,
                long_name=long_name,
                departments=departments,
                units=credits,
                credits=credits,
                grade_mode=grade_mode,
                description=description,
                prereq=None,
                coreq=None,
                antireq=None,
                notes=None,
                aka=None,
                repeatable=repeatable,
                nogpa=nogpa,
                active=active,
            )


NOGPA_TEXT = "Not included in GPA"
REQUEST_BODY = {
    "condition": "and",
    "filters": [
        {
            "id": "courseNumber-course",
            "name": "courseNumber",
            "inputType": "text",
            "group": "course",
            "type": "doesNotContain",
            "value": "A",
        },
        {
            "id": "courseNumber-course",
            "name": "courseNumber",
            "inputType": "text",
            "group": "course",
            "type": "doesNotContain",
            "value": "B",
        },
        # {
        #     "id": "status-course",
        #     "name": "status",
        #     "inputType": "select",
        #     "group": "course",
        #     "type": "doesNotContain",
        #     "value": "Inactive",
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150073",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "160740",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "160726",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "161071",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "103199",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "customField": True,
        #     "value": "150054",
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150087",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150135",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150178",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150211",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150243",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150250",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "161388",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150345",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150382",
        #     "customField": True,
        # },
        # {
        #     "id": "rawCourseId-course",
        #     "name": "rawCourseId",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "isNot",
        #     "value": "150390",
        #     "customField": True,
        # },
        {
            "group": "course",
            "id": "subjectCode-course",
            "inputType": "subjectCodeSelect",
            "name": "subjectCode",
            "type": "is",
            "value": "CPSC",
        },
    ],
}
