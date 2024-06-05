import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

MONGO_DB = os.getenv("MONGO_DB")
MONGO_CLIENT = MongoClient(MONGO_DB)
DIRTY_CATALOG_DB = MONGO_CLIENT.get_database("dirty_catalog")
CATALOG_DB = MONGO_CLIENT.get_database("catalog")
