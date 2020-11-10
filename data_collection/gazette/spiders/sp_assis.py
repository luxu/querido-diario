# -*- coding: utf-8 -*-
import scrapy
from dateparser import parse

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpAssisSpider(BaseGazetteSpider):
    TERRITORY_ID = "3504008"
    name = "sp_assis"
    allowed_domains = "www.assis.sp.gov.br"
    start_urls = ["https://www.assis.sp.gov.br/diario/"]
    BASE_URL = 'https://www.assis.sp.gov.br'

    def start_requests(self):
        for ano in range(2012,2018):
            gazette_url = f"https://www.assis.sp.gov.br/diario/{ano}"
            yield scrapy.Request(gazette_url)

    def parse(self, response):
        edicoes = response.css("#content ul li")
        for edicao in edicoes:
            url_do_diario = edicao.css("a::attr(href)").get()
            url_completa = ''.join((self.BASE_URL,url_do_diario[1:]))
            print(url_completa)
            break

            # urllib.request.urlretrieve(f'https://www.assis.sp.gov.br/diario_impresso/2016/2{i}.pdf', 'diario.pdf')

            # with open('diario.pdf', 'rb') as f:
            #     gazette = pdftotext.PDF(f)
            #
            # print(re.search(
            #     '\d* de [janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro]* de \d*',
            #     gazette[0]).group(0))
            #
            # print(pdf)
        # gazettes = response.css("#lista-edicoes li.edicao-atual")
        # for gazette in gazettes:
        #     gazette_url = gazette.css("a::attr(href)").extract_first()
        #     if gazette_url:
        #         yield scrapy.Request(gazette_url, callback=self.parse_gazette)
        #
        # for next_page_url in response.css("div.paginacao a::attr(href)"):
        #     yield response.follow(next_page_url, callback=self.parse)

    def parse_gazette(self, response):
        ...
        # gazette_date = parse(
        #     response.css(".edicao-data::text").extract_first(""), languages=["pt"]
        # ).date()
        # file_urls = response.css("div.edicao-download a::attr(href)").extract()
        # is_extra_edition = (
        #     "extra" in response.css("div.edicao-titulo::text").extract_first("").lower()
        # )
        # power = "executive"
        #
        # yield Gazette(
            #     date=gazette_date,
        #     file_urls=file_urls,
        #     is_extra_edition=is_extra_edition,
        #     power=power,
        # )
