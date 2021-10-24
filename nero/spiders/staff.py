
import scrapy
import htmlmin
from unidecode import unidecode
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from nero.spiders.parser import FacultyDirectoryParser, StaffParser
from nero.utils import Utils
from nero.items import Staff


class StaffSpider(CrawlSpider):
    name = 'staff'
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
            detail_dom = faculty_dom.next_sibling

            fdp = FacultyDirectoryParser(faculty_dom)
            title, code = fdp.title()
            directory = fdp.directory_of_people()

            if directory:  # If has contact directory
                yield response.follow("/info/%s/contact-us/directory" % code, self.parse_contacts_directory)

    def parse_contacts_directory(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        department_dom = soup.select_one(".headline .content a")
        faculty = department_dom.string.replace("Contacts", "").strip()
        did = Utils.title_to_id(faculty)

        staffs_dom = soup.select(".unitis-person-list .unitis-person-list tr")
        for staff_dom in staffs_dom:

            sp = StaffParser(staff_dom)
            name, directory_id = sp.name()
            title, room, phone = sp.title_room_phone()
            sid = Utils.name_to_id(name)

            staff_obj = Staff(sid=sid, name=name, directory_id=directory_id, title=title, room=room, phone=phone, did=did)
            yield staff_obj

        print(response.url)
