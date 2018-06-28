from redirects import *
from fileIO import *
import requests
keep_on = True

print("===================Welcome to Web Utilities===================")
while keep_on == True:
    selection = eval(input("What would you like to do? \n(1) Trace a redirect \n(2)Trace redirects from a text file \n(3)exit: "))

    if selection == 1:
        url = input("What is the URL you would like to trace?: ")
        output = []
        count = 1
        try:
            if ("https://" or "http://") in url:
                current = url
                for returned in list(get_redirects(url)):
                    output.append(returned)
                    output.append("\n")
            else:
                None
        except:
            output.append("Error while checking {}".format(current))
        for i in output:
            print(i)

    if selection == 2:
        #TODO fill this out
        pass

    if selection == 3:
        keep_on = False
