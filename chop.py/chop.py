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

is_syslog  = raw_input("Is this file a syslog file that NSM logs have been output to? (Y/N): ")

with open(raw_input("Enter the file to parse: "), "r") as input_file:
    # TODO: Capture line count and display progress of writing activity.
    #  consider possible options to display progress bar like something in the post here:
    #  https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

    # TODO: Check space to be used and space available.
    #  report this data to the user and ask for conformation to continue.

    # TODO: Combine syslog based cleanup into the chop.py program.
    #  1. Strip the localhost entries
    #  2. Strip the "message repeated" entries
    #  3. Output to a new, cleaned file, re-use that file to "split" the logs.

    # TODO: Migration different activities into functions.
    #  Originally it was not necessary to contain the functions of this script
    #  in functions but since the script has expanded to include additional operations
    #  it is now beneficial to migrate code into functions.

    linenumber = 0

    # 1. If we're combining without removing the line entry. Process the combination first,
    # it is assumed that the file will always contain top-to-bottom entries.
    # 2. If line does not start with {" skip the line.

    for line in input_file:
        cleaned_file = open("sanitized.json", 'a')
        error_file = open("error.log", 'a')

        # if the line is greater than 8045 combine line with next line.
        if len(line) >= 8045:
            error_file.write("Line: " + str(linenumber) + " Length: " + str(len(line)))
            combinedline = line.replace('\n', '').replace('\r', '') + next(input_file)
            cleaned_file.write(combinedline)

        # if line starts with valid JSON write the line.
        elif line.lstrip().startswith("{\""):
            cleaned_file.write(line)

        # error catch any remaining lines to the error.log.
        else:
            error_file.write(line)

        print "\r\tLines sanitized: [" + str(linenumber) + "]",
        linenumber += 1

    counter = 0

    # process newly created json file.
    clean_file = open("sanitized.json", 'r')

    print "\nSlicing and dicing your file...\n"

    for ln in clean_file:

        # use split to make the values in the string manageable.
        # this requires a split on comma followed by a split on colon
        # followed by stripping off quotes and then concatenating to
        # make the log file name
        first_split = ln.split(',')
        second_split = first_split[0].split(':')

        # handle exception if lines do not contain proper formatting and continue.
        try:
            file_name = second_split[1].strip("\"")
        except Exception, e:
            err = open('error.log', 'a')
            err.write('Exception: %s' %e + ' line: ' + str(counter) + '\n')
            err.close()
            continue

        logfile = file_name + ".json"

        # create the file if it doesn't exist (append does this by default)
        # append lines to existing files
        output_file = open(logfile, 'a')
        output_file.write(ln)

        counter += 1
        print "\r\tLines processed: [" + str(counter) + "]",

    print "\n\nChef work has been completed, you now have chopped ingredients."
