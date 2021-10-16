# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseTitle(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    code = scrapy.Field()
    faculty = scrapy.Field()


class CourseInfo(scrapy.Item):
    cid = scrapy.Field(serializer=int)

    code = scrapy.Field()
    number = scrapy.Field()
    topic = scrapy.Field()

    description = scrapy.Field()
    sub_topics = scrapy.Field()

    units = scrapy.Field(serializer=float)
    credits = scrapy.Field(serializer=float)
    hours = scrapy.Field()
    time_length = scrapy.Field()

    prereq = scrapy.Field()
    coreq = scrapy.Field()
    antireq = scrapy.Field()

    notes = scrapy.Field()
    aka = scrapy.Field()

    repeat = scrapy.Field(serializer=bool)
    nogpa = scrapy.Field(serializer=bool)


class Faculty(scrapy.Item):
    fid = scrapy.Field(serializer=int)
    code = scrapy.Field()
    title = scrapy.Field()

    phones = scrapy.Field()
    rooms = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()

    aka = scrapy.Field()


class Department(scrapy.Item):
    did = scrapy.Field(serializer=int)
    code = scrapy.Field()
    title = scrapy.Field()

    phones = scrapy.Field()
    rooms = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()

    aka = scrapy.Field()
    fid = scrapy.Field(serialize=int)


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
