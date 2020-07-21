# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json
import jsonlines
from itemadapter import ItemAdapter

class NeroPipeline:
    def process_item(self, item, spider):

        with jsonlines.open("data/" + spider.name + '.jsonlines', mode='a') as writer:
            writer.write(item.__dict__['_values'])

        return item
