# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json
import re
from itemadapter import ItemAdapter


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
        item_type = item.__class__.__name__
        if(item_type not in self.files.keys()):
            file_object = open("data/" + self.file_name_convert(item_type) + ".jsonl", 'w')
            self.files[item_type] = file_object
        
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.files[item_type].write(line)
        self.files[item_type].flush()

        return item
