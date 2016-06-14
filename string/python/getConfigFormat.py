#!/usr/bin/python
# source : http://stackoverflow.com/questions/11294535/verify-if-a-string-is-json-in-python
# source : http://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists-using-python

import ConfigParser
import sys
import json
import os.path
global file
global file_contents

#Check if file exists

file = sys.argv[1]
configType = "UNKNOWN"
if os.path.isfile(file): 

    file_contents = open(file).read()

    isINI = False
    isConfig = False
    isConfigWPA = False
    isSamba = False
    isJSON = False
    isNGINX = False

    def checkINI():
    	config = ConfigParser.ConfigParser()
    	try:
    	    config.read(file)
    	    return True
    	except:
    	    return False

    def checkSamba():
        if '[global]' in file_contents:
            return True
        else:
            return False

    def checkJSON():
        try:
            json_object = json.loads(file_contents)
        except ValueError, e:
            return False
        return True

    def checkConfig():
        if '[' in file_contents:
            return False
        else:
            if '{' in file_contents:
                return False
            if '=' in file_contents:
               return True
            else:
                return False

    def checkConfigWPA():
        if '[' in file_contents:
            return False
        else:
            if '=' in file_contents:
                if '{' in file_contents:
                    return True
            else:
                return False

    def checkNGINX():
        if '[' in file_contents:
            return False
        else:
            if '=' in file_contents:
               return False
            else:
                if '{' in file_contents:
                    return True

    isINI = checkINI()
    if isINI: 
        configType = "INI"
    isSAMBA = checkSamba()
    if isSAMBA: 
        configType = "SAMBA"
    isJSON = checkJSON()
    if isJSON: 
        configType = "JSON"
    isConfig = checkConfig()
    if isConfig: 
        configType = "CONFIG"
    isConfigWPA = checkConfigWPA()
    if isConfigWPA:
        configType = "WPASUPPLICANT"
    isNGINX = checkNGINX()
    if isNGINX:
        configType = "NGINX"
    print configType
else:
    print "NOFILE"

