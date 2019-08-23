#!/usr/bin/python2.7

# -*- coding: utf-8 -*-

"""
The process for splitting files is as follows:

1. Open JSON file.
2. For each line find the "_path":"<type>" value.
3. Use the type value to append an entry to the corresponding file.
4. Files will be stored in the directory of execution.

- The file output should be used as append and should create the file if none exists.
- The program makes assumptions that you will provide a correct input file name.
- The data in the file should be refined to contain ONLY zeek/bro JSON entries.


License: NMP (Not My Problem v1.0)
License URL: http://www.torrycrass.com/nmp-license-v1-0/
"""

# Program metadata information
__author__ = "Torry Crass"
__copyright__ = "Copyright 2019, chopPY"
__credits__ = ["Torry Crass"]
__license__ = "NMP (http://www.torrycrass.com/nmp-license-v1-0/)"
__version__ = "23092019.1.0"
__maintainer__ = "Torry Crass"
__email__ = "@TorryCrass"
__status__ = "Prototype"


print("This program takes a json Bro/Zeek file and splits a combined file into different\n"
      "components based on the \"_path\":\"type\" value. For example:\n"
      "\"_path\":\"dns\" will be written to dns.json."
      "\n\n")

with open(raw_input("Enter the file to parse: "), "r") as input_file:
    print("\nSlicing and dicing your file...")
    for ln in input_file:
        # use split to make the values in the string manageable.
        # this requires a split on comma followed by a split on colon
        # followed by stripping off quotes and then concatenating to
        # make the log file name
        first_split = ln.split(',')
        second_split = first_split[0].split(':')
        file_name = second_split[1].strip("\"")
        logfile = file_name + ".log"

        # create the file if it doesn't exist (append does this by default)
        # append lines to existing files
        output_file = open(logfile, 'a')
        output_file.write(ln)
    print("\nChef work has been completed, you now have chopped ingredients.")
