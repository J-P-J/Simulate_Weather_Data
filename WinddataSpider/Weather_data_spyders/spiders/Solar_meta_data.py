import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SolarmetaSpider(CrawlSpider):
    name = 'SolarmetaSpider'

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):

        urls =  [
            'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/solar/meta_data/'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url

        download_url_list = []
        list_of_data = response.xpath('//html/body/pre/a/@href').getall()
        for iurl in list_of_data:
            if '_' in iurl:
                download_link = url + iurl
                download_url_list.append(download_link)

        yield {'file_urls': download_url_list}

