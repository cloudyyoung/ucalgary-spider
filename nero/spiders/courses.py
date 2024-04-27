import json
from scrapy import Spider, Request
from nero.items import Course


class CoursesSpider(Spider):
    name = "courses"

    def start_requests(self):
        base_url = "https://app.coursedog.com/api/v1/cm/ucalgary_peoplesoft/courses?skip={skip}&limit={limit}"

        for t in range(0, 20):
            url = base_url.format(skip=t * 1000, limit=1000)
            yield Request(url=url, callback=self.parse_courses)

    def parse_courses(self, response):
        print(response.url)

        courses = str(response.body, encoding="utf-8")
        courses = dict(json.loads(courses))

        for course in courses.values():
            yield from self.parse_course(course)

    def parse_course(self, course):
        coursedog_id = course["id"]
        cid = course["customFields"]["rawCourseId"]
        course_group_id = course["courseGroupId"]

        code = course["code"]  # CPSC 413
        subject_code = course["subjectCode"]  # CPSC
        course_number = course["courseNumber"]  # 413

        name = course["name"]  # Topic
        long_name = course["longName"]

        topics = self.process_topics(course["topics"])

        faculty_code, faculty_name = self.process_faculty(course["college"])
        departments = course["departments"]
        department_ownership = course.get("departmentOwnership", {})
        career = course["career"]  # Undergraduate / Graduate Programs

        description_full = course["description"]
        description, prereq, coreq, antireq, notes, aka = self.process_description(
            description_full
        )

        requisites = course["requisites"]

        credits = float(course["credits"]["numberOfCredits"])
        grade_mode = course["gradeMode"]
        components = list(map(lambda c: c["code"], course["components"]))

        nogpa = NOGPA_TEXT.upper() in description_full.upper()
        repeatable = bool(course["credits"]["repeatable"])
        active = course["status"] == "Active"

        start_term = course["startTerm"]

        created_at = course["createdAt"]
        last_edited_at = course["lastEditedAt"]
        effective_start_date = course["effectiveStartDate"]
        effective_end_date = course["effectiveEndDate"]
        version = course["version"]

        yield Course(
            coursedog_id=coursedog_id,
            cid=cid,
            course_group_id=course_group_id,
            code=code,
            subject_code=subject_code,
            course_number=course_number,
            name=name,
            long_name=long_name,
            topics=topics,
            faculty_code=faculty_code,
            faculty_name=faculty_name,
            departments=departments,
            department_ownership=department_ownership,
            career=career,
            description=description,
            prereq=prereq,
            coreq=coreq,
            antireq=antireq,
            notes=notes,
            aka=aka,
            requisites=requisites,
            credits=credits,
            grade_mode=grade_mode,
            components=components,
            nogpa=nogpa,
            repeatable=repeatable,
            active=active,
            start_term=start_term,
            created_at=created_at,
            last_edited_at=last_edited_at,
            effective_start_date=effective_start_date,
            effective_end_date=effective_end_date,
            version=version,
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

    def process_faculty(self, faculty):
        if not faculty:
            return (None, None)

        if " - " not in faculty:
            return (None, faculty)

        code, full_name = faculty.split(" - ")
        return (code, full_name)

    def process_topics(self, _topics):
        topics = []
        for _topic in _topics:
            topic = {
                "id": _topic["id"],
                "code": _topic["code"],
                "name": _topic["name"],
                "long_name": _topic["longName"],
                "description": _topic["description"],
                "repeatable": _topic["repeatable"],
                "repeatable": bool(_topic["repeatable"]),
                "credits": _topic["numberOfCredits"],
                "link": _topic["link"],
            }
            topics.append(topic)
        return topics


PREREQ_TEXT = "Prerequisite(s): "
COREQ_TEXT = "Corequisite(s): "
ANTIREQ_TEXT = "Antirequisite(s): "
NOTES_TEXT = "Notes: "
NOTES_TEXT_ALT = "NOte: "
NOGPA_TEXT = "Not included in GPA"
AKA_TEXT = "Also known as: "
