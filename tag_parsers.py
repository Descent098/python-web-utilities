# Contains Utilities for parsing different tags in html

import requests
import bs4

def parse_list(reference, web=False):
    """Parses all list tags and pulls the information from the ul and li tags
    Returns: String
    Arguments: reference; the path or URL to parse from
    web; True if reference is a URL or false for local filepath"""
    #TODO add logic for ordered list parsing

    #TODO Search by class ID
    #class_id = eval(input("Do you have a class you want to look in? (1)Yes (2)No: "))
    class_id = 2 #Temp value for testing
    if class_id == 1:
        input("What is the class name?: ")

    elif class_id == 2: #if theres not a class to parse
        if web == False:
            reference += ".html" #Adding extension to filename
            html = open(reference, "r")

        elif web == True:
            html = get_html_from_URL(reference)

        soup = bs4.BeautifulSoup(html, 'html.parser')
        return soup.find('ul').get_text()

def parse_heading(reference, size="1",web=False):
    """Parses all heading tags and pulls the information between the tag
    Returns: String
    Arguments: reference; the path or URL to parse from
    Size: the heading type i.e. 1 for heading 1
    web; True if reference is a URL or false for local filepath"""

    #TODO Search by class ID
    #class_id = eval(input("Do you have a class you want to look in? (1)Yes (2)No: "))
    class_id = 2 #Temp value for testing
    if class_id == 1:
        input("What is the class name?: ")

    elif class_id == 2: #if theres not a class to parse
        if web == False:
            reference += ".html" #Adding extension to filename
            html = open(reference, "r")

        elif web == True:
            html = get_html_from_URL(reference)

        soup = bs4.BeautifulSoup(html, 'html.parser')
        return soup.find('h{}'.format(size)).get_text()

def get_html_from_URL(url):
    """Function that takes a URL as input and returns the HTML as a string"""
    response = requests.get(url)
    return response.text

def menu_options():
    """Called from main program; compartmentalizing menu options per utility"""
    is_web = eval(input("Is the html from (1)The Web or (2)Local File?: "))
    if is_web == 1:
        web = True
    elif is_web ==2:
        web = False
    script_choice = eval(input("What would you like to parse? \n(1)Heading Tags (2)Lists: "))

    if script_choice == 1:
        size = input("What size heading are you looking for (i.e. 1 for h1 tags, 2 for h2 tags)?: ")
        print(parse_heading(input("File name/url (Excluding Extension i.e. index for index.html): "), size, web))

    elif script_choice ==2:
        print(parse_list(input("File name/url (Excluding Extension i.e. index for index.html): "), web))


if __name__ == "__main__":
    """Testing stuff; only works if file is run as main"""
    # #h1 Parse Testing
    # is_web = eval(input("Is the html from (1)The Web or (2)Local File?: "))
    # if is_web == 1:
    #     web = True
    # elif is_web ==2:
    #     web = False
    # print(parse_heading(input("File name/url (Excluding Extension i.e. index for index.html): "), "1", web))
    ##########################################################################################################
    # #ul Parse Testing
    # is_web = eval(input("Is the html from (1)The Web or (2)Local File?: "))
    # if is_web == 1:
    #     web = True
    # elif is_web ==2:
    #     web = False
    # print(parse_list(input("File name/url (Excluding Extension i.e. index for index.html): "), web))
