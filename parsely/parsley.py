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
__version__ = "23092019.1.0"
__maintainer__ = "Torry Crass"
__email__ = "@TorryCrass"
__status__ = "Prototype"

# PROGRAM START

input_file = open('nearly.json', 'r')
output_file = open('almost.json', 'w')

find_word = [line.rstrip('\n') for line in open("field_find", 'r')]
replace_word = [line.rstrip('\n') for line in open("field_update", 'r')]

print("Data and word list files opened, processing data...")

for line in input_file:
    newline = line
    for i in range(len(find_word)):
        newline = newline.replace(find_word[i], replace_word[i])
    output_file.write(newline)

input_file.close()
output_file.close()

print("File processing complete, if you didn't get an exception, something happened.")
