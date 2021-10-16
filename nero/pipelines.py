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
    # CourseTitle, for replacing full course names with short course codes
    course_titles = {}

    def __init__(self):
        # Read all the course titles from past years
        title_year_file = open("data/course-title-year.jsonlines", "r")
        for line in title_year_file:
            course_title = json.loads(line)
            title = course_title["title"]
            code = course_title["code"]
            self.course_titles[title] = code
        title_year_file.close()

    def prereq_single_course(self, string):
        return string

    def prereq_x_units_from(self, string):
        m = re.match(self.regex_x_units_from, string)
        units_text = m.group(0)
        courses_text = m.group(1)

        courses = []
        last_code = ""

        _courses = re.split(',|or', courses_text)
        for _course in _courses:
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
            if(course_title == _courses):
                courses.append(course_title)
            else:
                courses.append(_course)  # Has to deal with this new pattern
                print("UNHANDLED PATTERN: " + _course)

        if(courses == []):
            print("UNHANDLED PATTERN: " + string)
            return string

        return {"units": int(units_text), "courses": courses}

    def prereq_consent_of_the(self, string):
        m = re.match(self.regex_consent_of_the, string)

        if(m):
            return {"consent": m.group(1).strip()}
        else:
            print("UNHANDLED PATTERN: " + string)
            return string

    def prereq_or(self, string):
        m = re.match(self.regex_or, string)
        if(m):
            code1, number1, code2, number2 = m.group(1), m.group(2), None, None

            code_or_number = m.group(3)
            if(re.match(self.regex_incomplete_course, code_or_number)):
                # This is a number
                code2 = code1
                number2 = m.group(3)
            else:
                code2 = m.group(3)
                number2 = m.group(4)

            # Trim spaces
            code1, number1, code2, number2 = code1.strip(), number1.strip(), code2.strip(), number2.strip()
            return [code1 + " " + number1, code2 + " " + number2]
        else:
            print("UNHANDLED PATTERN: " + string)
            return string

    # Regex string
    regex_incomplete_course = r"([0-9]{3})"
    regex_complete_course = r"([A-Z]{3,4}) ([0-9]{3})"
    regex_x_units_from = r"([0-9]) units from (.*)"
    regex_consent_of_the = r"Consent of the ([A-z ]*)"
    regex_or = r"([A-Z]{3,4}) ([0-9]{3}) or ([A-Z]{3,4})? ?([0-9]{3})"
    regex_single_course = r"([A-Z]{3,4}) ([0-9]{3})$"

    # All regex and its matching handle function
    # Tests on regex101.com
    patterns = {
        regex_x_units_from: prereq_x_units_from,
        regex_consent_of_the: prereq_consent_of_the,
        regex_or: prereq_or,
        regex_single_course: prereq_single_course,
    }

    def open_spider(self, spider):
        self.file = open("data/course-requisites.jsonlines", 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if(isinstance(item, CourseInfo)):
            course_requisite_obj = CourseRequisite(cid=item["cid"],
                                                   code=item["code"],
                                                   number=item["number"],
                                                   prereq=self.prereq(item['prereq']))

            line = json.dumps(ItemAdapter(course_requisite_obj).asdict()) + "\n"
            self.file.write(line)
            self.file.flush()

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
            prereq_text = re.sub(full_name, code, prereq_text)

        prereq = [prereq_text]

        # Split requisites into several and conditions
        _ands = prereq_text.split(";")
        if(len(_ands) == 1):  # If the requisite is not combined `x;y;z` but `x and y`.
            _ands = prereq_text.split("and")

        # For each and condition
        for _and in _ands:
            _and = str(_and).strip()

            # Match for a specific pattern for this and condition
            for regex in self.patterns.keys():

                # If found, pass in the and conditition to associated regex function
                if (re.search(regex, _and)):
                    prereq.append(self.patterns[regex](self, _and))
                    break

        # print(_prereq, prereq)
        return prereq
