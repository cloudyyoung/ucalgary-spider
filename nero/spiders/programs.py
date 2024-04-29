import json
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from collections import defaultdict
from nero.items import Program


class ProgramsSpider(Spider):
    name = "programs"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/programsskip={skip}&limit={limit}&sortBy=catalogDisplayName"

        # As of April 2024,
        for t in range(0, 99):
            url = base_url.format(skip=t * 1000, limit=1000)
            yield Request(url=url, callback=self.parse_programs)

    def parse_programs(self, response):
        print(response.url)

        data = str(response.body, encoding="utf-8")
        data = dict(json.loads(data))
        programs = data.values()

        for program in programs:
            yield from self.parse_program(defaultdict(lambda: None, program))

        if len(programs) < 1000:
            raise CloseSpider("No more programs to parse")

    def parse_program(self, program: defaultdict):
        custom_fields = defaultdict(lambda: None, program.get("customFields", {}))

        coursedog_id = program.get("id")
        program_group_id = program.get("programGroupId")

        code = program.get("code")
        name = program.get("name")
        long_name = program.get("longName")
        display_name = program.get("catalogDisplayName")

        type = program.get("type")  # MAJ, MIN, etc
        degree_designation_code, degree_designation_name = (
            self.process_degree_designation(program.get("degreeDesignation"))
        )  # Eg, "BSC-H - Bachelor of Science (Honours)""
        career = program.get("career")
        departments = program.get("departments", [])
        
        admission_info = custom_fields.get("programAdmissionsInfo")
        general_info = custom_fields.get("generalProgramInfo")

        transcript_level = program.get("transcriptLevel")
        transcript_description = program.get("transcriptDescription")

        requisites = program.get("requisites", {})

        active = program["status"] == "Active"
        start_term = self.process_start_term(program.get("startTerm"))

        created_at = program.get("createdAt")
        last_edited_at = program.get("lastEditedAt")
        effective_start_date = program.get("effectiveStartDate")
        effective_end_date = program.get("effectiveEndDate")
        version = program.get("version")

        yield Program(
            coursedog_id=coursedog_id,
            program_group_id=program_group_id,

            code=code,
            name=name,
            long_name=long_name,
            display_name=display_name,

            type=type,
            degree_designation_code=degree_designation_code,
            degree_designation_name=degree_designation_name,
            career=career,
            departments=departments,

            admission_info=admission_info,
            general_info=general_info,

            transcript_level=transcript_level,
            transcript_description=transcript_description,

            requisites=requisites,

            active=active,
            start_term=start_term,

            created_at=created_at,
            last_edited_at=last_edited_at,
            effective_start_date=effective_start_date,
            effective_end_date=effective_end_date,
            version=version,
        )

    def process_degree_designation(self, designation: str):
        if not designation:
            return None

        if " - " not in designation:
            return None

        designation_code, designation_name = designation.split(" - ")
        return designation_code, designation_name

    def process_start_term(self, start_term):
        if not start_term:
            return None

        id = start_term["id"]
        year = start_term["year"]
        term = str(start_term["semester"])
        return {
            "id": id,
            "year": year,
            "term": term,
        }


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
