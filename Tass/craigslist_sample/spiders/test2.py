from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from craigslist_sample.items import TASSItem
import scrapy
import re
import os.path
from scrapy.utils.response import body_or_str

class MySpider(CrawlSpider):
    name = "tass"
    allowed_domains = ["tass.com"]
    start_urls = ["http://tass.com/"]

    rules = (
        Rule(LinkExtractor(allow=('http://tass.com/.*\/\d{6}')), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = Selector(response)
        items = []
        item = TASSItem()
        item["title"] = hxs.xpath('//h1[@class="b-material__title"]/text()').extract()[0]
        article = hxs.xpath('string(//div[contains(@class,"b-material-text__l js-mediator-article") or contains(@class, "b-material-text js-mediator-article")])').extract()
        item["article"] = "\n".join(article).encode('utf8')
        item["link"] = response.url
        item["date"] = hxs.xpath('//meta[@name="publish_date"]/@content').extract()[0]
        items.append(item)
        return(items)