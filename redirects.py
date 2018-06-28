#Utilities to handle redirects and redirect histories, also some proxy info
import requests
from fileIO import *

def get_redirects_print_only(parsingurl):
    """Traces and prints the redirects of a link provided, does not display safelinks
    Designed for single URL's"""
    response = requests.get(parsingurl)
    if response.history:
        count = 0
        for resp in response.history:
            strresp = str(resp.url)
            count += 1
            #info = []
            if ("safelinks.protection.outlook.com" in strresp):
                None
            elif ("safelinks.protection.outlook.com" not in strresp):  # parses out safelinks
                yield ("Redirect Depth {} \nRedirect type: {} \nResponse URL: {}{}".format(count, resp.status_code, resp.url, "\n"))
                print("Redirect Depth {}".format(count), "\nRedirect type: {}".format(
                    resp.status_code), "\nResponse URL: {}".format(resp.url) + "\n")
        print("Final (User sees) destination: {} \nWith a {} redirect status{}".format(response.url, response.status_code, "\n"))
    else:
        print("Request was not redirected")

def get_redirects(parsingurl):
    """Traces and prints the redirects of a link provided, does not display safelinks
    Designed for batch processing from text files"""
    response = requests.get(parsingurl)
    if response.history:
        yield("\nNew Redirect")
        count = 0
        for resp in response.history:
            strresp = str(resp.url)
            count += 1
            if ("safelinks.protection.outlook.com" in strresp):
                None
            elif ("safelinks.protection.outlook.com" not in strresp):  # parses out safelinks
                yield ("Redirect Depth {} \nRedirect type: {} \nResponse URL: {}{}".format(count, resp.status_code, resp.url, "\n"))
                #print("Redirect Depth {}".format(count), "\nRedirect type: {}".format(resp.status_code), "\nResponse URL: {}".format(resp.url) + "\n")
        yield("Final (User sees) destination: {} \nWith a {} redirect status{}".format(response.url, response.status_code, "\n"))
    else:
        print("Request was not redirected")


def onetime():
    urls = parse_file()
    output = []
    count = 1
    for url in urls:
        try:
            if "https://" in url:
                current = url
                for returned in get_redirects(url):
                    output.append(returned)
                    output.append("\n")
            else:  # for the Added: thing
                if "Added" in url:
                    print("Url Number: {}".format(count))
                    count += 1
                output.append(url)
        except:
            output.append("Error while checking {}".format(current))
    output = [q for q in output if q is not None]
    output = [q for q in output if q is not ","]
    save_list(output)
