#!/usr/bin/python2.7

# -*- coding: utf-8 -*-

"""
PROGRAM NAME: parsley
PURPOSE: To find and replace an array of strings in a file. Best used with structured data
WHY: This script was created to fix incorrectly formatted monolithic log files that
    contain Zeek/Bro data that could not be successfully added to a HELK instance due to
	incorrect, misformatted, or extra data.
	
The process for search and replace is as follows:

1. Search terms are entered (one per line) in file_find.txt.
2. Corresponding replacement terms (one per line) are entered in field_update.txt.
3. parsley.py performs line by line search and replace for each of the search and
    corresponding replacement term over the specified file.
4. A file with the updates is created, the original file is left intact.

- This is best used with structured data; it was written and intended for Zeek/Bro
    data but might have value elsewhere.
- Beware of search terms, they should be as specific as possible. Generic terms
    will likely result in poor updates to the file and possibly data loss if values
	are overwritten.


License: NMP (Not My Problem v1.0)
License URL: http://www.torrycrass.com/nmp-license-v1-0/
"""

# Program metadata information
__author__ = "Torry Crass"
__copyright__ = "Copyright 2019, parsley"
__credits__ = ["Torry Crass"]
__license__ = "NMP (http://www.torrycrass.com/nmp-license-v1-0/)"
__version__ = "15102019.1.0"
__maintainer__ = "Torry Crass"
__email__ = "@TorryCrass"
__status__ = "Prototype"

# PROGRAM START

logo = """\
                           8               
                           8               
.oPYo. .oPYo. oPYo. .oPYo. 8 .oPYo. o    o 
8    8 .oooo8 8  `' Yb..   8 8oooo8 8    8 
8    8 8    8 8       'Yb. 8 8.     8    8 
8YooP' `YooP8 8     `YooP' 8 `Yooo' `YooP8 
8 ....::.....:..:::::.....:..:.....::....8 
8 ::::::::::::::::::::::::::::::::::::ooP'.
..::::::::::::::::::::::::::::::::::::...::
"""

print logo
print __version__ + " | " + __email__
print "_" * 58 + "\n"

print "parsley.py accepts an array of search terms from field_find.txt and replaces\n" \
    "finds with values from the corresponding array position in field_update.txt.\n"

print "REQUIREMENTS:"
print "- Search and replacement terms specified in corresponding .txt files\n" \
    "- Works best with uniform data sets\n" \
    "- For data safety an input and an output file so source data is not corrupted\n"

# TODO: Update program to allow overwrite of same file.
#  it may be desired to update the existing file instead of creating a new one;
#  the implication of this is if search and replace data is incorrect the resultant file
#  will be unusable so a warning to the user must be included.


def filecheck(filename):
    """
    This function checks to see if the file exists.
    
    :param filename: 
    :return: 
    """
    try:
        open(filename, 'r')
        return 1
    except IOError:
        print "Error: A required file does not exist.\n" \
              "- field_find.txt (required)\n" \
              "- field_update.txt (required)\n" \
              "- your entered JSON file (required)\n\n" \
              "Please check your files and try again."
        exit()

# Check if required array files exist, if not, exit immediately.
# The program requires these files to run properly.
filecheck("field_find.txt")
filecheck("field_update.txt")

# Get input and output file names from user
input_file = raw_input("Enter the ZEEK/BRO JSON file to parse: ")
filecheck(input_file)
output_file = raw_input("Enter the output file: ")

# Open files
input_file = open(input_file, 'r')
output_file = open(output_file, 'w')

# Parse array of terms into a list to be searched for and updated
find_word = [line.rstrip('\n') for line in open("field_find.txt", 'r')]
replace_word = [line.rstrip('\n') for line in open("field_update.txt", 'r')]

counter = 0

print("Data and word list files opened, processing data...\n")

for line in input_file:
    newline = line
    for i in range(len(find_word)):
        newline = newline.replace(find_word[i], replace_word[i])
    output_file.write(newline)

counter += 1
print "\r\tLines processed: [" + str(counter) + "]",

input_file.close()
output_file.close()

print("\n\nFile processing complete, if you didn't get an exception, something happened.")
