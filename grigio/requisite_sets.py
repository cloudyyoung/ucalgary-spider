from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB, process_requisites

requisite_sets = list(DIRTY_CATALOG_DB.get_collection("requisite_sets").find({}))


# Process all course sets
requisite_sets_catalog = CATALOG_DB.get_collection("requisite_sets")
requisite_sets_catalog.delete_many({})


for requisite_set in tqdm(requisite_sets, desc="Requisite Sets"):
    requisite_set = requisite_set.copy()

    # Process requisites
    requisites = requisite_set["requisites"]
    requisite_set["requisites"] = process_requisites(requisites)

    # Insert course set
    requisite_sets_catalog.insert_one(requisite_set)
