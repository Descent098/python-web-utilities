from cx_Freeze import setup, Executable

"""This file is used with cx_freeze to create an EXE out of the program"""

base = None

executables = [Executable("program.py", base=base)]

packages = ["idna", "bs4", "requests", "scrapy"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "web utilities",
    options = options,
    version = "0.1.0",
    description = 'a selection of python web utilities',
    executables = executables
)
