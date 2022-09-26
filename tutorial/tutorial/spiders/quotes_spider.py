import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.baoquangbinh.vn/thoi-su/202209/ky-niem-77-nam-quoc-khanh-nuoc-chxhcn-viet-nam-tai-cham-pa-sac-2203234/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//h2[@id='title']/text()").get()
        content = response.xpath("//div[@class='knc-content']").extract_first().strip()
        day = response.xpath("//span[@class='kbwcm-time']/text()").get()
        print('tieu de', title)
        print('content', content)
        print('day', day)