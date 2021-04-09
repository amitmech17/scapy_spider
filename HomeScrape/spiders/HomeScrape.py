import scrapy
from HomeScrape.items import HomeScrapeItem


class HomeSpider(scrapy.Spider):
    name = 'HomeScrape'

    def __init__(self, comp_id=None, *args, **kwargs):
        super(HomeSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://find-and-update.company-information.service.gov.uk/company/{comp_id}']

    def parse(self, response):
        item = HomeScrapeItem()
        item['address'] = response.xpath("(//dd[@class='text data'])[1]/text()").get().replace('\n', '').strip()
        item['status'] = response.xpath("(//dd[@class='text data'])[2]/text()").get().replace('\n', '').strip()
        item['type'] = response.xpath("(//dd[@class='text data'])[3]/text()").get().replace('\n', '').strip()
        item['Incorporate'] = response.xpath("//dd[@id='company-creation-date']/text()").get()
        accounts = response.xpath("//div[@class = 'column-half'][1]//p").extract()
        account = ''
        for acc in accounts:
            acc = acc.replace('<p>', '').replace('\n', '').replace('</strong>', ' ').replace('<strong>', ' ').replace('<br>', '').replace('</p>', '').replace("  ", "").strip()
            if acc != '':
                account = account + " " + acc
        item['Accounts'] = account
        confirmations = response.xpath("//div[@class = 'column-half'][2]//p").extract()
        confirmation = ''
        for con in confirmations:
            con = con.replace('<p>', '').replace('\n', '').replace('</strong>', ' ').replace('<strong>', ' ').replace(
                '<br>', '').replace('</p>', '').replace("  ", "").strip()
            if con != '':
                confirmation = confirmation + " " + con
        item['confirmation_status'] = confirmation
        yield item


