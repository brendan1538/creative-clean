import os
import os.path
import time
import datetime
import csv
from os import listdir
from os.path import isfile, join

currentDir = os.getcwd()
dline = (datetime.datetime.today() +
         datetime.timedelta(-30)).strftime('%Y/%m/%d')

removedFiles = []

# Add any other file extensions you want removed to this tuple
extensions = ('.png', '.jpg', '.psd', '.mov', '.mp4')
cleaned_extensions = []
# Clean the tuple by checking if a . is missing, and adding at the beginning if so.
# This will primarily be useful in future updates.


for e in extensions:
    cleaned_extensions.append(("." + e) if e.find(".") == -1 else e)
cleaned_extensions_tuple = (cleaned_extensions)


def getModDate(file):
    # Get the last modified date of the given file and return it if there's not error
    m = os.path.getmtime(file)
    try:
        return m
    except AttributeError:
        return "Error retreiving the modified date of " + file


def deleteFile(date, file):
    # Check if file is...
    # 1. Older than the cutoff date
    # 2. Ends with a file type in the extensions tuple
    if date < dline and file.lower().endswith(tuple(cleaned_extensions_tuple)):
        print((''))
        removedFiles.append(file)
        os.remove(file)


def clean_dir():
    for path, dirs, fileList in os.walk(currentDir):
        for f in fileList:
            if not f.startswith('.'):  # ignore hidden files
                absolutePath = os.path.join(path, f)
                if os.path.isfile(absolutePath):
                    date = time.strftime(
                        '%Y/%m/%d', time.gmtime(getModDate(absolutePath)))
                    # Invokes function to check if file should be deleted
                    deleteFile(date, absolutePath)


print("""
                   *** Welcome to Creative Clean! ***
    This tool automates the removal of old, unused files in a directory.
    It will even search through subfolders, so make sure this script is
    placed in the top-most directory you want to work down from!
    ********************************************************************
    """)
user_input = input("Do you wish to clean the current directory? (y/n): ")
if(user_input.lower() == "y") or (user_input.lower() == "yes"):
    how_often = input("Background or one-time? (bg / ot): ")
    if(how_often.lower() == "bg"):
        while True:
            print("""
              ******* Running clean process... *******
                Default occurrence is every 30 days.
              Consult README.pdf to see how to adjust
                settings and run in the background.
              CTRL+Z to pause script, CTRL+C to exit
            """)
            # Clean the directory
            clean_dir()

            print("\nFile(s) removed: " + str(removedFiles))

            user_exit = input("Quit? (y/n): ")
            if(user_exit.lower() == "y") or (user_exit.lower() == "yes"):
                break
            elif (user_exit.lower() == "n") or (user_exit.lower() == "no"):
                time.sleep(86400*30)  # Run every 30 days
                continue
    elif(how_often.lower() == "ot"):
        print("""
            ******* Running clean process... *******
                        One-time clean.
            Consult README.pdf to see how to adjust
              settings and run in the background.
        """)
        # Clean the directory
        clean_dir()
        print("\nFile(s) removed: " + str(removedFiles))
else:
    print("""Okay, please place this Python file in a directory you wish to clean,
    and open again when you're ready!""")
