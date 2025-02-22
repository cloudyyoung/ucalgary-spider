# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import re
from itemadapter.adapter import ItemAdapter
from prisma import Prisma
from nero.items import Course, Subject
import asyncio
from concurrent.futures import ThreadPoolExecutor


class DatabaseStorePipeline:
    def __init__(self) -> None:
        self.prisma = Prisma()
        self.loop = asyncio.get_event_loop()
        self.executor = ThreadPoolExecutor()

    def open_spider(self, spider):
        self.loop.run_in_executor(self.executor, self.prisma.connect)

    def close_spider(self, spider):
        self.loop.run_in_executor(self.executor, self.prisma.disconnect)

    def process_item(self, item, spider):
        adapted_item = ItemAdapter(item)

        # For all string fields, remove leading and trailing whitespace
        for field in adapted_item.field_names():
            if isinstance(item[field], str):
                item[field] = item[field].strip()
                item[field] = re.sub(r"\s+", " ", item[field])

        print(item)

        if isinstance(item, Subject):
            self.loop.run_in_executor(self.executor, self.create_subject, item)

        return item

    def create_subject(self, item):
        asyncio.run(self.prisma.subject.create(data=item))
        return item
