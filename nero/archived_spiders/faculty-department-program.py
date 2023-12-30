
import scrapy
import htmlmin
from unidecode import unidecode
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from nero.archived_spiders.__parser import FacultyDirectoryParser
from nero.archived_spiders.__utils import Utils
from nero.items import Faculty, Department, Program


class FacultySpider(CrawlSpider):
    name = 'faculty-department-program'
    allowed_domains = ['contacts.ucalgary.ca']
    start_urls = [
        'http://contacts.ucalgary.ca/directory/faculties',
        'http://contacts.ucalgary.ca/directory/departments'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select(".primary-row")
        for faculty_dom in faculties_dom:
            fdp = FacultyDirectoryParser(faculty_dom)
            title, code = fdp.title()
            phones, rooms, email, website = fdp.phone_room_email_website()
            aka = fdp.aka()
            parent_title, parent_type = fdp.parent()

            if "faculties" in response.url:  # This is a Faculty
                item_id = Utils.title_to_id(title, length=4)
                faculty_obj = Faculty(fid=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka)
                yield faculty_obj
            elif code != None and parent_title != None and parent_type != None:
                if parent_type == "Faculty":  # This is a Department
                    item_id = Utils.title_to_id(title)
                    fid = Utils.title_to_id(parent_title)
                    department_obj = Department(did=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka, fid=fid)
                    yield department_obj
                else:  # This is a Program
                    item_id = Utils.title_to_id(title)
                    did = Utils.title_to_id(parent_title)
                    program_obj = Program(pid=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka, did=did)
                    yield program_obj
            else:
                continue
