from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class HorseSpider(CrawlSpider):

    name = 'Whirlaway'

    allow_domains = ['treehouse-projects.github.io']

    start_urls = ['http://treehouse-projects.github.io/horse-land']

    # These are rules that the spider will follow
    rules = [Rule(LinkExtractor(allow=r'.*'),
                  callback='parse-horses',
                  follow=True)]

    def parse_horses(self, response):
        url = response.url
        title = response.css('title::text').extract()
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))