import scrapy

from ..items import ScrapAmazonItem
class AmazonScSpider(scrapy.Spider):
    name = "amazon-sc"
    # allowed_domains = ["exapmple.com"]
    start_urls = ["https://www.amazon.in/s?k=headphones"]

    def parse(self, response):
        product=ScrapAmazonItem()
        name=response.css(".a-color-base.a-text-normal::text").extract();
        no_of_reviews=response.css(".s-link-style .s-underline-text::text").extract();
        image_url= response.css(".s-image::attr(src)").extract()
        product["reviews_num"]=no_of_reviews;
        product["pname"]=name;
        product["image_url"]=image_url;
        yield product;




        
