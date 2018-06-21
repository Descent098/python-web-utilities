def parse_file():
    """Takes the path of a file as input and parses it"""
    fn = open("redirects_list_raw_mini.txt")
    dat = []
    URLS = []
    line = fn.readlines()
    dat = [url.split("\n") for url in line]  # single line list comprehension
    for li in dat:
        for URL in li:
            if "https://n" in URL:
                URLS.append(URL.lstrip())
                URLS.append("\n")
            if "Added:" in URL:
                URLS.append(URL.lstrip())
                URLS.append("\n")
            else:
                #print("\nNot a URL loop output: {}".format(URL))
                None
    return URLS


def save_list(list_data):
    """Takes in data and writes it to file"""
    new_filename = "Last_Raw_Data"  # Hard coded for current use
    new_filename += ".txt"
    q = open(new_filename, "w")
    for info in list_data:
        print(info)
        q.write(info)
