# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import re
import os
from itemadapter.adapter import ItemAdapter
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_DB = os.getenv("MONGO_DB")
MONGO_CLIENT = MongoClient(MONGO_DB)
MONGO_COLLECTION = "catalog"


class FileStorePipeline:
    files = {}

    def file_name_convert(self, item_type):
        return str(re.sub(r"([a-z])([A-Z])", r"\1-\2", item_type)).lower()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        for file in self.files.values():
            file.close()

    def process_item(self, item, spider):
        if item.__tablename__:
            tablename = item.__tablename__
        else:
            tablename = str(item.__class__.__name__).lower() + "s"

        # For all string fields, remove leading and trailing whitespace
        for field in ItemAdapter(item).field_names():
            if isinstance(item[field], str):
                item[field] = item[field].strip()
                item[field] = re.sub(r"\s+", " ", item[field])

        collection = MONGO_CLIENT.get_database(MONGO_COLLECTION).get_collection(
            tablename
        )
        collection.insert_one(ItemAdapter(item).asdict())

        return item
