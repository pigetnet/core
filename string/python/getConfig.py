#!/usr/bin/python
# Get a value inside a configuration file
# Test on /boot/config.txt

import sys
import os
#All args

if len(sys.argv) == 2:
    file = sys.argv[1]
    if os.path.isfile(file): 
        for line in open(file):
            line = line.strip()
            if line:
                if "#" not in line:
                    print line            