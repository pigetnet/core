| /do/core/string/add   |                                                                  |
|:----------------------|:-----------------------------------------------------------------|
| Info                  | [alpha] [2 args] [danger]                                        |
| Description           | Add a parameters in a configuration file                         |
| Usage                 | /do/core/string/add filename string_to_add                       |
| Example               | /do/core/string/add /string/add /boot/config.txt dtparam=i2c1=on |
| Arguments             | 1:file, 2:string_to_add,                                         |
| Variables             | file=$1, string_to_add=$2, exitcode=$?,                          |
| 1. File doesnt exists |                                                                  |

| /do/core/string/addAfterLine   |                                                                  |
|:-------------------------------|:-----------------------------------------------------------------|
| Info                           | [alpha] [undocumented]                                           |
| Usage                          | /string/addAfterLine filename addAfterString stringToReplace     |
| Example                        | /string/addAfterLine /etc/hosts raspberrypi 192.168.0.254 router |
| Arguments                      | 1:filename, 2:addAfterString, 3:stringToReplace,                 |
| Variables                      | filename=$1, addAfterString=$2, stringToReplace=$3,              |

| /do/core/string/addAfterLineIfNotExists   |                                                                            |
|:------------------------------------------|:---------------------------------------------------------------------------|
| Info                                      | [alpha] [undocumented]                                                     |
| Usage                                     | /string/addAfterLineIfNotExists Filename StringToSearch StringToAdd        |
| Example                                   | /string/addAfterLineIfNotExists /etc/hosts 127.0.0.1 127.0.0.1 raspberrypi |
| Variables                                 | lineToFind=$NewString, lineToNotFind=$NewString,                           |

| /do/core/string/addLine   |                                                                               |
|:--------------------------|:------------------------------------------------------------------------------|
| Info                      | [alpha] [undocumented]                                                        |
| Usage                     | /string/addLine Filename StringToAdd                                          |
| Example                   | /string/addLine /etc/apt/sources.list deb http://apt.pilight.org/ stable main |
| Variables                 | line=$NewString,                                                              |

| /do/core/string/eraseFromTo   |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |

| /do/core/string/eraseString   |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |

| /do/core/string/extractFromTo   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/string/extractFunction   |                        |
|:----------------------------------|:-----------------------|
| Info                              | [alpha] [undocumented] |

| /do/core/string/getAll   |                                                        |
|:-------------------------|:-------------------------------------------------------|
| Info                     | [alpha] [1 args]                                       |
| Description              | get All fields of a configuration file                 |
| Usage                    | /do/core/string/getAll filename                        |
| Example                  | /do/core/string/getAll /string/getAll /boot/config.txt |
| Arguments                | 1:file,                                                |
| Variables                | file=$1, configType=$(/string/getConfigFormat $file),  |
| 1. File doesnt exists    |                                                        |

| /do/core/string/getConfigFormat   |                        |
|:----------------------------------|:-----------------------|
| Info                              | [alpha] [undocumented] |

| /do/core/string/getJson   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/string/getLine   |                                                                                                                                                           |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                      | [alpha] [undocumented]                                                                                                                                    |
| Usage                     | /string/getLine fileToRead StringToSearch                                                                                                                 |
| Example                   | /string/getLine /etc/rc.local # Print                                                                                                                     |
| Arguments                 | 1:filename, 2:stringToSearch,                                                                                                                             |
| Variables                 | filename=$1, stringToSearch=$2, line=$(cat $filename |grep -n "$stringToSearch"|awk '{print $1}'| head -n 1), export NewString=$(echo $line|cut -d: -f1), |

| /do/core/string/removeLine   |                                     |
|:-----------------------------|:------------------------------------|
| Info                         | [alpha] [undocumented]              |
| Usage                        | removeLine Filename StringToRemove  |
| Example                      | removeLine /etc/samba/ netbios name |
| Variables                    | line=$NewString,                    |

| /do/core/string/replaceLine                                                     |                                                                                                               |
|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| Info                                                                            | [beta] [string] [avahi] [bonjour]                                                                             |
| Description                                                                     | Change name in /etc/hosts and /etc/hostname                                                                   |
| Usage                                                                           | /do/core/string/replaceLine \Filename\ \StringToSearch\ \StringToReplace\ \ElseAddAfterString\                |
| Example                                                                         | /do/core/string/replaceLine \/etc/hosts\ \127.0.0.1\ \127.0.0.1 raspberrypi\ \ff02::2         ip6-allrouters\ |
| Variables                                                                       | line=$NewString,                                                                                              |
| 1. #  In $filename : Replace l$line -- $stringToSearch... with $stringToReplace |                                                                                                               |

| /do/core/string/replaceLineIfExists   |                                                        |
|:--------------------------------------|:-------------------------------------------------------|
| Info                                  | [alpha] [undocumented]                                 |
| Usage                                 | replaceLine Filename StringToSearch StringToReplace    |
| Example                               | replaceLine /etc/hosts 127.0.0.1 127.0.0.1 raspberrypi |
| Variables                             | line=$NewString,                                       |

| /do/core/string/searchString   |                               |
|:-------------------------------|:------------------------------|
| Info                           | [alpha] [undocumented]        |
| Arguments                      | 1:file, 2:string,             |
| Variables                      | file=$1, string=$2, found=$?, |


| /do/core/string/ToAlphaNumeric   |                                                      |
|:---------------------------------|:-----------------------------------------------------|
| Info                             | [alpha] [undocumented]                               |
| Variables                        | export NewString=$(echo $1|sed 's/[^a-zA-Z0-9]//g'), |

| /do/core/string/ToNetbios              |                                                                                                   |
|:---------------------------------------|:--------------------------------------------------------------------------------------------------|
| Info                                   | [alpha] [undocumented]                                                                            |
| Variables                              | NewString=$(echo $NewString|cut -c1-16) #No more than 16 characters, export NewString=$NewString, |
| 1. No name provided RESET TO DEFAULT   |                                                                                                   |
| 2. No name provided : RESET TO DEFAULT |                                                                                                   |

| /do/core/string/Trim   |                                                  |
|:-----------------------|:-------------------------------------------------|
| Info                   | [alpha] [undocumented]                           |
| Variables              | export NewString=$(echo $1|tr -d '[[:space:]]'), |

| /do/core/string/upperToLower   |                                                         |
|:-------------------------------|:--------------------------------------------------------|
| Info                           | [alpha] [undocumented]                                  |
| Variables                      | export NewString=$(echo $1|tr '[:upper:]' '[:lower:]'), |

