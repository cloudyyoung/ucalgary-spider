import json
from scrapy import Spider, Request
from nero.items import Course


class CoursesSpider(Spider):
    name = "courses"

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
            number = course["courseNumber"]
            name = course["name"]
            long_name = course["longName"]

            faculty = course["college"]
            departments = course["departments"]
            career = course["career"]

            description_full = course["description"]
            description, prereq, coreq, antireq, notes, aka = self.process_description(
                description_full
            )

            credits = float(course["credits"]["numberOfCredits"])
            grade_mode = course["gradeMode"]
            components = list(map(lambda c: c["code"], course["components"]))

            nogpa = NOGPA_TEXT.upper() in description_full.upper()
            repeatable = bool(course["credits"]["repeatable"])
            active = course["status"] == "Active"

            yield Course(
                cid=cid,
                coursedog_id=coursedog_id,
                code=code,
                number=number,
                name=name,
                long_name=long_name,
                faculty=faculty,
                departments=departments,
                career=career,
                units=credits,
                credits=credits,
                grade_mode=grade_mode,
                components=components,
                description=description,
                prereq=prereq,
                coreq=coreq,
                antireq=antireq,
                notes=notes,
                aka=aka,
                repeatable=repeatable,
                nogpa=nogpa,
                active=active,
            )

    def process_description(self, description_full):
        description_full = description_full.replace("\n", "\n\n")
        (description, *more) = description_full.split("\n\n")

        prereq, coreq, antireq, notes, aka = None, None, None, None, None

        for t in more:
            if t.startswith(PREREQ_TEXT):
                prereq = t.replace(PREREQ_TEXT, "").strip()

            elif t.startswith(COREQ_TEXT):
                coreq = t.replace(COREQ_TEXT, "").strip()

            elif t.startswith(ANTIREQ_TEXT):
                antireq = t.replace(ANTIREQ_TEXT, "").strip()

            elif t.startswith(NOTES_TEXT) or t.startswith(NOTES_TEXT_ALT):
                notes = t.replace(NOTES_TEXT, "").replace(NOTES_TEXT_ALT, "").strip()

            elif t.startswith(AKA_TEXT):
                aka = t.replace(AKA_TEXT, "").strip()

        return (description, prereq, coreq, antireq, notes, aka)


PREREQ_TEXT = "Prerequisite(s): "
COREQ_TEXT = "Corequisite(s): "
ANTIREQ_TEXT = "Antirequisite(s): "
NOTES_TEXT = "Notes: "
NOTES_TEXT_ALT = "NOte: "
NOGPA_TEXT = "Not included in GPA"
AKA_TEXT = "Also known as: "
REQUEST_BODY = {
    "condition": "and",
    "filters": [
        # {
        #     "id": "courseNumber-course",
        #     "name": "courseNumber",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "doesNotContain",
        #     "value": "A",
        # },
        # {
        #     "id": "courseNumber-course",
        #     "name": "courseNumber",
        #     "inputType": "text",
        #     "group": "course",
        #     "type": "doesNotContain",
        #     "value": "B",
        # },
        {
            "id": "status-course",
            "name": "status",
            "inputType": "select",
            "group": "course",
            "type": "doesNotContain",
            "value": "Inactive",
        },
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
        {
            "group": "course",
            "id": "career-course",
            "inputType": "careerSelect",
            "name": "career",
            "type": "is",
            "value": "Undergraduate Programs",
        },
    ],
}
