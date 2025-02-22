import json
import re
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from collections import defaultdict
from nero.items import Course


class CoursesSpider(Spider):
    name = "courses"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses?skip={skip}&limit={limit}"

        # As of April 2024, approaximately 45 pages
        for t in range(0, 99):
            url = base_url.format(skip=t * 2000, limit=2000)
            yield Request(url=url, callback=self.parse_courses)

    def parse_courses(self, response):
        print(response.url)

        data = str(response.body, encoding="utf-8")
        data = dict(json.loads(data))
        courses = data.values()

        for course in courses:
            yield from self.parse_course(defaultdict(lambda: None, course))

        if len(courses) < 2000:
            raise CloseSpider("No more courses to parse")

    def parse_course(self, course: defaultdict):
        custom_fields = defaultdict(lambda: None, course.get("customFields", {}))
        credits_fields = defaultdict(lambda: None, course.get("credits", {}))

        coursedog_id = course.get("id")
        course_id = custom_fields.get("rawCourseId")
        course_group_id = course.get("courseGroupId")

        code = course.get("code")  # CPSC 413
        subject_code = course.get("subjectCode")  # CPSC
        course_number = course.get("courseNumber")  # 413, 502.06, etc

        name = course.get("name")  # Topic
        long_name = course.get("longName")

        topics = self.process_topics(course.get("topics", []))

        faculty_code, faculty_name = self.process_faculty(course.get("college"))
        departments = filter_departments(course.get("departments", []))
        career = career_serializer(course.get("career", ""))

        description_full = course.get("description")
        description, prereq, coreq, antireq, notes, aka, nogpa = (
            self.process_description(description_full)
        )

        requisites = self.process_requisites(course.get("requisites"))

        credits_raw = credits_fields.get("numberOfCredits")
        units = float(credits_raw) if credits_raw else None
        grade_mode_code, grade_mode_name = self.process_grade_mode(
            course.get("gradeMode")
        )

        components = list(
            map(lambda c: component_serializer(c["code"]), course.get("components", []))
        )
        multi_term = bool(custom_fields.get("lastMultiTermCourse"))

        # If grade mode is null but multi_term is true, then set grade_mode to MTG
        if not grade_mode_code and multi_term:
            grade_mode_code = "MTG"
        elif not grade_mode_code:
            grade_mode_code = "GRD"

        repeatable = bool(credits_fields.get("repeatable"))
        active = course.get("status") == "Active"
        start_term = self.process_start_term(course.get("startTerm"))

        created_at = course.get("createdAt")
        last_edited_at = course.get("lastEditedAt")
        effective_start_date = course.get("effectiveStartDate")
        effective_end_date = course.get("effectiveEndDate")
        version = course.get("version")

        yield Course(
            cid=course_group_id,  # course_group_id is more accurate, so swap it with cid
            code=code,
            course_number=course_number,
            #
            subject_code=subject_code,
            #
            description=description,
            name=name,
            long_name=long_name,
            notes=notes,
            version=version,
            units=units,
            aka=aka,
            #
            prereq=prereq,
            coreq=coreq,
            antireq=antireq,
            #
            is_active=active,
            is_multi_term=multi_term,
            is_nogpa=nogpa,
            is_repeatable=repeatable,
            #
            components=components,
            course_group_id=course_id,
            coursedog_id=coursedog_id,
            #
            course_created_at=created_at,
            course_last_updated_at=last_edited_at,
            course_effective_start_date=effective_start_date,
            course_effective_end_date=effective_end_date,
            #
            departments=departments,
            faculties=[faculty_code] if faculty_code else [],
            #
            career=career,
            topics=topics,
            grade_mode=grade_mode_code,
        )

    def process_description(self, description_full: str | None):
        description, prereq, coreq, antireq, notes, aka, nogpa = (
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        )

        if description_full:
            description_full = description_full.replace("\n", "\n\n")
            (description, *more) = description_full.split("\n\n")

            for t in more:
                if t.startswith(PREREQ_TEXT):
                    prereq = t.replace(PREREQ_TEXT, "").strip()

                elif t.startswith(COREQ_TEXT):
                    coreq = t.replace(COREQ_TEXT, "").strip()

                elif t.startswith(ANTIREQ_TEXT):
                    antireq = t.replace(ANTIREQ_TEXT, "").strip()

                elif t.startswith(NOTES_TEXT) or t.startswith(NOTES_TEXT_ALT):
                    notes = (
                        t.replace(NOTES_TEXT, "").replace(NOTES_TEXT_ALT, "").strip()
                    )

                elif t.startswith(AKA_TEXT):
                    aka = t.replace(AKA_TEXT, "").strip()

            nogpa = NOGPA_TEXT.upper() in description_full.upper()

        return (description, prereq, coreq, antireq, notes, aka, nogpa)

    def process_faculty(self, faculty: str | None):
        if not faculty:
            return (None, None)

        if " - " not in faculty:
            return (None, faculty)

        code, full_name = faculty.split(" - ")
        return (code, full_name)

    def process_topics(self, _topics: list):
        topics = []
        for _topic in _topics:
            topic = {
                # "id": _topic["id"],
                # "code": _topic["code"],
                "number": _topic["code"],
                "name": _topic["name"],
                "long_name": _topic["longName"],
                "description": _topic["description"],
                "is_repeatable": bool(_topic["repeatable"]),
                "units": _topic["numberOfCredits"],
                "link": _topic["link"],
            }
            topics.append(topic)
        return topics

    def process_start_term(self, start_term: dict | None):
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

    def process_grade_mode(self, grade_mode: str | None):
        if not grade_mode:
            return (None, None)

        if " - " not in grade_mode:
            return (None, grade_mode)

        grade_mode_code, grade_mode_name = grade_mode.split(" - ")
        return grade_mode_code, grade_mode_name

    def process_requisites(self, requisites: dict | None):
        if not requisites or "requisitesSimple" not in requisites:
            return []

        requisites_simple = requisites["requisitesSimple"]
        return convert_list_camel_to_snake(requisites_simple)


def convert_dict_keys_camel_to_snake(d: dict):
    e = {re.sub(r"(?<!^)(?=[A-Z])", "_", k).lower(): v for k, v in d.items()}

    for k, v in e.items():
        if isinstance(v, dict):
            e[k] = convert_dict_keys_camel_to_snake(v)
        elif isinstance(v, list):
            e[k] = convert_list_camel_to_snake(v)

    return e


def convert_list_camel_to_snake(a: list):
    return [
        convert_dict_keys_camel_to_snake(i) if isinstance(i, dict) else i for i in a
    ]


def component_serializer(component_abbr: str):
    if component_abbr == "LEC":
        return "LECTURE"
    elif component_abbr == "TUT":
        return "TUTORIAL"
    elif component_abbr == "LAB":
        return "LAB"
    elif component_abbr == "SEM":
        return "SEMINAR"
    elif component_abbr == "SEC":
        return "SECTION"
    raise ValueError(f"Unknown component abbreviation: {component_abbr}")


def career_serializer(career: str):
    if career == "Undergraduate Programs":
        return "UNDERGRADUATE_PROGRAM"
    elif career == "Graduate Programs":
        return "GRADUATE_PROGRAM"
    elif career == "Medicine Programs":
        return "MEDICINE_PROGRAM"


def filter_departments(departments: list):
    departments = [d for d in departments if len(d) > 2]

    # if it contains ANTH (Anthropology) or ARKY (Archaeology), then replace with ANAR (Anthropology and Archaeology)
    departments = [d.replace("ANTH", "ANAR") for d in departments]
    departments = [d.replace("ARKY", "ANAR") for d in departments]

    return departments


PREREQ_TEXT = "Prerequisite(s): "
COREQ_TEXT = "Corequisite(s): "
ANTIREQ_TEXT = "Antirequisite(s): "
NOTES_TEXT = "Notes: "
NOTES_TEXT_ALT = "NOte: "
NOGPA_TEXT = "Not included in GPA"
AKA_TEXT = "Also known as: "
