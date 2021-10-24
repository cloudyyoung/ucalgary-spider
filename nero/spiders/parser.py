import re
from unidecode import unidecode

from nero.utils import Utils


class Parser:
    dom = ""

    def __init__(self, dom) -> None:
        self.dom = dom


class FacultyDirectoryParser(Parser):

    def title(self):
        title_dom = self.dom.select_one(".unitis-business-unit .uofc-row-expander")
        if title_dom:
            title = title_dom.get_text(strip=True)
        else:
            title = None

        code_dom = self.dom.select_one(".unitis-business-unit .target")
        if code_dom:
            code = code_dom.attrs['name']
        else:
            code = None

        return (title, code)

    def phone_room_email_website(self):
        lists = {"phones": None, "rooms": None, "email": None, "website": None}
        for item in lists:
            text = []
            list_dom = self.dom.next_sibling.select(".unitis-%s-list li" % item)

            if list_dom:
                for each in list_dom:
                    if each.string:
                        text.append(each.string.strip())
                    else:
                        text.append(each.get_text(strip=True))

            if item == "website":
                text = list(filter(lambda x: not x.find("http"), text))  # Only leave link with http

            if text:
                lists[item] = text

        return (lists['phones'], lists['rooms'], lists['email'], lists['website'])

    def aka(self):
        aka = None
        contents_dom = self.dom.next_sibling.select(".details-row-cell .content")

        if contents_dom and len(contents_dom) >= 2:
            content_dom = contents_dom[1].select("p")

            for each in content_dom:
                text = each.get_text(strip=True)

                aka_reg_res = re.match(r"Also Known as:(.*)", text)
                if aka_reg_res:
                    aka = aka_reg_res.group(1).split(", ")

        return aka

    def parent(self):
        parent_type_dom = self.dom.select_one(".unitis-business-unit-parents .unitis-campuscontacts-unit-type")
        if parent_type_dom:
            parent_type = parent_type_dom.string
        else:
            parent_type = None

        parent_title_dom = self.dom.select_one(".unitis-business-unit-parents a")
        if parent_title_dom:
            parent_title = parent_title_dom.string
        else:
            parent_title = None

        return (parent_title, parent_type)

    def directory_of_people(self):
        directory_dom = self.dom.next_sibling.select_one(".unitis-directory-link a")
        if directory_dom:
            directory = directory_dom.attrs['href']
        else:
            directory = None
        return directory


class CourseDirectoryParser(Parser):
    def title(self):
        title_dom = self.dom.select_one("a.uofc-row-expander")
        title_text = title_dom.get_text(strip=True)
        titles = title_text.split("-")

        key = titles[0].strip()
        topic = titles[1].strip()

        return (key, topic)

    def __dom_text_link(self, dom):
        if(dom.find("a")):
            text = dom.select_one("a").get_text(strip=True)
            link = dom.select_one("a").attrs['href']
        else:
            text = dom.get_text(strip=True)
            link = None
        return (text, link)

    def sections(self):
        if not self.dom.next_sibling or not self.dom.next_sibling.select_one(".uofc-table"):
            # This course does not have a section
            # Example: https://contacts.ucalgary.ca/info/phil/courses/w2022
            # PHIL 367: "Sorry, no sections found."
            return

        if "has-details" in self.dom.next_sibling.select_one(".uofc-table").attrs['class']:  # If table is .uofc-table.has-details
            blocks_dom = self.dom.next_sibling.select(".uofc-table tr.primary-row")  # Blocks are Info + Note, means primary + detached
        else:
            blocks_dom = self.dom.next_sibling.select(".uofc-table tr")  # Blocks are only Info

        for block_dom in blocks_dom:

            name = block_dom.contents[1].get_text(strip=True)  # LEC 1, LEC 2, TUT 1
            time = unidecode(block_dom.contents[2].get_text(strip=True))  # TBA, TR 16:00 - 16:50

            room, room_link = self.__dom_text_link(block_dom.contents[3])  # TBA, MS 201

            instructor_name, instructor_link = self.__dom_text_link(block_dom.contents[4])  # Nathaly Verwaal

            if instructor_name != "":
                sid = Utils.name_to_id(instructor_name)
            else:
                sid = None

            if instructor_link != None:
                directory_id = instructor_link.split("/")[-1]
            else:
                directory_id = None

            if "primary-row" in block_dom.attrs['class'] and block_dom.next_sibling != None and "attached-row" in block_dom.next_sibling.attrs['class']:  # If it has attached-row
                note = block_dom.next_sibling.select_one(".details-row-cell div[style]").get_text(strip=True)
                note = note.lstrip("Notes: ")

                if note == "":
                    note = None
            else:
                note = None

            yield (name, time, room, sid, directory_id, note)

class StaffParser(Parser):
    def name(self):
        name_dom = self.dom.select_one(".uofc-directory-name-cell a[href]")

        if not name_dom:
            name = directory_id = None
        else:
            name_arr = name_dom.string.strip().split(",")
            name = name_arr[1].strip() + " " + name_arr[0].strip()
            directory_id = name_dom.attrs['href'].strip().split("/")[-1].strip()

        return (name, directory_id)

    def title_room_phone(self):
        lists = {"title": None, "room": None, "phone": None}
        for each in lists:
            items_dom = self.dom.select(".uofc-directory-%s-cell li" % each)

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
