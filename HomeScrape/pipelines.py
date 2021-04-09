# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class HomescrapePipeline:

    def __init__(self):
        self.client = pymongo.MongoClient(f'mongodb://quickcompany:Jst5XRpQZRCcQeKU@143.110.189.142:27071')
        self.db = self.client['prod_data']
        self.collection = self.db['Troibits']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
