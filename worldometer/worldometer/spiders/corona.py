import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
            for country  in response.xpath('//tbody/tr/td[2]/a'):
                link=country.xpath('.//@href').get()
                name=country.xpath('.//text()').get()
                #absolute_url= 'https://www.worldometers.info/coronavirus/'+link
                if link:
                 yield response.follow(url=link,callback=self.pageparser,meta={'country_name':name})


    def pageparser(self,response):
        name=response.request.meta['country_name']
        cases=response.xpath('(//*[@id="maincounter-wrap"]/div/span)[1]/text()').get()
        recoverd=response.xpath('(//*[@id="maincounter-wrap"]/div/span)[3]/text()').get()
        death=response.xpath('(//*[@id="maincounter-wrap"]/div/span)[2]/text()').get()
    

        yield{
            'Name':name,
            'total':cases,
            'recoverd':recoverd,
            'deaths':death
        }
