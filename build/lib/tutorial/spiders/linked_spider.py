from crawl import CrawlSpider2
from scrapy.http import FormRequest, Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from crawl import Rule
from branditems import BrandData
from scrapy.contrib.loader import ItemLoader
from tutorial import settings


class AdData2(CrawlSpider2):
    name = 'AdData2'
    allowed_domains = ['www.addataexpress.com']
    # login_page = 'http://www.addataexpress.com/?page_id=806'
    DOWNLOAD_DELAY = 5
    USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    start_urls = ['https://platform.linkedin.com/js/xdrpc.html?v=0.0.2000-RC8.37403-1415#xdm_e=http%3A%2F%2Fwww.addataexpress.com&xdm_c=li_gen_1406568331137_0&xdm_p=1#target=li_gen_1406568331137_0&width=600&height=400&mode=wrapper']

    # rules = (
    #     Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
    #          callback='parse_item', follow=True),
    # )
    def init_request(self):
        settings.overrides['CONCURRENT_REQUESTS'] = 3
        settings.overrides['CONCURRENT_REQUESTS_PER_DOMAIN'] = 3
        settings.overrides['RANDOM_DOWNLOAD_DELAY'] = False
        return [FormRequest("http://www.addataexpress.com/chklog.php",
                        formdata={'username': 'atso', 'password': '988718'},
                        callback=self.start_requests)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'PHPSESSID': "ogo5flffuoca925b79b9s2bir4"}, callback=self.parse)

    # def start_requests(self):
    # #     """This function is called before crawling starts."""
    #     return Request(url=self.target_url, cookies={'PHPSESSID': "ogo5flffuoca925b79b9s2bir4"}, callback=self.parse)


    # def start_requests(self):
    #     yield Request(self.start_urls, cookies={'PHPSESSID': "ogo5flffuoca925b79b9s2bir4"}, callback=self.parse_response)

    # def parse_response(self, response):
    #     self.log(response)
    #         # Now the crawling can begin
    #     return self.initialized()
    #
    #
    # def login(self, response):
    #     """Generate a login request."""
    #     return FormRequest.from_response(response,
    #                                      formdata={'username': 'atso', 'password': '988718'},
    #                                      callback=self.check_login_response)
    #
    # def check_login_response(self, response):
    #     """Check the response returned by a login request to see if we are
    #     successfully logged in.
    #     """
    #     if "Welcome, Andrew Tso" in response.body:
    #         self.log("Successfully logged in. Let's start crawling!")
    #         # Now the crawling can begin
    #         return self.initialized()
    #     else:
    #         self.log("Login Failed :(")
    #         # Something went wrong, couldn't log in, so nothing happens

    def parse(self, response):
        l = ItemLoader(item=BrandData(), response=response)
        l.add_xpath('linkedin', '//*[@id="main-content"]/div/span')
        return l.load_item()


