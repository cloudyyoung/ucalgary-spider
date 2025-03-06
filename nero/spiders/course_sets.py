import json
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from collections import defaultdict
from nero.items import CourseSet
from nero.spiders.courses import convert_dict_keys_camel_to_snake


class CourseSetsSpider(Spider):
    name = "course-sets"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courseSets?skip={skip}&limit={limit}"

        for t in range(0, 99):
            url = base_url.format(skip=t * 2000, limit=2000)
            yield Request(url=url, callback=self.parse_course_sets)

    def parse_course_sets(self, response):
        print(response.url)

        data = str(response.body, encoding="utf-8")
        data = dict(json.loads(data))
        course_sets = data.values()

        for course_set in course_sets:
            yield from self.parse_course_set(defaultdict(lambda: None, course_set))

        if len(course_sets) < 2000:
            raise CloseSpider("No more course sets to parse")

    def parse_course_set(self, course_set: defaultdict):
        id = course_set.get("id")
        course_set_group_id = course_set.get("courseSetGroupId")

        name = str(course_set.get("name", "")).strip()
        description = course_set.get("description")
        type = course_set.get("type")  # static or dynamic

        structure = self.process_structure(course_set.get("structure"))

        if type == "static":
            course_list = course_set.get("courseList", [])
        elif type == "dynamic":
            course_list = course_set.get("dynamicCourseList", [])
        else:
            raise Exception(f"Unknown course set type: {type}")

        created_at = course_set.get("createdAt")
        last_edited_at = course_set.get("lastEditedAt")

        yield CourseSet(
            csid=id,
            course_set_group_id=course_set_group_id,
            #
            type=type,
            name=name,
            description=description,
            #
            structure=structure,
            course_list=course_list,
            #
            course_set_created_at=created_at,
            course_set_last_updated_at=last_edited_at,
        )

    def process_structure(self, structure):
        if not structure:
            return {"condition": "all", "rules": []}
        return convert_dict_keys_camel_to_snake(structure)
