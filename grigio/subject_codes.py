from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB

# Departments
subject_codes = list(DIRTY_CATALOG_DB.get_collection("subject_codes").find({}))

subject_codes_catalog = CATALOG_DB.get_collection("subject_codes")
subject_codes_catalog.delete_many({})

for code in tqdm(subject_codes, desc="Subject Codes"):
    code.pop("_id")
    subject_codes_catalog.insert_one(code)
