#TODO set up a set of crawlers for specific purposes
import scrapy

class validation_spider(scrapy.Spider):
    """Crawler to validate that a site can be crawled;
    Extends scrapy spider"""
    def __init__(self, domains = [], start = ''):
        """Constructor for spider instance;
        Returns: None
        Arguments: domains; list of subdomains allowed to parse
        start; the starting url to crawl from"""
        name = "validation"
        allowed_domains = domains
        start_urls = start

if __name__ == "__main__":
    1
