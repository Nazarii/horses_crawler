# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import pandas as pd
from spiders.horses_spider import HORSES


class HorsePipeline(object):

    def open_spider(self, spider):
        self.collection = []

    def close_spider(self, spider):
        outpath = os.path.join(os.getcwd(), 'output.csv')
        out = {}
        odds = [x['odds'] for x in self.collection]
        for horse in HORSES:
            odd = [x.pop(0) for x in odds]
            out[horse] = odd
        df = pd.DataFrame.from_dict(out)
        df.to_csv(outpath, index=False, quoting=csv.QUOTE_NONNUMERIC)

    def process_item(self, item, spider):
        self.collection.append(dict(item))
        return item
