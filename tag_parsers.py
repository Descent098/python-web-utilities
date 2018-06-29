# Contains Utilities for parsing different tags in html
from lxml import html
import requests
import bs4

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
    reference += ".html" #Adding extension to filename
    class_id = eval(input("Do you have a class you want to look in? (1)Yes (2)No: "))
    if class_id == 1:
        input("What is the class name?: ")

    elif class_id == 2: #if theres not a class to parse
        if web == False:
            html = open(reference, "r")
            soup = bs4.BeautifulSoup(html, 'html.parser')
            return soup.find('h1').get_text()


        elif web == True:
            #TODO Implement functionality
            None

if __name__ == "__main__":
    """Testing stuff; only works if file is run as main"""
    print(parse_heading_1(input("File name (Excluding Extension i.e. index for index.html): ")))
