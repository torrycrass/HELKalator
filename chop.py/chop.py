#!/usr/bin/python2.7

# -*- coding: utf-8 -*-

"""
PROGRAM NAME: Chop.PY (CHOPPY)
PURPOSE: To parse Zeek/Bro monolithic log files into component files
WHY: Importing Zeek/Bro logs into HELK/ELK systems (in my experience so far) requires
    data to be very clean. Splitting the data into specific types allows for troubleshooting
    at individual log type levels vs. trying to identify and resolve problems across a
    larger data set.

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
__copyright__ = "Copyright 2019, Chop.PY"
__credits__ = ["Torry Crass"]
__license__ = "NMP (http://www.torrycrass.com/nmp-license-v1-0/)"
__version__ = "23092019.1.0"
__maintainer__ = "Torry Crass"
__email__ = "@TorryCrass"
__status__ = "Prototype"

# PROGRAM START

logo = """\
 _____ _                 ________   __
/  __ \ |                | ___ \ \ / /
| /  \/ |__   ___  _ __  | |_/ /\ V /
| |   | '_ \ / _ \| '_ \ |  __/  \ /
| \__/\ | | | (_) | |_) || |     | |
 \____/_| |_|\___/| .__(_)_|     \_/
                  | |
                  |_|
"""
print logo
print __version__ + " | " + __email__
print "_" * 39 + "\n"

print "Chop.PY (choppy) takes your monolithic JSON formatted Zeek/Bro file\n" \
      "and splits the file into its component log files such as conn.log and\n" \
      "dns.log for ease of import to analysis systems.\n"

print "REQUIREMENTS:"
print "- JSON formatted data file\n" \
      "- Uniform data, no random non JSON lines\n" \
      "- A correct input filename\n"


with open(raw_input("Enter the file to parse: "), "r") as input_file:
    # TODO: Capture line count and display progress of writing activity.
    #  consider possible options to display progress bar like something in the post here:
    #  https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

    counter = 0

    print "\nSlicing and dicing your file...\n"

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

        counter += 1
        print "\r\tLines processed: [" + str(counter) + "]",

    print "\n\nChef work has been completed, you now have chopped ingredients."
