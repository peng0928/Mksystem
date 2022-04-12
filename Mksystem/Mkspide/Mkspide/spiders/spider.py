import re

import scrapy
from lxml import etree
from Mkspide.items import MkspideItem

class ExampleSpider(scrapy.Spider):
    name = 'MK'
    start_urls = ['https://www.imooc.com/course/list?ct=1&page=1']
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }
    def parse(self, response):
        for page in range(1,29):
            url = f'https://www.imooc.com/course/list?ct=1&page={page}'
            yield scrapy.Request(url=url, callback=self.l_parse)

    def l_parse(self, response):
        tree = etree.HTML(response.text)
        links = tree.xpath("//div[@class='course-list']/div[@class='list max-1152 clearfix']/a/@href")
        titles = tree.xpath("//div[@class='course-list']/div[@class='list max-1152 clearfix']/a/p[@class='title ellipsis2']/text()")
        ranks = tree.xpath("//div[@class='list max-1152 clearfix']/a/p[@class='one']/text()")
        for item, rank, title in zip(links, ranks, titles):
            rank = re.findall('\d+', rank)[0]
            url = 'https:' + item
            title = title
            # print(url)
            yield scrapy.Request(url=url, meta={'url':url, 'title':title, 'rank':rank}, callback=self.c_parser)

    def c_parser(self,response):
        rank = response.meta['rank']
        title = response.meta['title']
        url = response.meta['url']
        tree = etree.HTML(response.text)
        mark = tree.xpath("//div[@class='static-item l score-btn']/span[@class='meta-value']/text()|//div[@class='info-bar clearfix']/span[@class='nodistance'][4]/text()")[0]
        text_data = tree.xpath("//div[@class='course-description course-wrap']/text()|//div[@class='dec-box']/p/text()")[0]
        item = MkspideItem()
        item['title'] = title
        item['url'] = url
        item['mark'] = mark
        item['text_data'] = text_data
        item['people'] = str(rank)
        yield item
        # print(item)