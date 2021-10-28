# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json
import re
from itemadapter import ItemAdapter
from bs4 import BeautifulSoup
from nero.items import CourseInfo, CourseRequisite


class FileStorePipeline:
    files = {}

    def file_name_convert(self, item_type):
        return str(re.sub(r"([a-z])([A-Z])", r"\1-\2", item_type)).lower()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        for file in self.files.values():
            file.close()

    def process_item(self, item, spider):
        item_type = item.__class__.__name__
        if(item_type not in self.files.keys()):
            file_object = open("data/" + self.file_name_convert(item_type) + ".jsonlines", 'w')
            self.files[item_type] = file_object
        else:
            line = json.dumps(ItemAdapter(item).asdict()) + "\n"
            self.files[item_type].write(line)

        return item


class CourseRequisitesPipeline:
    def prereq_single_course(self, string):
        return string

    def prereq_x_units_from(self, string):
        x = re.match(self.regex_x_units_from, string)
        units_text = x.group(1).strip()
        courses_text = x.group(2).strip()

        y = re.match(self.regex_x_units_from_courses_labelled_at, courses_text)
        z = re.match(self.regex_x_units_from_courses_labelled_at_including, courses_text)

        if(z):
            # courses labelled ART at the 300 level, including ...
            code = z.group(1).strip()
            number = z.group(2).strip()
            including = z.group(3).strip()

            return {"units": int(units_text), "from": f"${code} ${number}+", "including": self.prereq(including)}
        elif (y):
            # courses labelled ARST at the 300 level or above
            code = y.group(1).strip()
            number = y.group(2).strip()

            return {"units": int(units_text), "from": f"${code} ${number}+"}
        else:
            courses = []
            last_code = ""

            # Split `from` text into several pieces of courses
            _courses = re.split(',|or', courses_text)
            for _course in _courses:
                _course = _course.strip()
                x = re.match(self.regex_complete_course, _course)
                y = re.match(self.regex_incomplete_course, _course)

                code, key, course_title = "", "", ""

                # If the course name is complete `Arts 241`, or incomplete `241`
                if(x):
                    code = last_code = x.group(1)
                    key = x.group(2)
                elif(y):
                    code = last_code
                    key = y.group(1)

                # Trim spaces
                code, key, course_title = code.strip(), key.strip(), course_title.strip()

                course_title = code + " " + key
                courses.append(course_title)

            if(courses == []):
                print("UNHANDLED PATTERN - X UNITS FROM []: " + string)
                return string

            return {"units": int(units_text), "from": courses}

    def prereq_consent_of_the(self, string):
        m = re.match(self.regex_consent_of_the, string)

        if(m):
            return {"consent": m.group(1).strip()}
        else:
            print("UNHANDLED PATTERN - CONSENT OF: " + string)
            return string

    def prereq_or_courses(self, string):
        m = re.match(self.regex_or_courses_full_incomplete, string)
        n = re.match(self.regex_or_courses_full_full, string)

        if(m):  # full_incomplete: ANTH 391 or 490
            code1, number1, code2, number2 = m.group(1), m.group(2), m.group(1), m.group(3)
        elif(n):  # full_full: ARCH 201 or ARST 201
            code1, number1, code2, number2 = n.group(1), n.group(2), n.group(3), n.group(4)
        else:
            print("UNHANDLED PATTERN - OR: " + string)
            return string

        # Trim spaces
        code1, number1, code2, number2 = code1.strip(), number1.strip(), code2.strip(), number2.strip()
        return [code1 + " " + number1, code2 + " " + number2]

    # CourseTitle, for replacing full course names with short course codes
    course_titles = {}

    # Regex string
    regex_incomplete_course = r"([0-9]{3})"
    regex_complete_course = r"([A-Z]{3,4}) ([0-9]{3})"
    regex_x_units_from = r"^([0-9]{1,2}) units (?:from|in|of) (.*)$"
    regex_x_units_from_courses_labelled_at = r"courses labelled ([A-Z]{3,4}) at the ([0-9]{3}) level(?: or above)$"
    regex_x_units_from_courses_labelled_at_including = r"courses labelled ([A-Z]{3,4}) at the ([0-9]{3}) level(?:,) including ([0-9]{1,2}) units from (.*)"
    regex_consent_of_the = r"^[Cc]onsent of the ([A-z ,-]*)$"
    regex_or_courses_full_incomplete = r"^([A-Z]{3,4}) ([0-9]{3}) or ([0-9]{3})$"
    regex_or_courses_full_full = r"^([A-Z]{3,4}) ([0-9]{3}) or ([A-Z]{3,4}) ([0-9]{3})$"
    regex_single_course = r"^([A-Z]{3,4}) ([0-9]{3})$"

    # All regex and its matching handle function
    # Tests on regex101.com
    patterns = {
        regex_x_units_from: prereq_x_units_from,
        regex_x_units_from_courses_labelled_at: prereq_x_units_from,
        regex_x_units_from_courses_labelled_at_including: prereq_x_units_from,
        regex_consent_of_the: prereq_consent_of_the,
        regex_or_courses_full_incomplete: prereq_or_courses,
        regex_or_courses_full_full: prereq_or_courses,
        regex_single_course: prereq_single_course,
    }

    def open_spider(self, spider):
        # Read all the course titles from past years
        title_year_file = open("data/course-title-year.jsonlines", "r")
        for line in title_year_file:
            course_title = json.loads(line)
            title = course_title["title"]
            code = course_title["code"]
            self.course_titles[title] = code
        title_year_file.close()

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if(isinstance(item, CourseRequisite)):
            item["prereq"] = self.prereq(item["prereq"])
        return item

    def prereq(self, prereq_text):
        # If no prereq, return nothing
        if(prereq_text == None):
            return None

        # Remove all the html tags in requisites
        soup = BeautifulSoup(str(prereq_text), 'html.parser')
        prereq_text = str(soup.get_text())

        # Trim trailing period
        prereq_text = prereq_text.rstrip('.')

        # Replace all full names with short codes, from the names longest to shortest
        for full_name in sorted(self.course_titles.keys(), key=len, reverse=True):
            code = self.course_titles[full_name]
            prereq_text = re.sub(full_name + r" ([0-9]{3})", code + r" \1", prereq_text)
            prereq_text = re.sub(r"labelled " + full_name, r"labelled " + code, prereq_text)

        prereq = []

        # Split requisites into several and conditions
        _ands = prereq_text.split(";")
        for _and in _ands:
            _and = str(_and).strip()
            handled = False

            # Match for a specific pattern for this and condition
            for regex in self.patterns.keys():

                # If found, pass in the and conditition to associated regex function
                if (re.search(regex, _and)):
                    prereq.append(self.patterns[regex](self, _and.strip()))
                    handled = True
                    break

            # Unhandled, add raw text
            if(not handled):
                prereq.append(_and)

        print(prereq_text, "->", prereq)
        return prereq
