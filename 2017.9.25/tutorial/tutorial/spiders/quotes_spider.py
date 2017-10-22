# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import QuotesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  'http://quotes.toscrape.com/page/2/',
                ]
            
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="quote"]')
        items = []
        item = QuotesItem()
        for site in sites:
            item['text'] = site.xpath('span[@class="text"]/text()').extract()
            item['author'] = site.xpath('span/small[@class="author"]/text()').extract()
            item['tags'] = site.xpath('div/meta[@class="keywords"]/@content').extract()
            items.append(item)
        return items