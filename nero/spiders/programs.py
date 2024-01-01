import json
from scrapy import Spider, Request
from nero.items import Course


class ProgramsSpider(Spider):
    name = "programs"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/programs/search/$filters?catalogId=SGrVclL1qqlruuZrIFIi&skip={skip}&limit={limit}&sortBy=catalogDisplayName&effectiveDatesRange=2024-06-21,2024-06-30"

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

        for program in data:
            print(program)

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
        {
            "id": "status-course",
            "name": "status",
            "inputType": "select",
            "group": "course",
            "type": "doesNotContain",
            "value": "Inactive",
        },
    ],
}
