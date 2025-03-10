# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Subject(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()


class Course(scrapy.Item):
    cid = scrapy.Field()
    code = scrapy.Field()
    course_number = scrapy.Field()

    subject_code = scrapy.Field()

    description = scrapy.Field()
    name = scrapy.Field()
    long_name = scrapy.Field()
    notes = scrapy.Field()
    version = scrapy.Field(serializer=int)
    units = scrapy.Field(serializer=int)
    aka = scrapy.Field()

    prereq = scrapy.Field()
    coreq = scrapy.Field()
    antireq = scrapy.Field()

    is_active = scrapy.Field(serializer=bool)
    is_multi_term = scrapy.Field(serializer=bool)
    is_nogpa = scrapy.Field(serializer=bool)
    is_repeatable = scrapy.Field(serializer=bool)

    components = scrapy.Field(serializer=int)
    course_group_id = scrapy.Field()
    coursedog_id = scrapy.Field()

    course_created_at = scrapy.Field()
    course_last_updated_at = scrapy.Field()
    course_effective_start_date = scrapy.Field()
    course_effective_end_date = scrapy.Field()

    departments = scrapy.Field(serializer=list)
    faculties = scrapy.Field(serializer=list)

    career = scrapy.Field()
    topics = scrapy.Field(serializer=list)
    grade_mode = scrapy.Field()


class Faculty(scrapy.Item):
    __collection_name__ = "faculties"

    name = scrapy.Field()
    display_name = scrapy.Field()
    code = scrapy.Field()
    is_active = scrapy.Field(serializer=bool)


class Department(scrapy.Item):
    name = scrapy.Field()
    display_name = scrapy.Field()
    code = scrapy.Field()
    is_active = scrapy.Field(serializer=bool)


class Program(scrapy.Item):
    pid = scrapy.Field()
    coursedog_id = scrapy.Field()
    program_group_id = scrapy.Field()

    code = scrapy.Field()
    name = scrapy.Field()
    long_name = scrapy.Field()
    display_name = scrapy.Field()

    type = scrapy.Field()
    degree_designation_code = scrapy.Field()
    degree_designation_name = scrapy.Field()
    career = scrapy.Field()
    departments = scrapy.Field(serializer=list)
    faculties = scrapy.Field(serializer=list)

    admission_info = scrapy.Field()
    general_info = scrapy.Field()

    transcript_level = scrapy.Field(serializer=int)
    transcript_description = scrapy.Field()

    requisites = scrapy.Field(serializer=list)

    is_active = scrapy.Field(serializer=bool)
    start_term = scrapy.Field()

    program_created_at = scrapy.Field()
    program_last_updated_at = scrapy.Field()
    program_effective_start_date = scrapy.Field()
    program_effective_end_date = scrapy.Field()
    version = scrapy.Field(serializer=int)


class CourseSet(scrapy.Item):
    __collection_name__ = "course-sets"

    csid = scrapy.Field()
    course_set_group_id = scrapy.Field()

    type = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()

    structure = scrapy.Field(serializer=dict)
    course_list = scrapy.Field(serializer=list)

    course_set_created_at = scrapy.Field()
    course_set_last_updated_at = scrapy.Field()


class RequisiteSet(scrapy.Item):
    __collection_name__ = "requisite-sets"

    id = scrapy.Field()
    requisite_set_group_id = scrapy.Field()

    name = scrapy.Field()
    description = scrapy.Field()

    requisites = scrapy.Field(serializer=list)

    effective_start_date = scrapy.Field()
    effective_end_date = scrapy.Field()
    created_at = scrapy.Field()
    last_edited_at = scrapy.Field()
    version = scrapy.Field()


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
