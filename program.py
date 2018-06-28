from redirects import get_redirects_print_only
from fileIO import *
import requests
keep_on = True

print("===================Welcome to Web Utilities===================")
while keep_on == True:
    selection = eval(input("What would you like to do? \n(1) Trace a redirect \n(2)Trace redirects from a text file \n(3)exit: "))

    if selection == 1:
        url = input("What is the URL you would like to trace?: ")
        get_redirects_print_only(url)

    if selection == 2:
        #TODO fill this out
        pass

    if selection == 3:
        keep_on = False
