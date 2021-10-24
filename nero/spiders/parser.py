import re
from unidecode import unidecode

from nero.utils import Utils


class Parser:
    dom = ""

    def __init__(self, dom) -> None:
        self.dom = dom

class CourseInfoParser(Parser):

    def __convert_link(self, doms):
        for dom in doms.select("a.link-text"):
            href = dom.get("href").split("#")[-1].strip()
            dom.attrs = {"cid": href}
            dom.name = "course"
        return doms

    def calendar_id(self):
        return int(self.dom.previous_element.attrs['name'])

    def title_number_topic(self):
        keys = self.dom.select(".course-code")
        title = keys[0].get_text(strip=True)
        number = int(keys[1].get_text(strip=True))
        topic = keys[2].get_text(strip=True)
        return (title, number, topic)

    def description_subtopics(self):
        description_dom = self.dom.select_one(".course-desc")
        self.__convert_link(description_dom)

        description = []
        sub_topics = {}
        concat_text = " "

        for description_dom in description_dom.contents:
            sub_topics_reg = r"[0-9]{3}\.([0-9]{2})[\.]? ([A-Za-z \,\(\)\'\-][^0-9<]*)"
            sub_topics_reg_res_all = re.findall(
                sub_topics_reg, str(description_dom))

            if sub_topics_reg_res_all:  # Contain sub topics
                for sub_topics_reg_res in sub_topics_reg_res_all:
                    decimal = sub_topics_reg_res[0]
                    topic = sub_topics_reg_res[1].strip()
                    sub_topics[decimal] = topic
                concat_text = "<br>"
            elif description_dom.name == "a":  # Link
                description.append(str(description_dom).strip())
            elif description_dom.string:  # Pure string
                description.append(str(description_dom.string.strip()))
            else:
                description.append(description_dom.decode_contents().strip())
        pass

        description = concat_text.join(description)

        if not description:
            description = None

        if not sub_topics:
            sub_topics = None

        return (description, sub_topics)

    def requisites(self):
        ret = {"prereq": None, "coreq": None, "antireq": None, "notes": None, "aka": None}

        for each in ret.keys():
            req_dom = self.dom.select_one(".course-" + each)
            self.__convert_link(req_dom)

            inner_html = req_dom.decode_contents().strip()

            if inner_html:
                ret[each] = inner_html
            else:
                ret[each] = None

        return (ret["prereq"], ret["coreq"], ret["antireq"], ret["notes"], ret["aka"])

    def repeat_nogpa(self):
        ret = {"repeat": False, "nogpa": False}

        for each in ret.keys():
            repeat_dom = self.dom.select_one(".course-" + each)
            content = repeat_dom.get_text(strip=True)

            ret[each] = content != ""

        return (ret["repeat"], ret["nogpa"])

    def units_credits_hours_time_length(self):
        hours_text = self.dom.select_one(
            ".course-hours").get_text(strip=True)
        hours_reg = {
            "units": r"([0-9.]*?) units",  # units
            "credits": r"([0-9.]*?) credit[s]?",  # credits
            "hours": r"\((.*?[0-9A-Za-z\/]-.*?[0-9A-Z\/])\)",  # h(x-y)
            "time_length": r"\((.*?[0-9-] .*?[a-zA-Z])\)"  # x period
        }
        ret = {}  # [units, credits, h(x-y), x period]

        for (key, reg) in hours_reg.items():

            if not re.search(reg, hours_text):
                ret[key] = None
                continue

            hours_reg_res = re.findall(reg, hours_text)  # Find text
            hours_text = re.sub(reg, "", hours_text)  # Remove matched text

            if key == "units" or key == "credits":
                ret[key] = float(hours_reg_res[0])
            else:
                ret[key] = list(hours_reg_res)

        return (ret["units"], ret["credits"], ret["hours"], ret["time_length"])


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
