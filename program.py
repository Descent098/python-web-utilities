"""File to run all the utilities from"""
import requests
import os

# Import module menus
from modules.redirects import menu_options as redirects_menu
from modules.tag_parsers import menu_options as tag_parsers_menu
from modules.youtube_utilities import menu_options as youtube_utilities_menu
from modules.fileIO import *

def clear_terminal():
    """Clears Terminal"""
    if os.name=='nt': #Windows
        os.system('cls')

    else:
        os.system('clear')


def menu():
    keep_on = True
    print("===================Welcome to Web Utilities===================")
    output = None
    while keep_on == True:
        clear_terminal()
        if output:
            print("NOTICE: {}\n".format(output))
        
        utility_to_run = (eval(input("What type of utility do you need? \n(0)Exit \n(1)Redirect tracing (Very Broken) \n(2)HTML Tag parsing \n(3)Youtube Utilities: ")))
        if utility_to_run == 1:
            redirects_menu()

        elif utility_to_run == 2:
            tag_parsers_menu()

        elif utility_to_run == 3:
            output = youtube_utilities_menu()

        elif utility_to_run == 0:
            exit()

if __name__ == "__main__":
    menu()