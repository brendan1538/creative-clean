import os
import os.path
import time
import datetime
import csv
from os import listdir
from os.path import isfile, join

currentDir = os.getcwd()
dline = (datetime.datetime.today() +
         datetime.timedelta(-30)).strftime('%m/%d/%Y')

removedFiles = []

# Add any other file extensions you want removed to this tuple
extensions = ('.png', '.jpg', '.psd', '.mov', '.mp4')


def getModDate(file):
    # Get the last modified date of the given file and return it
    m = os.path.getmtime(file)
    try:
        return m
    except AttributeError:
        return "Error retreiving the modified date of " + file


def deleteFile(date, file):
    # Check if file is...
    # 1. Older than the cutoff date
    # 2. Ends with a file type in the reference sheet
    if date < dline and file.lower().endswith(extensions):
        print((''))
        removedFiles.append(file)
        os.remove(file)


while True:
    for path, dirs, fileList in os.walk(currentDir):
        clean_files = (os.path.join(path, filename) for filename in fileList)
        for f in fileList:
            if not f.startswith('.'):  # ignore hidden files
                absolutePath = os.path.join(path, f)
                if os.path.isfile(absolutePath):
                    date = time.strftime(
                        '%m/%d/%Y', time.gmtime(getModDate(absolutePath)))

                    # Invokes function to check if file should be deleted
                    deleteFile(date, absolutePath)

    print("File(s) removed: " + str(removedFiles))
    time.sleep(86400*30)  # Run every 30 days
