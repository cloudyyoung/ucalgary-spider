import re
import hashlib

class Utils:


    @staticmethod
    def faculty_to_id(faculty):
        faculty = re.sub(r"\(.*?\)", "", faculty)
        faculty = re.sub(r"[A-Za-z ]+ of", "", faculty)
        faculty = re.sub(r"Faculty", "", faculty)
        faculty = re.sub(r"([^a-zA-Z]*)", "", faculty)
        faculty = faculty.strip().encode("utf-8")

        md5 = hashlib.md5()
        md5.update(faculty)
        faculty_id = int(str(int(md5.hexdigest(), 16)).rjust(4, "0")[0:4])

        return faculty_id
