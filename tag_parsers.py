# Contains Utilities for parsing different tags in html
from lxml import html
import requests

def parse_ul_tags(reference, web=False):
    """Parses ul tags from the URL's html and pulls all the information
    Returns: String
    Arguments: reference; the path or URL to parse from
    web; True if reference is a URL or false for local filepath"""
    #TODO implement using local parsing code and pull from URL using requests
    if web == False:
        #TODO Implement local path logic
        None
    elif web == True:
        #TODO Implement functionality
        None

def parse_heading_1(reference, web=False):
    """Parses all h1 tags and pulls the information between the tag
    Returns: String
    Arguments: reference; the path or URL to parse from
    web; True if reference is a URL or false for local filepath"""
    if web == False:
        with open(reference, "r") as f:
            page = f.read()
        tree = html.fromstring(page)
        for i in tree:
            print(i.drop_tag())
        print(tree)

    elif web == True:
        #TODO Implement functionality
        None

parse_heading_1("ul.html")
