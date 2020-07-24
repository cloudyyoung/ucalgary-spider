
import scrapy
import htmlmin
import re
from unidecode import unidecode
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from nero.utils import Utils
from nero.items import Faculty, Department, Program, Staff


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

            title, code = self.faculty_title(faculty_dom)
            phones, rooms, email, website = self.faculty_field(detail_dom)
            aka = self.faculty_aka(detail_dom)
            parent_title, parent_type = self.faculty_parent(faculty_dom)
            directory = self.faculty_directory(detail_dom)
            
            if "faculties" in response.url: # This is a Faculty
                item_id = Utils.title_to_id(title)
                faculty_obj = Faculty(fid=item_id, title=title, code=code, phones=phones, rooms=rooms, email=email, website=website, aka=aka)
                yield faculty_obj
            elif code != None and parent_title != None and parent_type != None:
                if parent_type == "Faculty": # This is a Department
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
            
            # TODO: Academic only -> All contacts
            if directory: # If has contact directory
                yield response.follow("/info/" + code + "/contact-us/directory/1-46929", self.parse_contacts_directory)



    def parse_contacts_directory(self, response):
        
        body = htmlmin.minify(str(response.body, encoding="utf-8"), remove_empty_space=True, remove_all_empty_space=True)
        body = unidecode(body)
        soup = BeautifulSoup(body, 'html.parser')

        department_dom = soup.select_one(".headline .content a")
        faculty = department_dom.string.replace("Contacts", "").strip()
        did = Utils.title_to_id(faculty)

        staffs_dom = soup.select(".unitis-person-list .unitis-person-list tr")
        for staff_dom in staffs_dom:
            
            name, directory_id = self.staff_name(staff_dom)
            sid = Utils.name_to_id(name)
            title, room, phone = self.staff_field(staff_dom)

            staff_obj = Staff(sid=sid, name=name, directory_id=directory_id, title=title, room=room, phone=phone, did=did)
            yield staff_obj

        print(response.url)

    

    def faculty_title(self, faculty_dom):
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

    def faculty_field(self, faculty_dom):
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

    def faculty_aka(self, faculty_dom):
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

    def faculty_parent(self, faculty_dom):
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

    def faculty_directory(self, faculty_dom):
        directory_dom = faculty_dom.select_one(".unitis-directory-link a")
        if directory_dom:
            directory = directory_dom.attrs['href']
        else:
            directory = None
        return directory

    def staff_name(self, staff_dom):
        name_dom = staff_dom.select_one(".uofc-directory-name-cell a[href]")
        
        if not name_dom:
            name = directory_id = None
        else:
            name_arr = name_dom.string.strip().split(",")
            name = name_arr[1].strip() + " " + name_arr[0].strip()
            directory_id = name_dom.attrs['href'].strip().split("/")[-1].strip()

        return (name, directory_id)

    def staff_field(self, staff_dom):
        lists = {"title": None, "room": None, "phone": None}
        for each in lists:
            items_dom = staff_dom.select(".uofc-directory-" + each + "-cell li")

            if not items_dom:
                continue

            text = []
            for item_dom in items_dom:
                if item_dom.string:
                    text.append(item_dom.string.strip())
                else:
                    text.append(item_dom.get_text(strip=True))

            if text:
                lists[each] = text

        return (lists['title'], lists['room'], lists['phone'])
        
