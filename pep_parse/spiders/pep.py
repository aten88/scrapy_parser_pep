import scrapy
import re

from pep_parse.constants import PEP_URLS, PEP_DOMAIN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """ Паук-парсер PEP """
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [PEP_URLS]

    def parse(self, response):
        """ Метод парсинга ссылок PEP """
        all_peps = response.css('section#numerical-index table tbody tr')
        for href_pep in all_peps:
            pep_link = PEP_URLS + href_pep.css('td a.pep::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """ Метод парсинга данных из карточки PEP """
        number_pep = re.search(r'\d+', response.css(
            'section#pep-content h1::text'
        ).get()).group()
        name_pep = response.css('section#pep-content h1::text').get().split(
            '–', 1
        )[1].strip()
        status_pep = response.css('section#pep-content abbr::text').get()

        data = {
            'number': number_pep,
            'name': name_pep,
            'status': status_pep
        }
        yield PepParseItem(data)
