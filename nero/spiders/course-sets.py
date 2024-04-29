import json
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from collections import defaultdict
from nero.items import CourseSet


class CourseSetsSpider(Spider):
    name = "course-sets"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courseSets?skip={skip}&limit={limit}"

        for t in range(0, 99):
            url = base_url.format(skip=t * 1000, limit=1000)
            yield Request(url=url, callback=self.parse_course_sets)

    def parse_course_sets(self, response):
        print(response.url)

        data = str(response.body, encoding="utf-8")
        data = dict(json.loads(data))
        course_sets = data.values()

        for course_set in course_sets:
            yield from self.parse_course_set(defaultdict(lambda: None, course_set))

        if len(course_sets) < 1000:
            raise CloseSpider("No more courses to parse")

    def parse_course_set(self, course_set: defaultdict):
        id = course_set.get("id")

        name = str(course_set.get("name")).strip() if course_set.get("name") else None
        description = course_set.get("description")
        type = course_set.get("type")  # static or dynamic

        structure = course_set.get("structure", {})

        if type == "static":
            course_list = course_set.get("courseList", [])
        elif type == "dynamic":
            course_list = course_set.get("dynamicCourseList", [])
        else:
            raise Exception(f"Unknown course set type: {type}")

        created_at = course_set.get("createdAt")
        last_edited_at = course_set.get("lastEditedAt")

        yield CourseSet(
            id=id,
            #
            name=name,
            description=description,
            type=type,
            #
            structure=structure,
            course_list=course_list,
            #
            created_at=created_at,
            last_edited_at=last_edited_at,
        )
