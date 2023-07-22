import scrapy

from ..items import ScrapAmazonItem
class AmazonScSpider(scrapy.Spider):
    name = "amazon-sc"
    # allowed_domains = ["exapmple.com"]
    count=1
    start_urls = ["https://www.amazon.in/s?k=headphones&page=1&qid=1690018332&ref=sr_pg_1"]

    def parse(self, response):
        product=ScrapAmazonItem()
        name=response.css(".a-color-base.a-text-normal::text").extract();
        no_of_reviews=response.css(".s-link-style .s-underline-text::text").extract();
        image_url= response.css(".s-image::attr(src)").extract()
        price=response.css(".a-price-whole::text").extract()
        product["reviews_num"]=no_of_reviews;
        product["pname"]=name;
        product["image_url"]=image_url;
        product["price"]=price;
        yield product;

        AmazonScSpider.count+=1
        nxt_page="https://www.amazon.in/s?k=headphones&page="+str(self.count)+"&qid=1690018332&ref=sr_pg_"+str(self.count);

        if AmazonScSpider.count<6:
            yield response.follow(nxt_page,callback=self.parse)
            print(self.count)





        
