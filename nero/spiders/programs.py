import json
from scrapy import Spider, Request
from nero.items import Program


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
            custom_fields = program["customFields"]

            coursedog_id = program["id"]
            code = program["code"]
            name = program["name"]
            long_name = program["longName"]
            type = program["type"]
            career = program["career"]
            departments = program["departments"]
            admission_info = (
                custom_fields["programAdmissionsInfo"]
                if "programAdmissionsInfo" in custom_fields
                else None
            )
            general_info = (
                custom_fields["generalProgramInfo"]
                if "generalProgramInfo" in custom_fields
                else None
            )
            transcript_level = program["transcriptLevel"]
            transcript_description = program["transcriptDescription"]
            requisites = program["requisites"]
            version = program["version"]
            active = program["status"] == "Active"

            yield Program(
                coursedog_id=coursedog_id,
                code=code,
                name=name,
                long_name=long_name,
                type=type,
                career=career,
                departments=departments,
                admission_info=admission_info,
                general_info=general_info,
                transcript_level=transcript_level,
                transcript_description=transcript_description,
                requisites=requisites,
                version=version,
                active=active,
            )


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
