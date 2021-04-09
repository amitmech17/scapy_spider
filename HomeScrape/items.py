# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field()
    status = scrapy.Field()
    type = scrapy.Field()
    Incorporate = scrapy.Field()
    Accounts = scrapy.Field()
    confirmation_status = scrapy.Field()
    Nature_of_business = scrapy.Field()




