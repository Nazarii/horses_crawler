import scrapy
from horses.items import HorseItem


class HorsesSpider(scrapy.Spider):
    name = 'horses'

    def start_requests(self):
        item = HorseItem()
        urls = [
            'http://sports.williamhill.com/bet/en-gb/betting/e/11029917/ap/Ascot+-+King+George+VI+Stakes+-+29th+Jul+2017.html',
            'https://www.skybet.com/horse-racing/ascot/event/20693785',
            'http://www.paddypower.com/racing/future-racing/king-george-vi--chase',
        #     TODO - add Webdriver for click on next url
            'https://www.bet365.com/?lng=1&amp;cb=105812028182#/HO/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse)

    def parse(self, response):
        pass