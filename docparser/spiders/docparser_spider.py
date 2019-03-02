import logging
import scrapy
from scrapy.utils.log import configure_logging

from docparser.items import DOCParserItem

configure_logging(install_root_handler=False)

logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


class DocParserSpider(scrapy.Spider):
    name = 'docparser'
    allowed_domains = ['www.dochkisinochki.ru']
    start_urls = (
        'https://www.dochkisinochki.ru/icatalog/',
    )

    def parse(self, response):
        pattern = "//ul[@class='topmenu-ndrow']/li/a/@href"
        menu_links = response.xpath(pattern).extract()
        for link in menu_links:
            url = response.urljoin(link)
        yield scrapy.Request('https://www.dochkisinochki.ru/icatalog/categories/progulki_i_poezdki/', callback=self.parse_categories_list)

    def parse_categories_list(self, response):
        pattern = "//ul/li/a[@class='shop-main-menu_submenu-item--link']/@href"
        categories_links = response.xpath(pattern).extract()
        for link in categories_links:
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_category)

    def parse_category(self, response):
        pattern = "//div[@class='esk-content']/a[@class='jDataLink']/@href"
        trade_links = response.xpath(pattern).extract()
        for link in trade_links:
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_product)

        next_info_pattern = "//div[@class='pagination-new']/a[@class='next_new']/@href"
        next_info = response.xpath(next_info_pattern).extract()
        if next_info:
            next_url = response.urljoin(next_info[0])
            yield scrapy.Request(next_url, callback=self.parse_category)

    def parse_product(self, response):
        print("Product URL")
        print(response.url)
        code = response.xpath("//span[@itemprop='sku']/text()").extract()
        print("code", code)
        item = DOCParserItem()
        item['code'] = code[0].strip() if code else ''
        item['url'] = response.url
        yield item

