import re
import datetime
import hashlib
from nameparser import HumanName

class Utils:

    @staticmethod
    def title_to_id(title, length = 5):
        title = re.sub(r"\((.*?)\)", r"\1", title)
        title = re.sub(r"[A-Za-z ]+ of", "", title)
        title = re.sub(r"Faculty", "", title)
        title = re.sub(r" and ", "", title)
        title = re.sub(r"([^a-zA-Z]*)", "", title)
        title = title.strip()

        title_id = Utils.__text_to_id(title, length)
        return title_id

    @staticmethod
    def name_to_id(name):
        name_obj = HumanName(name)
        name_parse = name_obj.first.capitalize().strip() + name_obj.last.capitalize().strip()

        name_id = Utils.__text_to_id(name_parse, 6)
        return name_id
    
    @staticmethod
    def __text_to_id(text, length):
        text = str(text).encode("utf-8")
        md5 = hashlib.md5()
        md5.update(text)
        text_id = int(str(int(md5.hexdigest(), 16)).rjust(length, "0")[0:length])
        return text_id

    @staticmethod
    def current_term():
        now = datetime.datetime.now()

        fall_start = datetime.datetime(month=8, day=24)
        fall_end = datetime.datetime(month=12, day=31)

        winter_start = datetime.datetime(month=1, day=1)
        winder_end = datetime.datetime(month=4, day=30)

        spring_start = datetime.datetime(month=5, day=1)
        spring_end = datetime.datetime(month=6, day=26)

        summer_start = datetime.datetime(month=6, day=27)
        summer_end = datetime.datetime(month=8, day=23)

        if fall_start <= now <= fall_end:
            return "Fall"
        elif winter_start <= now <= winter_end:
            return "Winter"
        elif spring_start <= now <= spring_end:
            return "Spring"
        elif summer_start <= now <= summer_end:
            return "Summer"

    @staticmethod
    def current_year():
        now = datetime.datetime.now()
        return now.year


    @staticmethod
    def abbr_to_term(text):
        if(text == "f"):
            return "Fall"
        elif(text == "w"):
            return "Winter"
        elif(text == "p"):
            return "Spring"
        elif(text == "s"):
            return "Summer"
        else:
            return None