import re
import hashlib
import HumanName

class Utils:

    @staticmethod
    def title_to_id(title, length = 4):
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
