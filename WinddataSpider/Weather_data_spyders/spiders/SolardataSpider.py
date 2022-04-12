'''
Spider to download windspeed, wind direction from dwd
'''
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WinddataSpider(CrawlSpider):
    name = 'solardataSpider'

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):

        urls =  [
            'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/solar/historical/'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url

        download_url_list = []
        list_of_data = response.xpath('//html/body/pre/a/@href').getall()
        for iurl in list_of_data:
            if '_20091231_his' in iurl:
                download_link = url + iurl
                download_url_list.append(download_link)

        yield {'file_urls': download_url_list}
