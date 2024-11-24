import os
from openai import OpenAI
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
OPENAI_CLIENT = OpenAI(api_key=OPENAI_KEY)
openai_client = OPENAI_CLIENT

MONGO_DB = os.getenv("MONGO_DB")
MONGO_CLIENT = MongoClient(MONGO_DB)
CATALOG_DB = MONGO_CLIENT.get_database("catalog")


# Collections
courses_collection = CATALOG_DB.get_collection("courses")
programs_collection = CATALOG_DB.get_collection("programs")
course_sets_collection = CATALOG_DB.get_collection("course_sets")
requisite_sets_collection = CATALOG_DB.get_collection("requisite_sets")
