import scrapy
from horses.items import HorseItem

HORSES = ['Sizing John',
          'Thistlecrack',
          'Might Bite',
          'Fox Norton',
          'Douvan',
          'Djakadam',
          'Un De Sceaux',
          'Outlander',
          'Tea For Two',
          'Native River',
          'Cue Card',
          'Coneygree',
          'Yorkhill',
          'Top Notch',
          'Valseur Lido',
          'Min',
          'Altior',
          'Bristol De Mai',
          'Josses Hill',
          'Bellshill',
          'Clan Des Obeaux',
          ]


class HorsesSpider(scrapy.Spider):
    name = 'horses'

    def start_requests(self):
        item = HorseItem()
        urls = [
            'http://sports.williamhill.com/bet/en-gb/betting/e/11029917/ap/Ascot+%2d+King+George+VI+Stakes+%2d+29th+Jul+2017.html',
            'https://www.skybet.com/horse-racing/ascot/event/20693785',
            'http://www.paddypower.com/racing/future-racing/king-george-vi--chase',
            'http://www.paddypower.com/racing/future-racing/king-george-vi--chase',
            'https://www.bet365.com/?lng=1&cb=105812028182#/AC/B2/C172/D101/E33281960/F2/G-1/H-1/P10/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, meta={'item': item,
                                                'dont_redirect': True,
                                                'handle_httpstatus_list': [301,
                                                                           302,
                                                                           403,
                                                                           ]
                                                }, callback=self.parse)

    def parse(self, response):
        item = response.request.meta['item']
        horse_lst = response.css('div.infos.left h4.left::text').extract()
        horses = [str(horse.encode('ascii', 'ignore').strip('\n\t'))
                  for horse in horse_lst]
        odds = response.css('div.odd a::text').extract()
        odds = map(str, odds)
        item['horse_name'] = horses or HORSES
        item['odds'] = odds or [None] * 21
        item['url'] = response.url or [None] * 21
        yield item
