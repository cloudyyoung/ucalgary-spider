# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import re
from itemadapter.adapter import ItemAdapter
from prisma import Prisma
from nero.items import Course, Subject


class DatabaseStorePipeline:
    def __init__(self) -> None:
        self.prisma = Prisma()

    def open_spider(self, spider): ...

    def close_spider(self, spider): ...

    async def process_item(self, item, spider):
        if not self.prisma.is_connected():
            await self.prisma.connect()

        adapted_item = ItemAdapter(item)

        # For all string fields, remove leading and trailing whitespace
        for field in adapted_item.field_names():
            if isinstance(item[field], str):
                item[field] = item[field].strip()
                item[field] = re.sub(r"\s+", " ", item[field])

        if isinstance(item, Subject):
            await self.prisma.subject.create(
                data={"title": item["title"], "code": item["code"]}
            )

        return item
