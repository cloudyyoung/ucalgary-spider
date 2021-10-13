import re
import datetime
import time
import hashlib
from nameparser import HumanName


class Utils:

    @staticmethod
    def title_to_id(title, length=5):
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
    def current_academic_year():
        now = datetime.datetime.now()
        
        year = now.year
        fall_start = datetime.datetime(year=year, month=8, day=24)
        year_end = datetime.datetime(year=year, month=12, day=31)

        if now >= fall_start and now <= year_end:
            return now.year
        elif now < fall_start:
            return now.year - 1

    @staticmethod
    def current_academic_year_short():
        return Utils.current_academic_year() - 2000

    @staticmethod
    def abbr_to_term(abbr):
        if(abbr == "f"):
            return "Fall"
        elif(abbr == "w"):
            return "Winter"
        elif(abbr == "p"):
            return "Spring"
        elif(abbr == "s"):
            return "Summer"
        else:
            return None

    @staticmethod
    def term_to_long_id(term, year_short):
        long_id = "32" + str(year_short)
        if term == "p":
            long_id += "3"
        elif term == "s":
            long_id += "5"
        elif term == "f":
            long_id += "7"
        elif term == "w":
            long_id += "1"
        return long_id
