# -*- encoding: utf-8 -*-
from horses.spiders.horses_spider import HorsesSpider
import logging
import pandas as pd
import os
from scrapy.crawler import CrawlerProcess
import time


logging.getLogger('scrapy').propagate = False
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(HorsesSpider)


if __name__ == '__main__':
    while True:
        with open(os.path.join(os.getcwd(), 'output.csv'), 'r') as f:
            process.start()
            df = pd.read_csv(f, sep=",")
            print df
            time.sleep(300)
