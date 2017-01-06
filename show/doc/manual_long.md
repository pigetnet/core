| /do/core/show/askUser                           |                                       |
|:------------------------------------------------|:--------------------------------------|
| Info                                            | [interactive] [beta]                  |
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
| Info                          | [interactive] [whiptail] [beta]                                                                                                                                                                                                                                                                                                                                  |
| Description                   | Create a whiptail menu based on a text configuration files                                                                                                                                                                                                                                                                                                       |
| Usage                         | /show/commandMenu menuFiles                                                                                                                                                                                                                                                                                                                                      |
| Example                       | /show/commandMenu /do/buttons/menu/buttons.conf                                                                                                                                                                                                                                                                                                                  |
| Arguments                     | 1:menuConf,                                                                                                                                                                                                                                                                                                                                                      |
| Variables                     | menuConf=$1, title=$line, optionsNb=$((optionsNb+1)), optionsNb=$((optionsNb+1)), commandNb=$((commandNb+1)), menuLine=$((menuLine+1)), optionsNb=$((optionsNb+1)), optionsNb=$((optionsNb+1)), answer=$(whiptail --backtitle "PIGET MENU : madnerd.org" --title "$title" --menu "$subtitle" 0 0 0 "${options[@]}"  3>&1 1>&2 2>&3), #isnumber=$(isnum $answer), |
| Modules                       | /show/example '/show/commandMenu /do/buttons/menu/buttons.conf',                                                                                                                                                                                                                                                                                                 |
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

| /do/core/show/cpuTemp   |                                   |
|:------------------------|:----------------------------------|
| Info                    | [beta]                            |
| Description             | Display CPU temperture in celsius |
| Usage                   | /show/cpuTemp                     |

| /do/core/show/date   |                                              |
|:---------------------|:---------------------------------------------|
| Info                 | [interactive] [beta]                         |
| Description          | Display date formatted to be use in filename |
| Usage                | /show/date                                   |
| Example              | 15-00-09_01-06-2017                          |

| /do/core/show/description   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/show/dir   |                        |
|:--------------------|:-----------------------|
| Info                | [beta]                 |
| Description         | Display current folder |
| Usage               | /show/dir              |
| Example             | /usr/bin               |

| /do/core/show/displayhtml   |                                                                                                             |
|:----------------------------|:------------------------------------------------------------------------------------------------------------|
| Info                        | [http] [python] [SimpleHHTPServer] [beta]                                                                   |
| Description                 | Display a directory on port 314 (using pythonSmallServer)                                                   |
| Usage                       | /show/displayhtml                                                                                           |
| Variables                   | smbname=$(/show/smbGetName), oldpid=$(ps axf | grep "SimpleHTTPServer" | grep -v grep | awk '{print  $1}'), |
| 1. Display $1 on $smbname   |                                                                                                             |

| /do/core/show/displayhtmlStop   |                                                                                |
|:--------------------------------|:-------------------------------------------------------------------------------|
| Info                            | [http] [python] [SimpleHHTPServer] [beta]                                      |
| Description                     | Kill pythonSmallServer instances                                               |
| Usage                           | /show/displayhtmlStop                                                          |
| Example                         | /show/displayhtmlStop                                                          |
| Variables                       | oldpid=$(ps axf | grep "SimpleHTTPServer" | grep -v grep | awk '{print  $1}'), |
| 1. Killing SimpleHTTPServer     |                                                                                |

| /do/core/show/errorBox   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/example   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/file                             |                                |
|:-----------------------------------------------|:-------------------------------|
| Info                                           | [cat] [beta]                   |
| Description                                    | Display the content of a file  |
| Usage                                          | /show/file filename            |
| Example                                        | /show/file /etc/samba/smb.conf |
| Arguments                                      | 1:filename,                    |
| Variables                                      | filename=$1,                   |
| 1. ~~~~~~~~~~~~~ $1 ~~~~~~~~~~~ $PICOLOR       |                                |
| 2. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ $PICOLOR |                                |

| /do/core/show/folderSize   |                                                      |
|:---------------------------|:-----------------------------------------------------|
| Info                       | [du] [beta]                                          |
| Description                | Display the size of a folder (or the current folder) |
| Usage                      | /show/folderSize or /show/folderSize dir             |
| Example                    | /show/folderSize /etc                                |
| Arguments                  | 1:folder,                                            |
| Variables                  | folder=$1,                                           |

| /do/core/show/gpio   |                                                                        |
|:---------------------|:-----------------------------------------------------------------------|
| Info                 | [gpio] [beta]                                                          |
| Description          | Pretty gpio display                                                    |
| Usage                | /show/gpio                                                             |
| Variables            | r=$(tput setaf 1), n=$(tput sgr 0), w=$(tput bold), g=$(tput setaf 2), |

| /do/core/show/help                                             |                                                            |
|:---------------------------------------------------------------|:-----------------------------------------------------------|
| Info                                                           | [python] [analyseScript] [alpha]                           |
| Description                                                    | Automatically generate an help markdown table for a script |
| Usage                                                          | /show/help script                                          |
| Example                                                        | /show/help /pi/name                                        |
| Arguments                                                      | 1:script,                                                  |
| Variables                                                      | script=$1,                                                 |
| System                                                         | /system/python/analyseScript.py $script,                   |
| 1. Welcome to PiGet                                            |                                                            |
| 1. You can install a module using /pi/install                  |                                                            |
| 2. You can prepare your Raspberry Pi with commands inside /pi/ |                                                            |
| 3. You can rename your Raspberry with /pi/name mynewname       |                                                            |
| 4. Every modules commands are inside /do/                      |                                                            |
| 5. Modules have commands in common                             |                                                            |
| 6. /do/module/install : install module                         |                                                            |
| 7. /do/module/settings : open configuration file               |                                                            |
| 8. /do/module/setup : Interactive setup                        |                                                            |
| 9. /do/module/start : Start module                             |                                                            |
| 10. /do/module/stop : Stop module                              |                                                            |

| /do/core/show/helpVerbose   |                                                                           |
|:----------------------------|:--------------------------------------------------------------------------|
| Info                        | [python] [analyseScript] [alpha] [verbose]                                |
| Description                 | Automatically generate an help markdown table for a script (verbose mode) |
| Usage                       | /show/help script                                                         |
| Example                     | /show/help /pi/name                                                       |
| Arguments                   | 1:script,                                                                 |
| Variables                   | script=$1,                                                                |
| System                      | /system/python/analyseScript.py $script --verbose,                        |

| /do/core/show/info   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/show/ip   |                          |
|:-------------------|:-------------------------|
| Info               | [hostname] [beta]        |
| Description        | Display first IP address |
| Usage              | /show/ipAddress          |
| Example            | /show/ipAddress          |

| /do/core/show/ipAddress   |                          |
|:--------------------------|:-------------------------|
| Info                      | [hostname] [beta]        |
| Description               | Display first IP address |
| Usage                     | /show/ipAddress          |
| Example                   | /show/ipAddress          |

| /do/core/show/ipInterface   |                                                                                          |
|:----------------------------|:-----------------------------------------------------------------------------------------|
| Info                        | [ip] [beta]                                                                              |
| Description                 | Save ip address from an interface into a variable                                        |
| Usage                       | . /show/ipInterface                                                                      |
| Example                     | . /show/ipInterface eth0                                                                 |
| Arguments                   | 1:interface,                                                                             |
| Variables                   | interface=$1, ipAddr=$(ip -f inet -o addr show $interface|cut -d\  -f 7 | cut -d/ -f 1), |

| /do/core/show/ipInternet   |                               |
|:---------------------------|:------------------------------|
| Info                       | [wget] [ipecho.net] [release] |
| Description                | Show external ip              |
| Usage                      | . /show/ipInternet            |

| /do/core/show/ipList   |                      |
|:-----------------------|:---------------------|
| Info                   | [hostname] [release] |
| Description            | Show all ip address  |
| Usage                  | /show/ipList         |

| /do/core/show/ipUser   |                             |
|:-----------------------|:----------------------------|
| Info                   | [pinky] [release]           |
| Description            | Show ip of current ssh user |
| Usage                  | /show/ipUser                |

| /do/core/show/isConnected   |                                       |
|:----------------------------|:--------------------------------------|
| Info                        | [ping] [wikipedia.org] [release]      |
| Description                 | Ping a hostname or ping wikipedia.org |
| Usage                       | . /show/isConnected                   |
| Example                     | . /show/isConnected github.com        |
| Arguments                   | 1:url,                                |
| Variables                   | url=$1,                               |

| /do/core/show/isGithubRepo   |                                           |
|:-----------------------------|:------------------------------------------|
| Info                         | [curl] [github.com] [official api]        |
| Description                  | Check if a username/repo exists on github |
| Usage                        | /show/isGithubRepo                        |
| Example                      | /show/isGithubRepo ldleman yana-server    |
| Arguments                    | 1:username, 2:repo,                       |
| Variables                    | username=$1, repo=$2,                     |

| /do/core/show/isInstalled   |                                                                                       |
|:----------------------------|:--------------------------------------------------------------------------------------|
| Info                        | [dpkg] [grep] [/var/lib/dpkg/status]                                                  |
| Description                 | Check if a apt-get package is installed                                               |
| Usage                       | /show/isInstalled                                                                     |
| Example                     | /show/isInstalled samba                                                               |
| Arguments                   | 1:package,                                                                            |
| Variables                   | package=$1, check=$(grep -A1 -Fx "Package: $package" /var/lib/dpkg/status|tail -n 1), |

| /do/core/show/isIP   |                                      |
|:---------------------|:-------------------------------------|
| Info                 | [regular expression]                 |
| Description          | Check if a variable is an ip address |
| Usage                | /show/isIP                           |
| Example              | /show/isIP 192.168.0.1               |
| Arguments            | 1:ip,                                |
| Variables            | ip=$1,                               |

| /do/core/show/isPackage   |                                    |
|:--------------------------|:-----------------------------------|
| Info                      | [apt-cache]                        |
| Description               | Check if this is a apt-get package |
| Usage                     | . /show/isPackage                  |
| Example                   | . /show/isPackage samba            |
| Arguments                 | 1:package,                         |
| Variables                 | package=$1,                        |

| /do/core/show/isRoot   |                           |
|:-----------------------|:--------------------------|
| Info                   | [id]                      |
| Description            | Check if the user is root |
| Usage                  | /show/isRoot              |
| Example                | /show/isRoot              |

| /do/core/show/linebreak   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/show/listecho   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |
| 1. $1 $2                 |                        |

| /do/core/show/listUsers   |                 |
|:--------------------------|:----------------|
| Info                      | [/etc/passwd]   |
| Description               | List all users  |
| Usage                     | /show/listUsers |

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

| /do/core/show/myip   |                             |
|:---------------------|:----------------------------|
| Info                 | [pinky] [release]           |
| Description          | Show ip of current ssh user |
| Usage                | /show/ipUser                |

| /do/core/show/name   |                                                             |
|:---------------------|:------------------------------------------------------------|
| Info                 | [samba] [hostname] [beta]                                   |
| Description          | Show hostname using samba config file or hostname file      |
| Usage                | /show/name                                                  |
| Variables            | smbname=$(cat /etc/samba/smb.conf |grep "netbios name = "), |

| /do/core/show/nextline   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/nlbecho   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

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
| Info                       | [samba] [hostname] [beta]                                   |
| Description                | Show hostname using samba config file or hostname file      |
| Usage                      | /show/name                                                  |
| Variables                  | smbname=$(cat /etc/samba/smb.conf |grep "netbios name = "), |

| /do/core/show/time   |                       |
|:---------------------|:----------------------|
| Info                 | [date] [release]      |
| Description          | Show hour and minutes |
| Usage                | /show/time            |

| /do/core/show/unusedDisk   |                           |
|:---------------------------|:--------------------------|
| Info                       | [df] [release]            |
| Description                | Show remaining disk space |
| Usage                      | /show/unusedDisk          |

| /do/core/show/usage   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/show/usageDescription   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/show/userConnected   |                                              |
|:------------------------------|:---------------------------------------------|
| Info                          | [df] [release]                               |
| Description                   | Show numbers of users logged into a terminal |
| Usage                         | /show/userConnected                          |

