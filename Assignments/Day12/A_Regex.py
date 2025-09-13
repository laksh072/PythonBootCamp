# Assignment 1: List All .txt Files and Check for a Word using glob + re.search

# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found


# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".


# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

import glob
import re
import os


files = glob.glob("Assignments/Day12/*.txt")
for file in files:
    with open(file, "r") as f:
        content = f.read()
        match = re.search(r"Python", content)
        if match:
            print(f"Python found in : {file}")
        f.close()


files = glob.glob("Assignments/Day12/*.*")
print(files)
for file in files:
    filename = os.path.basename(file)
    match = re.match(r"^(data_).*(\.csv)$", filename)
    if match:
        print(f"csv file starts with data_: {file}")

listofphones = ["(123) 450-7890", "(080) 123-456", "(91) 11-82525"]
for phone in listofphones:
    match = re.match(r"\([1-9]{3}\)\s[0-9]{3}-[0-9]{4}", phone)
    if match:
        print(f"This is a valid phone Number: {phone}")
    else:
        print(f"Invalid phone Number: {phone}")
