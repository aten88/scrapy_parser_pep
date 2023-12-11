import scrapy


class PepParseItem(scrapy.Item):
    """ Шаблон сохраняемых данных PEP """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
