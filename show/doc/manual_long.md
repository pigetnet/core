| /do/core/show/askUser                           |                                       |
|:------------------------------------------------|:--------------------------------------|
| Info                                            | [interactive] [alpha]                 |
| Description                                     | Ask an question and return the answer |
| Usage                                           | Return $ASKUSER                       |
| Example                                         | . /show/askUser What Time is it?      |
| Arguments                                       | 1:question,                           |
| Variables                                       | question=$1, export ASKUSER=$answer,  |
| 1. -- Ask user: /show/messagebox /show/askUser  |                                       |
| 2. -- Ask user: /show/usage  question           |                                       |
| 3. -- Ask user: /show/example  What Time is it? |                                       |

| /do/core/show/colecho   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |
| Arguments               | 1:text, 2:color,       |
| Variables               | text=$1, color=$2,     |

| /do/core/show/commandMenu     |                                                                                                                                                                                                                                                                                                                                                                  |
|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                          | [alpha] [undocumented]                                                                                                                                                                                                                                                                                                                                           |
| Arguments                     | 1:menuConf,                                                                                                                                                                                                                                                                                                                                                      |
| Variables                     | menuConf=$1, title=$line, optionsNb=$((optionsNb+1)), optionsNb=$((optionsNb+1)), commandNb=$((commandNb+1)), menuLine=$((menuLine+1)), optionsNb=$((optionsNb+1)), optionsNb=$((optionsNb+1)), answer=$(whiptail --backtitle "PIGET MENU : madnerd.org" --title "$title" --menu "$subtitle" 0 0 0 "${options[@]}"  3>&1 1>&2 2>&3), #isnumber=$(isnum $answer), |
| 1. See you around!            |                                                                                                                                                                                                                                                                                                                                                                  |
| 1. ${commands[$answer]}       |                                                                                                                                                                                                                                                                                                                                                                  |
| 2. ${commands[$answer]}       |                                                                                                                                                                                                                                                                                                                                                                  |
| 1. Cant find menu : $menuConf |                                                                                                                                                                                                                                                                                                                                                                  |

| /do/core/show/console   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/continuePrompt   |                        |
|:-------------------------------|:-----------------------|
| Info                           | [alpha] [undocumented] |
| 1. Stopped... $info            |                        |

| /do/core/show/cpuTemp   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/date   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/show/description   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/show/dir   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |

| /do/core/show/displayhtml   |                                                                                                             |
|:----------------------------|:------------------------------------------------------------------------------------------------------------|
| Info                        | [alpha] [undocumented]                                                                                      |
| Variables                   | smbname=$(/show/smbGetName), oldpid=$(ps axf | grep "SimpleHTTPServer" | grep -v grep | awk '{print  $1}'), |
| 1. Display $1 on $smbname   |                                                                                                             |

| /do/core/show/displayhtmlStop   |                                                                                |
|:--------------------------------|:-------------------------------------------------------------------------------|
| Info                            | [alpha] [undocumented]                                                         |
| Variables                       | oldpid=$(ps axf | grep "SimpleHTTPServer" | grep -v grep | awk '{print  $1}'), |
| 1. Killing SimpleHTTPServer     |                                                                                |

| /do/core/show/errorBox   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/example   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/file                             |                        |
|:-----------------------------------------------|:-----------------------|
| Info                                           | [alpha] [undocumented] |
| 1. ~~~~~~~~~~~~~ $1 ~~~~~~~~~~~ $PICOLOR       |                        |
| 2. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ $PICOLOR |                        |

| /do/core/show/folderSize   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |
| Arguments                  | 1:folder,              |
| Variables                  | folder=$1,             |

| /do/core/show/gpio   |                                                                        |
|:---------------------|:-----------------------------------------------------------------------|
| Info                 | [alpha] [undocumented]                                                 |
| Variables            | r=$(tput setaf 1), n=$(tput sgr 0), w=$(tput bold), g=$(tput setaf 2), |

| /do/core/show/help                                       |                                                                                                                  |
|:---------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| Info                                                     | [alpha] [undocumented]                                                                                           |
| Arguments                                                | 1:script,                                                                                                        |
| Variables                                                | script=$1,                                                                                                       |
| System                                                   | /system/python/analyseScript.py $script, /show/listecho "You can install a module using /system/downloadModule", |
| 1. Welcome to PiGet                                      |                                                                                                                  |
| 1. You can install a module using /system/downloadModule |                                                                                                                  |
| 2. You can prepare your Raspberry Pi with /pi/           |                                                                                                                  |
| 3. You can rename your Raspberry with /pi/name mynewname |                                                                                                                  |
| 4. Every modules commands are inside /do/                |                                                                                                                  |
| 5. Modules have commands in common                       |                                                                                                                  |
| 6. /do/module/install : install module                   |                                                                                                                  |
| 7. /do/module/settings : open configuration file         |                                                                                                                  |
| 8. /do/module/setup : Interactive setup                  |                                                                                                                  |
| 9. /do/module/start : Start module                       |                                                                                                                  |
| 10. /do/module/stop : Stop module                        |                                                                                                                  |

| /do/core/show/helpVerbose                                |                                                                                                                            |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| Info                                                     | [alpha] [undocumented]                                                                                                     |
| Arguments                                                | 1:script,                                                                                                                  |
| Variables                                                | script=$1,                                                                                                                 |
| System                                                   | /system/python/analyseScript.py $script --verbose, /show/listecho "You can install a module using /system/downloadModule", |
| 1. Welcome to PiGet                                      |                                                                                                                            |
| 1. You can install a module using /system/downloadModule |                                                                                                                            |
| 2. You can prepare your Raspberry Pi with /pi/           |                                                                                                                            |
| 3. You can rename your Raspberry with /pi/name mynewname |                                                                                                                            |
| 4. Every modules commands are inside /do/                |                                                                                                                            |
| 5. Modules have commands in common                       |                                                                                                                            |
| 6. /do/module/install : install module                   |                                                                                                                            |
| 7. /do/module/settings : open configuration file         |                                                                                                                            |
| 8. /do/module/setup : Interactive setup                  |                                                                                                                            |
| 9. /do/module/start : Start module                       |                                                                                                                            |
| 10. /do/module/stop : Stop module                        |                                                                                                                            |

| /do/core/show/info   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/show/ipAddress   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/show/ipInterface   |                                                                                          |
|:----------------------------|:-----------------------------------------------------------------------------------------|
| Info                        | [alpha] [undocumented]                                                                   |
| Arguments                   | 1:interface,                                                                             |
| Variables                   | interface=$1, ipAddr=$(ip -f inet -o addr show $interface|cut -d\  -f 7 | cut -d/ -f 1), |

| /do/core/show/ipInternet   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/show/ipList   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/show/ipUser   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/show/isConnected   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |
| Arguments                   | 1:url,                 |
| Variables                   | url=$1,                |

| /do/core/show/isGithubRepo   |                        |
|:-----------------------------|:-----------------------|
| Info                         | [alpha] [undocumented] |
| Arguments                    | 1:username, 2:repo,    |
| Variables                    | username=$1, repo=$2,  |

| /do/core/show/isInstalled   |                                                                     |
|:----------------------------|:--------------------------------------------------------------------|
| Info                        | [alpha] [undocumented]                                              |
| Variables                   | check=$(grep -A1 -Fx "Package: $1" /var/lib/dpkg/status|tail -n 1), |

| /do/core/show/isIP   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |
| Arguments            | 1:ip,                  |
| Variables            | ip=$1,                 |

| /do/core/show/isPackage   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/show/isRoot   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/show/linebreak   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/show/listecho   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |
| 1. $1 $2                 |                        |

| /do/core/show/listUsers   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/show/log   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |

| /do/core/show/messagebox   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/show/minibox_ERROR   |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |

| /do/core/show/minibox_OK   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/show/minibox_SKIP   |                        |
|:-----------------------------|:-----------------------|
| Info                         | [alpha] [undocumented] |

| /do/core/show/minibox_WARNING   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/show/modules   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/myip   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/show/name   |                                                             |
|:---------------------|:------------------------------------------------------------|
| Info                 | [alpha] [undocumented]                                      |
| Variables            | smbname=$(cat /etc/samba/smb.conf |grep "netbios name = "), |

| /do/core/show/nextline   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/nlbecho   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/programs           |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |
| 1. Processes --- PID --- Command |                        |

| /do/core/show/return   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/show/sambaFolder   |                                                                                                                                                                        |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                        | [alpha] [undocumented]                                                                                                                                                 |
| Arguments                   | 1:current_folder,                                                                                                                                                      |
| Variables                   | current_folder=$PWD, current_folder=$1, first=$(echo "$current_folder" | cut -d "/" -f2), second=$(echo "$current_folder" | cut -d "/" -f3), name=$(/show/smbGetName), |

| /do/core/show/smbGetName   |                                                             |
|:---------------------------|:------------------------------------------------------------|
| Info                       | [alpha] [undocumented]                                      |
| Variables                  | smbname=$(cat /etc/samba/smb.conf |grep "netbios name = "), |

| /do/core/show/state   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |
| Arguments             | 1:module,              |
| Variables             | module=$1,             |

| /do/core/show/time   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/show/unusedDisk   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/show/usage   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/show/usageDescription   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/show/userConnected   |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |

| /do/core/show/wifiManufacturer   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

