# Helper functions to handle file input and output
import tkinter as tk
from tkinter import filedialog


def select_file():
    """Opens a dialogue to select text files and returns path as a string"""
    root = tk.Tk()
    root.withdraw()
    file_path = str(filedialog.askopenfilename(
        title="Select File",
        filetypes=[("Text files", ".txt")]
        ))
    return str(file_path)


def parse_file():
    """Takes the path of a file as input and parses it"""
    source = open(select_file())
    dat = []
    URLS = []
    line = source.readlines()
    dat = [url.split("to") for url in line]  # single line list comprehension
    for li in dat:
        for URL in li:
            if "https://n" in URL:
                URLS.append(URL.lstrip())
                URLS.append("\n")
            else:
                # print("\nNot a URL loop output: {}".format(URL))
                None
    return URLS


def save_list(list_data):
    """Takes in data and writes it to file"""
    new_filename = input("What would you like the filename to be?:")
    new_filename += ".txt"
    q = open(new_filename, "w")
    for info in list_data:
        print(info)
        q.write(info)


if __name__ == "__main__":
    print(select_file())