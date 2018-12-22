import scrapy
import requests
from bs4 import BeautifulSoup

class site:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url))

    def __repr__(self):
        soup.title.string


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
    yt= site("https://youtube.com")
    print(yt)