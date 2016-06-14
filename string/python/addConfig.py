#!/usr/bin/python
# source : http://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python
# Get a value inside a configuration file
# Test on /boot/config.txt

import sys
import os
#All args

if len(sys.argv) == 3:
    alreadyDone = False

    file = sys.argv[1]
    string_to_add = sys.argv[2]

    if os.path.isfile(file): 
        for line in open(file):
            line = line.strip()
            if line:
                if "#" not in line:
                    if string_to_add in line:
                        alreadyDone = True

        if not alreadyDone:
            with open(file, "a") as file_append:
                file_append.write(string_to_add + "\n")
        else:
            sys.exit(1)