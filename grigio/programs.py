from tqdm import tqdm

from grigio.utils import DIRTY_CATALOG_DB, CATALOG_DB, process_requisites

programs = list(
    DIRTY_CATALOG_DB.get_collection("programs").find(
        {"career": "Undergraduate Programs", "active": True}
    )
)


# Process all course sets
programs_catalog = CATALOG_DB.get_collection("programs")
programs_catalog.delete_many({})


for programs in tqdm(programs, desc="Programs"):
    programs = programs.copy()

    # Process requisites
    requisites = programs["requisites"]
    programs["requisites"] = process_requisites(requisites)

    # Insert course set
    programs_catalog.insert_one(programs)
