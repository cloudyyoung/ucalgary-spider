
import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from nero.utils import Utils
from nero.items import Faculty, Department, Program


class FacultyContact(CrawlSpider):
    name = 'faculty-contact'
    allowed_domains = ['contacts.ucalgary.ca']
    start_urls = [
        'http://contacts.ucalgary.ca/directory/faculties',
        'http://contacts.ucalgary.ca/directory/departments'
    ]

    def parse(self, response):
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        faculties_dom = soup.select(".primary-row")
        for faculty_dom in faculties_dom:
            detail_dom = faculty_dom.next_sibling

            title, code = self.title(faculty_dom)
            phones, rooms, email, website = self.field(detail_dom)
            aka = self.aka(detail_dom)
            parent_title, parent_type = self.parent(faculty_dom)
            
            if "faculties" in response.url: # This is a faculty
                item_id = Utils.title_to_id(title, 4)
                faculty_obj = Faculty(fid=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka)
                yield faculty_obj
            elif code != None and parent_title != None:
                if parent_type == "Faculty": # This is a Department
                    item_id = Utils.title_to_id(title, 5)
                    fid = Utils.title_to_id(parent_title, 4)
                    department_onj = Department(did=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka, fid=fid)
                    yield department_onj
                else:  # This is a Program
                    item_id = Utils.title_to_id(title, 5)
                    did = Utils.title_to_id(parent_title, 5)
                    program_obj = Program(pid=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka, did=did)
                    yield program_obj
            
            if code == "cpsc":
                yield response.follow("http://contacts.ucalgary.ca/info/" + code + "/contact-us/directory/1-46929", self.parse_contacts_directory)

    def parse_contacts_directory(self, response):
        
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        staffs_dom = soup.select(".unitis-person-list .unitis-person-list tr")
        for staff_dom in staffs_dom:
            
            name, directory_id = self.staff_name(staff_dom)
            sid = Utils.name_to_id(name)

            print(name, sid)

            if not name:
                continue



        print(response.url)

    

    def title(self, faculty_dom):
        title_dom = faculty_dom.select_one(".unitis-business-unit .uofc-row-expander")
        if title_dom:
            title = title_dom.get_text(strip=True)
        else:
            title = None

        code_dom = faculty_dom.select_one(".unitis-business-unit .target")
        if code_dom:
            code = code_dom.attrs['name']
        else:
            code = None

        return (title, code)

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
                text = list(filter(lambda x: not x.find("http"), text)) # Only leave link with http

            if text:
                lists[item] = text

        return (lists['phones'], lists['rooms'], lists['email'], lists['website'])

    def aka(self, faculty_dom):
        aka = None
        contents_dom = faculty_dom.select(".details-row-cell .content")

        if contents_dom and len(contents_dom) >= 2:
            content_dom = contents_dom[1].select("p")

            for each in content_dom:
                text = each.get_text(strip=True)

                aka_reg_res = re.match(r"Also Known as:(.*)", text)
                if aka_reg_res:
                    aka = aka_reg_res.group(1).split(", ")

        return aka

    def parent(self, faculty_dom):
        parent_type_dom = faculty_dom.select_one(".unitis-business-unit-parents .unitis-campuscontacts-unit-type")
        if parent_type_dom:
            parent_type = parent_type_dom.string
        else:
            parent_type = None

        parent_title_dom = faculty_dom.select_one(".unitis-business-unit-parents a")
        if parent_title_dom:
            parent_title = parent_title_dom.string
        else:
            parent_title = None
        
        return (parent_title, parent_type)

    def staff_name(self, staff_dom):
        name_dom = staff_dom.select_one(".uofc-directory-name-cell a[href]")
        
        if not name_dom:
            name = directory_id = None
        else:
            name_arr = name_dom.string.strip().split(",")
            name = name_arr[1].strip() + " " + name_arr[0].strip()
            directory_id = name_dom.attrs['href'].strip().split("/")[-1].strip()

        return (name, directory_id)
