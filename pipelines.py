# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import spider


class ZhilianPipeline(object):
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(**spider.settings['MONGO_CONFIG'])
        self.db=self.client[spider.settings['MONGO_DB']]
        self.coll=self.client[spider.settings['MONGO_COLL']]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.coll.insert(item)
        return item
