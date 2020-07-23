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
    credits = scrapy.Field(serializer=int)
    hours = scrapy.Field()
    time_length = scrapy.Field()

    prereq = scrapy.Field()
    coreq = scrapy.Field()
    antireq = scrapy.Field()

    notes = scrapy.Field()
    aka = scrapy.Field()

    repeat = scrapy.Field(serializer=bool)
    nogpa = scrapy.Field(serializer=bool)
