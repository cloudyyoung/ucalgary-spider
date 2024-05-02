import json
from scrapy import Spider, Request
from collections import defaultdict
from nero.items import RequisiteSet
from nero.spiders.courses import convert_list_camel_to_snake


class RequisiteSetsSpider(Spider):
    name = "requisite-sets"

    def start_requests(self):
        # This endpoint does not support limit and skip
        url = "https://app.coursedog.com/api/v1/ucalgary_peoplesoft/requisite-sets"
        yield Request(url=url, callback=self.parse_requisite_sets)

    def parse_requisite_sets(self, response):
        print(response.url)

        data = str(response.body, encoding="utf-8")
        requisite_sets = list(json.loads(data))

        for course_set in requisite_sets:
            yield from self.parse_requisite_set(defaultdict(lambda: None, course_set))

    def parse_requisite_set(self, course_set: defaultdict):
        id = course_set.get("_id")
        requisite_set_group_id = course_set.get("requisiteSetGroupId")

        name = str(course_set.get("name")).strip() if course_set.get("name") else None
        description = course_set.get("description")

        requisites = self.process_requisites(course_set.get("requisites"))

        effective_start_date = course_set.get("effectiveStartDate")
        effective_end_date = course_set.get("effectiveEndDate")
        created_at = course_set.get("createdAt")
        last_edited_at = course_set.get("lastEditedAt")
        version = course_set.get("version")

        yield RequisiteSet(
            id=id,
            requisite_set_group_id=requisite_set_group_id,
            #
            name=name,
            description=description,
            #
            requisites=requisites,
            #
            effective_start_date=effective_start_date,
            effective_end_date=effective_end_date,
            created_at=created_at,
            last_edited_at=last_edited_at,
            version=version,
        )

    def process_requisites(self, requisites):
        if not requisites:
            return []

        return convert_list_camel_to_snake(requisites)
