"""File to run all the utilities from"""
from redirects import menu_options as redirects_menu
from tag_parsers import menu_options as tag_parsers_menu
from fileIO import *
import requests

print("===================Welcome to Web Utilities===================")
keep_on = True
while keep_on == True:

    utility_to_run = (eval(input("What type of utility do you need? \n(1)Redirect tracing (2)HTML Tag parsing: ")))
    if utility_to_run == 1:
        redirects_menu()
    elif utility_to_run == 2:
        tag_parsers_menu()
    #TODO Make this level of menu

    # selection = eval(input("What would you like to do? \n(1) Trace a redirect \n(2)Trace redirects from a text file \n(3)exit: "))
    #
    # if selection == 1:
    #     url = input("What is the URL you would like to trace?: ")
    #     single_URL_trace(url)
    #
    # if selection == 2:
    #     #TODO fill this out
    #     pass
    #
    # if selection == 3:
    #     keep_on = False
