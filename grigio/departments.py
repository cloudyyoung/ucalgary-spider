from tqdm import tqdm

from bianco.requisites.methods import try_nlp

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB

# Departments
departments = list(DIRTY_CATALOG_DB.get_collection("departments").find({}))

departments_catalog = CATALOG_DB.get_collection("departments")
departments_catalog.delete_many({})

for department in tqdm(departments, desc="Departments"):
    department.pop("_id")
    departments_catalog.insert_one(department)

