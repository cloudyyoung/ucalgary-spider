# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json


class CourseCode(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()
    faculty = scrapy.Field()
    year = scrapy.Field()


class Course(scrapy.Item):
    cid = scrapy.Field(serializer=int)
    coursedog_id = scrapy.Field(serializer=int)

    code = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    long_name = scrapy.Field()

    faculty = scrapy.Field()
    departments = scrapy.Field(serializer=list)
    career = scrapy.Field()

    units = scrapy.Field(serializer=float)
    credits = scrapy.Field(serializer=float)
    grade_mode = scrapy.Field()
    components = scrapy.Field(serializer=list)

    description = scrapy.Field()
    prereq = scrapy.Field()
    coreq = scrapy.Field()
    antireq = scrapy.Field()

    notes = scrapy.Field()
    aka = scrapy.Field()

    repeatable = scrapy.Field(serializer=bool)
    nogpa = scrapy.Field(serializer=bool)
    active = scrapy.Field(serializer=bool)


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
