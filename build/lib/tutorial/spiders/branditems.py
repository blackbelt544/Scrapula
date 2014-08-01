# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import *
from w3lib.html import remove_entities
class BrandData(Item):
    brand = Field(input_processor=MapCompose(remove_entities),
                  output_processor=Identity(),
    )

    address = Field(input_processor=MapCompose(remove_entities),
                    output_processor=Identity(), )

    compownbrand = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )

    phone = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )

    URL = Field(input_processor=MapCompose(remove_entities),
                         output_processor=TakeFirst(), )

    seniorcorpent = Field(input_processor=MapCompose(remove_entities),
                         output_processor=TakeFirst(), )

    businesscat = Field(input_processor=MapCompose(remove_entities),
                         output_processor=TakeFirst(), )

    industries = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )

    title = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )

    name = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )

    linkedin = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )

    email = Field(input_processor=MapCompose(remove_entities),
                         output_processor=Identity(), )