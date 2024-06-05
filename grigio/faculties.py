from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB

# Departments
faculties = list(DIRTY_CATALOG_DB.get_collection("faculties").find({}))

faculties_catalog = CATALOG_DB.get_collection("faculties")
faculties_catalog.delete_many({})

for faculty in tqdm(faculties, desc="Departments"):
    faculty.pop("_id")
    faculties_catalog.insert_one(faculty)
