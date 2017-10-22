# -*- coding: utf-8 -*-
import scrapy 
from tutorial.items import TutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  'http://quotes.toscrape.com/page/2/',
                  ]

    def parse(self, response):
        items = []
        
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="quote"]')
        for site in sites:
            item = TutorialItem()
            item['text'] = site.xpath('span[@class="text"]/text()').extract()
            item['author'] = site.xpath('span/small[@class="author"]/text()').extract()
            item['tag'] = site.xpath('div/meta[@class="keywords"]/@content').extract()
            items.append(item)
        return items
        