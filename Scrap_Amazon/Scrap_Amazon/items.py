# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapAmazonItem(scrapy.Item):
    # define the fields for your item here like:
    pname = scrapy.Field()
    reviews_num=scrapy.Field()
    image_url=scrapy.Field()
    
    pass

