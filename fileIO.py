def parse_file():
    """Takes the path of a file as input and parses it"""
    fn = open("redirects_list.txt")
    dat = []
    URLS = []
    line = fn.readlines()
    dat = [url.split("\n") for url in line] #single line list comprehension
    for li in dat:
        for URL in li:
            if "https://" in URL :
                URLS.add(URL)
            else:
                print("\nURL loop output: {}".format(URL)
    #return URLS

#print(parse_file())
