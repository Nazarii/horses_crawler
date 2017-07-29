# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv
import pandas as pd


class HorsePipeline(object):

    def open_spider(self, spider):
        self.collection = []
        self.df = pd.DataFrame()

    def close_spider(self, spider):
        self.df = pd.DataFrame(self.collection)
        df = self.df
        outpath = os.path.join(os.getcwd(), 'output.csv')
        df.to_csv(outpath, index=False, quoting=csv.QUOTE_NONNUMERIC)

    def process_item(self, item, spider):
        self.collection.append(dict(item))
        return item
