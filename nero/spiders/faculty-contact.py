
import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from nero.utils import Utils
from nero.items import CourseTitle, CourseInfo


class FacultyContact(CrawlSpider):
    name = 'faculty-contact'
    allowed_domains = ['contacts.ucalgary.ca']
    start_urls = [
        'http://contacts.ucalgary.ca/directory/faculties'
    ]

    def parse(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select(".primary-row")
        for faculty_dom in faculties_dom:
            detail_dom = faculty_dom.next_sibling

            title, code, fid = self.title(faculty_dom)
            phones, rooms, email, website = self.field(detail_dom)
            
            print(title, website)


    def title(self, faculty_dom):
        title = faculty_dom.select_one(".unitis-business-unit .uofc-row-expander").get_text(strip=True)
        code = faculty_dom.select_one(".unitis-business-unit .target").attrs['name']
        fid = Utils.faculty_to_id(title)

        return (title, code, fid)

    def field(self, faculty_dom):
        lists = {"phones": None, "rooms": None, "email": None, "website": None}
        for item in lists:
            text = []
            list_dom = faculty_dom.select(".unitis-" + item + "-list li")

            if list_dom:
                for each in list_dom:
                    if each.string:
                        text.append(each.string.strip())
                    else:
                        text.append(each.get_text(strip=True))
            
            if item == "website":
                text = list(filter(lambda x: not x.find("http"), text))

            if text:
                lists[item] = text
        return (lists['phones'], lists['rooms'], lists['email'], lists['website'])
