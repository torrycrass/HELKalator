**PROGRAM NAME:** parsley  
**PURPOSE:** To find and replace an array of strings in a file. Best used with structured data  
**WHY:** This script was created to fix incorrectly formatted monolithic log files that contain Zeek/Bro data that could not be successfully added to a HELK instance due to incorrect, mis-formatted, or extra data.  

##### The process for search and replace is as follows:

1. Search terms are entered (one per line) in file_find.txt.
1. Corresponding replacement terms (one per line) are entered in field_update.txt.
1. parsley.py performs line by line search and replace for each of the search and
    corresponding replacement term over the specified file.
1. A file with the updates is created, the original file is left intact.

a. This is best used with structured data; it was written and intended for Zeek/Bro data but might have value elsewhere.
a. Beware of search terms, they should be as specific as possible. Generic terms will likely result in poor updates to the file and possibly data loss if values are overwritten.

License: NMP (Not My Problem v1.0)  
License URL: http://www.torrycrass.com/nmp-license-v1-0/
