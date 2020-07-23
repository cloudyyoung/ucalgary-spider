import re
import hashlib

class Utils:

    @staticmethod
    def title_to_id(title, length = 4):
        title = re.sub(r"\((.*?)\)", r"\1", title)
        title = re.sub(r"[A-Za-z ]+ of", "", title)
        title = re.sub(r"Faculty", "", title)
        title = re.sub(r" and ", "", title)
        title = re.sub(r"([^a-zA-Z]*)", "", title)
        title = title.strip().encode("utf-8")

        md5 = hashlib.md5()
        md5.update(title)
        title_id = int(str(int(md5.hexdigest(), 16)).rjust(length, "0")[0:length])
        
        return title_id
