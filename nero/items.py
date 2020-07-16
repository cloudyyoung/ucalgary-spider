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
    pass
