# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import re
import json
from itemadapter.adapter import ItemAdapter
import requests
from nero.items import Course, Subject


class PlanUcalgaryApiPipeline:
    def open_spider(self, spider): ...

    def close_spider(self, spider): ...

    async def process_item(self, item, spider):
        adapted_item = ItemAdapter(item)

        # For all string fields, remove leading and trailing whitespace
        for field in adapted_item.field_names():
            if isinstance(item[field], str):
                adapted_item[field] = item[field].strip()
                adapted_item[field] = re.sub(r"\s+", " ", item[field])

        if hasattr(item, "__collection_name__"):
            collection_name = item.__collection_name__
        else:
            collection_name = item.__class__.__name__.lower() + "s"

        if isinstance(item, Course):
            if not adapted_item.get("is_active"):
                return item

        url = f"http://localhost:5150/{collection_name}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImMzYzc3MWNiLWI4NjctNGVjNC1hOTYyLThiYWZlMDhkNjE5NSIsImVtYWlsIjoiY2xvdWR5LnlvdW5nQG91dGxvb2suY29tIiwiaWF0IjoxNzQwMjk1Njk2LCJleHAiOjE3NDAzMzE2OTYsImlzcyI6InBsYW4tdWNhbGdhcnktYXBpIn0.uqwPA2FaRICf2k6PfZ7BWrJVPM8a1ODNKbgyZpdGhnc",
        }

        response = requests.post(url, json=adapted_item.asdict(), headers=headers)

        if response.status_code == 403:
            response_json = response.json()
            existing = response_json.get("existing", None)

            if existing:
                existing_id = existing.get("id", None)

                if existing_id:
                    url += f"/{existing_id}"
                    response = requests.put(
                        url, json=adapted_item.asdict(), headers=headers
                    )

        if response.status_code > 299 and response.status_code != 403:
            spider.logger.error(
                f"Failed to POST /{collection_name}\n{json.dumps(adapted_item.asdict())}\n{response.text}\n\n"
            )
            # exit()

        return item
