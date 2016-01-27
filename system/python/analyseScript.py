#!/usr/bin/python
import sys
import os.path
from tabulate import tabulate
global description
global usage
global example
global installedProgram
global moduleCommand
global systemCommand
global longdescription
global nb_title
global nb_subtitle
global Return
global info
global interactive
global variables
global fileExistsCheck
global arguments
global longdescriptionTable

description = ""
usage = ""
example = ""
installedProgram = []
moduleCommand = []
systemCommand = []
longdescription = ""
nb_title = 0
nb_subtitle = 0
Return = ""
info = ""
interactive = False
variables = []
fileExistsCheck = []
arguments = []
longdescriptionTable = []


def removeCommand(text, pattern):
    text = text.replace(pattern, "")
    text = text.strip()
    text = text.replace("'", "")
    text = text.replace('"', '')
    text = text.replace('$0', fileToCheck)
    text = text.replace("$OK", "")
    text = text.replace("$WARN", "")
    text = text.replace("$INFO", "")
    text = text.replace("$ERR", "")
    return text


def analyseFile(fileToCheck):
    global description
    global usage
    global example
    global installedProgram
    global moduleCommand
    global systemCommand
    global longdescription
    global nb_title
    global nb_subtitle
    global Return
    global info
    global interactive
    global variables
    global fileExistsCheck
    global arguments
    global longdescriptionTable

    installedProgram = []
    with open(fileToCheck) as f:
        content = f.readlines()

    for line in content:
        if '/show/usageDescription' in line:
            description = removeCommand(line, "/show/usageDescription")
        if '/show/info' in line:
            info = removeCommand(line, '/show/info')
        if '/show/usage' in line:
            usage = removeCommand(line, "/show/usage")
        if '/show/return' in line:
            Return = removeCommand(line, "/show/return")
        if '/show/example' in line:
            example = removeCommand(line, "/show/example")
        if '/system/install' in line:
            nb_subtitle = nb_subtitle + 1
            installCommand = removeCommand(line, "/system/install")
            longdescription += "   " + str(nb_subtitle) + ". -- Install: " + installCommand + "\n"
            installedProgram.append(installCommand)

        if 'apt-get install' in line:
            nb_subtitle = nb_subtitle + 1
            installCommand = removeCommand(line, "apt-get install")
            longdescription += "   " + str(nb_subtitle) + ". -- Install: " + installCommand + "\n"
            installedProgram.append(installCommand)

        if '/show/description' in line:
            nb_title = nb_title + 1
            nb_subtitle = 0
            longdescription += str(nb_title) + "." + " " + removeCommand(line, "/show/description") + "\n"
            longdescriptionTable.append([str(nb_title) + "." + " " + removeCommand(line, "/show/description"), ""])

        if '/show/colecho "' in line:
            nb_subtitle = nb_subtitle + 1
            longdescription += "   " + str(nb_subtitle) + ". " + removeCommand(line, "/show/colecho") + "\n"
            longdescriptionTable.append([str(nb_subtitle) + ". " + removeCommand(line, "/show/colecho"), ""])

        if '/show/listecho' in line:
            nb_subtitle = nb_subtitle + 1
            longdescription += "   " + str(nb_subtitle) + ". " + removeCommand(line, "/show/listecho") + "\n"
            longdescriptionTable.append([str(nb_subtitle) + ". " + removeCommand(line, "/show/listecho"), ""])

        if '/show/askUser' in line:
            nb_subtitle = nb_subtitle + 1
            longdescription += "   " + str(nb_subtitle) + ". -- Ask user: " + removeCommand(line, ". /show/askUser") + "\n"
            longdescriptionTable.append([str(nb_subtitle) + ". -- Ask user: " + removeCommand(line, ". /show/askUser"), ""])

            interactive = True

        # Check for variables
        if '=$' in line:
            variablesRaw = line.strip()
            variables.append(variablesRaw)
            nbArguments = variablesRaw[-1:]
            if nbArguments.isdigit():
                if '=$'+nbArguments in line:
                    arguments.append(nbArguments + ":" + variablesRaw.replace("=$"+nbArguments, ""))

        # Check for piget command
        if '/do/' in line:
            if '/show/listecho' in line:
                pass
            else:
                moduleCommand.append(line.strip())

        # Check for piget system command
        if '/system/' in line:
            systemCommand.append(line.strip())

        if 'if [[ -e ' in line:
            checkCommand = line.replace("if [[ -e ", "")
            checkCommand = checkCommand.replace("]];then", "")
            fileExistsCheck.append(checkCommand.strip())


def displayText():
    print "----------------------------------------"
    print fileToCheck
    print "----------------------------------------"

    if info != "":
        print "info: " + info
    else:
        print "info: [alpha] [undocumented]"

    if description != "":
        print "Description: " + description

    if usage != "":
        print "Usage: " + usage

    if Return != "":
        print "Return: " + Return

    if example != "":
        print "Example: " + example

    if longdescription != "":
        print " "
        print "What will happen ?"
        print longdescription

    if len(arguments) >= 1:
        print ""
        print "Arguments"
        print "-------------------"
        print arguments

    if len(installedProgram) >= 1:
        print ""
        print "Installed Programs"
        print "-------------------"
        print installedProgram

    if len(moduleCommand) >= 1:
        print ""
        print "Modules command"
        print "-------------------"
        print moduleCommand

    if len(variables) >= 1:
        print ""
        print "Variables"
        print "-------------------"
        print variables

    if len(systemCommand) >= 1:
        print ""
        print "System command"
        print "-------------------"
        print systemCommand

    if len(fileExistsCheck) >= 1:
        print ""
        print "Files exists ?"
        print "-------------------"
        print fileExistsCheck


def saveDetailedToMarkdown():
    markdownTable = []
    markdown = ""
    headers = [fileToCheck, ""]

    if info != "":
        markdownTable.append(["Info", info])
    else:
        markdownTable.append(["Info", "[alpha] [undocumented]"])

    if description != "":
        markdownTable.append(["Description", description])

    if usage != "":
        markdownTable.append(["Usage", usage])

    if example != "":
        markdownTable.append(["Example", example])

    if len(installedProgram) >= 1:

        installString = ""
        for installed in installedProgram:
            installString += installed + ", "
        markdownTable.append(["Softwares", installString])

    if len(arguments) >= 1:
        argumentString = ""
        for argument in arguments:
            argumentString += argument + ", "
        markdownTable.append(["Arguments", argumentString])

    if len(variables) >= 1:
        variableString = ""
        for variable in variables:
            variableString += variable + ", "
        markdownTable.append(["Variables", variableString])

    if len(moduleCommand) >= 1:
        moduleString = ""
        for module in moduleCommand:
            moduleString += module + ", "
        markdownTable.append(["Modules", moduleString])

    if len(systemCommand) >= 1:
        systemString = ""
        for system in systemCommand:
            systemString += system + ", "
        markdownTable.append(["System", systemString])

    if len(fileExistsCheck) >= 1:
        fileCheckString = ""
        for filecheck in fileExistsCheck:
            fileCheckString += filecheck + ", "
        markdownTable.append(["File exists", filecheck])

    if len(longdescriptionTable) >= 1:
        for longDescription in longdescriptionTable:
            markdownTable.append(longDescription)

    markdown = tabulate(markdownTable, headers, tablefmt="pipe")
    print markdown

def saveToMarkdown():
    markdownTable = []
    markdown = ""
    headers = [fileToCheck, ""]


    if description != "":
         markdownTable.append(["Description", description])

    if example != "":
        markdownTable.append(["Example", example])

    if info != "":
        markdownTable.append(["Info", info])
    else:
        markdownTable.append(["Info", "[alpha] [undocumented]"])

    if len(arguments) >= 1:
        argumentString = ""
        for argument in arguments:
            argumentString += argument + ", "
        markdownTable.append(["Arguments", argumentString])

    markdown = tabulate(markdownTable, headers, tablefmt="pipe")
    print markdown

if len(sys.argv) == 2:
    fileToCheck = sys.argv[1]
    if os.path.isfile(fileToCheck):
        analyseFile(fileToCheck)
        saveToMarkdown()
    else:
        print "No script named" + fileToCheck
elif len(sys.argv) == 3 and sys.argv[2] == "--verbose":
    fileToCheck = sys.argv[1]
    if os.path.isfile(fileToCheck):
        analyseFile(fileToCheck)
        saveDetailedToMarkdown()
else:
    print "Usage: /system/analyseScript /pi/install"
