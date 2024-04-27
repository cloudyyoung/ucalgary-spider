# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json


class SubjectCode(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()


class Course(scrapy.Item):
    coursedog_id = scrapy.Field()
    cid = scrapy.Field()
    course_group_id = scrapy.Field()
    code = scrapy.Field()
    subject_code = scrapy.Field()
    course_number = scrapy.Field()
    name = scrapy.Field()
    long_name = scrapy.Field()
    topics = scrapy.Field(serializer=list)
    faculty_code = scrapy.Field()
    faculty_name = scrapy.Field()
    departments = scrapy.Field(serializer=list)
    department_ownership = scrapy.Field(seerializer=json.dumps)
    career = scrapy.Field()
    description = scrapy.Field()
    prereq = scrapy.Field()
    coreq = scrapy.Field()
    antireq = scrapy.Field()
    notes = scrapy.Field()
    aka = scrapy.Field()
    requisites = scrapy.Field(seerializer=json.dumps)
    credits = scrapy.Field()
    grade_mode = scrapy.Field()
    components = scrapy.Field(serializer=list)
    nogpa = scrapy.Field()
    repeatable = scrapy.Field()
    active = scrapy.Field(serializer=bool)
    start_term = scrapy.Field()
    created_at = scrapy.Field()
    last_edited_at = scrapy.Field()
    effective_start_date = scrapy.Field()
    effective_end_date = scrapy.Field()
    version = scrapy.Field()


class Faculty(scrapy.Item):
    id = scrapy.Field()

    name = scrapy.Field()
    display_name = scrapy.Field()
    active = scrapy.Field(serializer=bool)


class Department(scrapy.Item):
    id = scrapy.Field()

    name = scrapy.Field()
    display_name = scrapy.Field()
    active = scrapy.Field(serializer=bool)


class Program(scrapy.Item):
    coursedog_id = scrapy.Field()

    code = scrapy.Field()
    name = scrapy.Field()
    long_name = scrapy.Field()
    display_name = scrapy.Field()

    type = scrapy.Field()
    degree_designation = scrapy.Field()
    career = scrapy.Field()
    departments = scrapy.Field(serializer=list)

    admission_info = scrapy.Field()
    general_info = scrapy.Field()
    transcript_level = scrapy.Field(serializer=int)
    transcript_description = scrapy.Field()

    requisites = scrapy.Field(serializer=json.dumps)

    version = scrapy.Field(serializer=int)
    active = scrapy.Field(serializer=bool)


class Staff(scrapy.Item):
    sid = scrapy.Field(serialize=int)
    name = scrapy.Field()
    directory_id = scrapy.Field()

    title = scrapy.Field()
    room = scrapy.Field()
    phone = scrapy.Field()

    did = scrapy.Field(serialize=int)


class Section(scrapy.Item):
    key = scrapy.Field()  # Course key
    topic = scrapy.Field()

    year = scrapy.Field(serialize=int)
    term = scrapy.Field()

    name = scrapy.Field()
    time = scrapy.Field()
    room = scrapy.Field()

    sid = scrapy.Field(serialize=int)
    directory_id = scrapy.Field()

    note = scrapy.Field()
