import requests

def parse_file(filepath):
    """Takes the path of a file as input and parses it"""
    fn = open(filepath, r)

    URLS = []
    #Parse input file for URL's

    #assign data from files in a loop to variable dat
    while reading: # placeholder sudo code
        for url in line:
            urls = [url for url in dat] #single line list comprehension
        else conditional:
            None


def get_redirects(parsingurl):
    """Traces and prints the redirects of a link provided"""
    #TODO Make
    response = requests.get(parsingurl)
    if response.history:
        print("Request was redirected")
        count = 0
        for resp in response.history:
            strresp = str(resp.url)
            count+=1
            info = []
            if ("safelinks.protection.outlook.com" in strresp):
                q =1
            elif ("safelinks.protection.outlook.com" not in strresp):
                info.add(["Redirect Depth {}".format(count),"\nRedirect type: {}".format(resp.status_code), "\nResponse URL: {}".format(resp.url) + "\n"])
                print ("Redirect Depth {}".format(count),"\nRedirect type: {}".format(resp.status_code), "\nResponse URL: {}".format(resp.url) + "\n")
        print("Final (User sees) destination:")
        print(response.status_code, response.url)
    else:
        print ("Request was not redirected")


get_redirects(input("What URL would you like to see the redirect trace for?: "))#Input URL to trace
