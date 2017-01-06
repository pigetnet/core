| /do/core/show/askUser   |                                       |
|:------------------------|:--------------------------------------|
| Description             | Ask an question and return the answer |
| Example                 | . /show/askUser What Time is it?      |
| Info                    | [interactive] [beta]                  |
| Arguments               | 1:question,                           |

| /do/core/show/colecho   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |
| Arguments               | 1:text, 2:color,       |

| /do/core/show/commandMenu   |                                                            |
|:----------------------------|:-----------------------------------------------------------|
| Description                 | Create a whiptail menu based on a text configuration files |
| Example                     | /show/commandMenu /do/buttons/menu/buttons.conf            |
| Info                        | [interactive] [whiptail] [beta]                            |
| Arguments                   | 1:menuConf,                                                |

| /do/core/show/console   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/continuePrompt   |                        |
|:-------------------------------|:-----------------------|
| Info                           | [alpha] [undocumented] |

| /do/core/show/cpuTemp   |                                   |
|:------------------------|:----------------------------------|
| Description             | Display CPU temperture in celsius |
| Info                    | [beta]                            |

| /do/core/show/date   |                                              |
|:---------------------|:---------------------------------------------|
| Description          | Display date formatted to be use in filename |
| Example              | 15-00-09_01-06-2017                          |
| Info                 | [interactive] [beta]                         |

| /do/core/show/description   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/show/dir   |                        |
|:--------------------|:-----------------------|
| Description         | Display current folder |
| Example             | /usr/bin               |
| Info                | [beta]                 |

| /do/core/show/displayhtml   |                                                           |
|:----------------------------|:----------------------------------------------------------|
| Description                 | Display a directory on port 314 (using pythonSmallServer) |
| Info                        | [http] [python] [SimpleHHTPServer] [beta]                 |

| /do/core/show/displayhtmlStop   |                                           |
|:--------------------------------|:------------------------------------------|
| Description                     | Kill pythonSmallServer instances          |
| Example                         | /show/displayhtmlStop                     |
| Info                            | [http] [python] [SimpleHHTPServer] [beta] |

| /do/core/show/errorBox   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/example   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/file   |                                |
|:---------------------|:-------------------------------|
| Description          | Display the content of a file  |
| Example              | /show/file /etc/samba/smb.conf |
| Info                 | [cat] [beta]                   |
| Arguments            | 1:filename,                    |

| /do/core/show/folderSize   |                                                      |
|:---------------------------|:-----------------------------------------------------|
| Description                | Display the size of a folder (or the current folder) |
| Example                    | /show/folderSize /etc                                |
| Info                       | [du] [beta]                                          |
| Arguments                  | 1:folder,                                            |

| /do/core/show/gpio   |                     |
|:---------------------|:--------------------|
| Description          | Pretty gpio display |
| Info                 | [gpio] [beta]       |

| /do/core/show/help   |                                                            |
|:---------------------|:-----------------------------------------------------------|
| Description          | Automatically generate an help markdown table for a script |
| Example              | /show/help /pi/name                                        |
| Info                 | [python] [analyseScript] [alpha]                           |
| Arguments            | 1:script,                                                  |

| /do/core/show/helpVerbose   |                                                                           |
|:----------------------------|:--------------------------------------------------------------------------|
| Description                 | Automatically generate an help markdown table for a script (verbose mode) |
| Example                     | /show/help /pi/name                                                       |
| Info                        | [python] [analyseScript] [alpha] [verbose]                                |
| Arguments                   | 1:script,                                                                 |

| /do/core/show/info   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/show/ip   |                          |
|:-------------------|:-------------------------|
| Description        | Display first IP address |
| Example            | /show/ipAddress          |
| Info               | [hostname] [beta]        |

| /do/core/show/ipAddress   |                          |
|:--------------------------|:-------------------------|
| Description               | Display first IP address |
| Example                   | /show/ipAddress          |
| Info                      | [hostname] [beta]        |

| /do/core/show/ipInterface   |                                                   |
|:----------------------------|:--------------------------------------------------|
| Description                 | Save ip address from an interface into a variable |
| Example                     | . /show/ipInterface eth0                          |
| Info                        | [ip] [beta]                                       |
| Arguments                   | 1:interface,                                      |

| /do/core/show/ipInternet   |                               |
|:---------------------------|:------------------------------|
| Description                | Show external ip              |
| Info                       | [wget] [ipecho.net] [release] |

| /do/core/show/ipList   |                      |
|:-----------------------|:---------------------|
| Description            | Show all ip address  |
| Info                   | [hostname] [release] |

| /do/core/show/ipUser   |                             |
|:-----------------------|:----------------------------|
| Description            | Show ip of current ssh user |
| Info                   | [pinky] [release]           |

| /do/core/show/isConnected   |                                       |
|:----------------------------|:--------------------------------------|
| Description                 | Ping a hostname or ping wikipedia.org |
| Example                     | . /show/isConnected github.com        |
| Info                        | [ping] [wikipedia.org] [release]      |
| Arguments                   | 1:url,                                |

| /do/core/show/isGithubRepo   |                                           |
|:-----------------------------|:------------------------------------------|
| Description                  | Check if a username/repo exists on github |
| Example                      | /show/isGithubRepo ldleman yana-server    |
| Info                         | [curl] [github.com] [official api]        |
| Arguments                    | 1:username, 2:repo,                       |

| /do/core/show/isInstalled   |                                         |
|:----------------------------|:----------------------------------------|
| Description                 | Check if a apt-get package is installed |
| Example                     | /show/isInstalled samba                 |
| Info                        | [dpkg] [grep] [/var/lib/dpkg/status]    |
| Arguments                   | 1:package,                              |

| /do/core/show/isIP   |                                      |
|:---------------------|:-------------------------------------|
| Description          | Check if a variable is an ip address |
| Example              | /show/isIP 192.168.0.1               |
| Info                 | [regular expression]                 |
| Arguments            | 1:ip,                                |

| /do/core/show/isPackage   |                                    |
|:--------------------------|:-----------------------------------|
| Description               | Check if this is a apt-get package |
| Example                   | . /show/isPackage samba            |
| Info                      | [apt-cache]                        |
| Arguments                 | 1:package,                         |

| /do/core/show/isRoot   |                           |
|:-----------------------|:--------------------------|
| Description            | Check if the user is root |
| Example                | /show/isRoot              |
| Info                   | [id]                      |

| /do/core/show/linebreak   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/show/listecho   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/listUsers   |                |
|:--------------------------|:---------------|
| Description               | List all users |
| Info                      | [/etc/passwd]  |

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
| Description          | Show ip of current ssh user |
| Info                 | [pinky] [release]           |

| /do/core/show/name   |                                                        |
|:---------------------|:-------------------------------------------------------|
| Description          | Show hostname using samba config file or hostname file |
| Info                 | [samba] [hostname] [beta]                              |

| /do/core/show/nextline   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/show/nlbecho   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/show/return   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/show/sambaFolder   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |
| Arguments                   | 1:current_folder,      |

| /do/core/show/smbGetName   |                                                        |
|:---------------------------|:-------------------------------------------------------|
| Description                | Show hostname using samba config file or hostname file |
| Info                       | [samba] [hostname] [beta]                              |

| /do/core/show/time   |                       |
|:---------------------|:----------------------|
| Description          | Show hour and minutes |
| Info                 | [date] [release]      |

| /do/core/show/unusedDisk   |                           |
|:---------------------------|:--------------------------|
| Description                | Show remaining disk space |
| Info                       | [df] [release]            |

| /do/core/show/usage   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/show/usageDescription   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/show/userConnected   |                                              |
|:------------------------------|:---------------------------------------------|
| Description                   | Show numbers of users logged into a terminal |
| Info                          | [df] [release]                               |

