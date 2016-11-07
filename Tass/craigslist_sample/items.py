# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TASSItem(Item):
    title = Field()
    article = Field()
    link = Field()
    date = Field()

