# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DataCollectorItem(Item):
    # define the fields for your item here like:
    # name = Field()
   title = Field()
   linke = Field()
   source = Field()
   actor = Field()
   content = Field()
