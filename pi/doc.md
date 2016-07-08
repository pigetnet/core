| /pi/install   |                                                                  |
|:--------------|:-----------------------------------------------------------------|
| Info          | [beta]                                                           |
| Description   | Download a module at github.com/pigetnet and install it          |
| Usage         | /pi/install module                                               |
| Example       | /pi/install samba                                                |
| Arguments     | 1:moduleName,                                                    |
| Variables     | moduleName=$1,                                                   |
| Modules       | if [ -e /do/$moduleName/install ];then, /do/$moduleName/install, |
| System        | /system/downloadModule $moduleName,                              |

| /pi/installWiringPi                               |                           |
|:--------------------------------------------------|:--------------------------|
| Info                                              | [alpha] [undocumented]    |
| Softwares                                         | git-core,                 |
| System                                            | /system/install git-core, |
| 1. WiringPi Pi Installation                       |                           |
| 2. /opt/wiringPi/                                 |                           |
| 3. WiringPi installed!                            |                           |
| 4. gcc program.cpp -o program -lwiringPi $PICOLOR |                           |

| /pi/installWiringPiPython          |                                                         |
|:-----------------------------------|:--------------------------------------------------------|
| Info                               | [alpha] [undocumented]                                  |
| Softwares                          | python-dev, python-pip,                                 |
| System                             | /system/install python-dev, /system/install python-pip, |
| 1. Install WiringPi 2 (for python) |                                                         |

| /pi/ledBlink   |                          |
|:---------------|:-------------------------|
| Info           | [release]                |
| Description    | Make the green led blink |
| Usage          | /pi/ledBlink             |

| /pi/ledOff   |                        |
|:-------------|:-----------------------|
| Info         | [release]              |
| Description  | Turn off the green led |
| Usage        | /pi/ledOff             |

| /pi/ledOn   |                       |
|:------------|:----------------------|
| Info        | [release]             |
| Description | Turn on the green led |
| Usage       | /pi/ledOn             |

| /pi/ledReset   |                                        |
|:---------------|:---------------------------------------|
| Info           | [release]                              |
| Description    | Reset the green led to SDcard activity |
| Usage          | /pi/ledReset                           |

| /pi/linker   |                                                  |
|:-------------|:-------------------------------------------------|
| Info         | [beta] [2 args]                                  |
| Description  | create a link to a command inside /usr/local/bin |
| Usage        | /pi/linker command link                          |
| Example      | /pi/linker /pi/ledOn turn_on_led                 |
| Arguments    | 1:scriptToLink, 2:link,                          |
| Variables    | scriptToLink=$1, link=$2,                        |

| /pi/make                                    |                                                         |
|:--------------------------------------------|:--------------------------------------------------------|
| Info                                        | [alpha] [undocumented]                                  |
| Description                                 | Launch install script at /boot/piget/scripts/install.sh |
| Usage                                       | /pi/make                                                |
| Example                                     | /pi/make                                                |
| 1. Starting project                         |                                                         |
| 1. Launching /boot/piget/scripts/install.sh |                                                         |
| 2. You can download one with /pi/download   |                                                         |

| /pi/name                             |                                                                                                                     |
|:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| Info                                 | [alpha] [undocumented]                                                                                              |
| Description                          | Rename your Raspberry Pi using avahi/samba                                                                          |
| Usage                                | /pi/name [newname] (default:/boot/piget/config/name.txt)                                                            |
| Example                              | /pi/name raspberrypi                                                                                                |
| Softwares                            | samba, avahi-daemon,                                                                                                |
| Arguments                            | 1:NEW_HOSTNAME,                                                                                                     |
| Variables                            | NEW_HOSTNAME=$(cat /boot/piget/config/name.txt), NEW_HOSTNAME=$NewString, NEW_HOSTNAME=$1, NEW_HOSTNAME=$NewString, |
| System                               | /system/install samba, /system/install avahi-daemon, /system/restart samba,                                         |
| 1. Raspberry Pi Name : $NEW_HOSTNAME |                                                                                                                     |
| 1. Using /boot/piget/config/name.txt |                                                                                                                     |
| 2. Raspberry Pi Name : $NEW_HOSTNAME |                                                                                                                     |
| 3. Samba Name : $NEW_HOSTNAME        |                                                                                                                     |

| /pi/prepare   |                        |
|:--------------|:-----------------------|
| Info          | [alpha] [undocumented] |

| /pi/readme.md   |                        |
|:----------------|:-----------------------|
| Info            | [alpha] [undocumented] |

| /pi/removeDefaultUser                                                                            |                                                                               |
|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| Info                                                                                             | [alpha] [undocumented]                                                        |
| Description                                                                                      | Remove pi user (if it is not logged)                                          |
| Usage                                                                                            | /pi/removeDefaultUser                                                         |
| Example                                                                                          | /pi/removeDefaultUser                                                         |
| Variables                                                                                        | isRootEnable=$(passwd -S|awk '{print $2}'),                                   |
| System                                                                                           | /system/removeAccount pi, /system/scriptOnNextReboot "/pi/removeDefaultUser", |
| 1. ROOT IS NOT ENABLE, ERASING DEFAULT ACCOUNT WILL BLOCKED YOU FROM ACCESSING YOUR RASPBERRY PI |                                                                               |

| /pi/removeDesktop              |                                                                           |
|:-------------------------------|:--------------------------------------------------------------------------|
| Info                           | [alpha] [undocumented]                                                    |
| Description                    | Remove all desktop applications (WARNING THIS TAKES MORE THAN 30 MINUTES) |
| Usage                          | /pi/removeDesktop                                                         |
| Example                        | /pi/removeDesktop                                                         |
| 1. Remove Desktop applications |                                                                           |
| 1. This can take a long time   |                                                                           |

| /pi/removeRaspiNotice   |                                                 |
|:------------------------|:------------------------------------------------|
| Info                    | [release]                                       |
| Description             | remove notice to use raspi-config on connection |
| Usage                   | /pi/removeRaspiNotice                           |

| /pi/resizeSD   |                                                               |
|:---------------|:--------------------------------------------------------------|
| Info           | [release] [reboot]                                            |
| Description    | Expand SDcard on next boot using raspi-config unattended mode |
| Usage          | /pi/resizeSD                                                  |

| /pi/timeZone         |                         |
|:---------------------|:------------------------|
| Info                 | [release] [interactive] |
| Description          | Modify timezone         |
| Usage                | /pi/timeZone            |
| 1. Settings timezone |                         |

| /pi/update                          |                          |
|:------------------------------------|:-------------------------|
| Info                                | [beta] [long]            |
| Description                         | Update apt-get and Piget |
| Usage                               | /pi/update               |
| 1. Update everything                |                          |
| 1. Update Applications with apt-get |                          |
| 2. Update PiGet                     |                          |

| /pi/updateAllGitRepo                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                                 | [alpha] [caution]                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Description                                          | Update all git repositories on the system                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Usage                                                | /pi/updateAllGitRepo                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Variables                                            | d=$(dirname $d), cd "$d" && remoteUrl=$(cat ./.git/config |grep "url"|awk '{print $3}'), cd "$d" && remoteHash=$(git ls-remote $remoteUrl|head -n1|awk '{print $1}'), cd "$d" && localHash=$(git rev-parse origin/master), fetchStatus=$?, cd "$d" && lastcomment=$(git reset --hard origin/master | awk '{$1="";$2="";$3="";$4="";$5="";print $0;}') > /dev/null 2>&1, resetStatus=$?, cd "$d" && pullLog=$(git pull origin master) > /dev/null 2>&1, pullStatus=$?, |
| 1. PIGET : Update all git repositories on the system |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1. COMMENT - $lastcomment                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2. Warning message from git pull                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| /pi/updateGitRepo                |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                             | [alpha] [undocumented]                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Arguments                        | 1:d,                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Variables                        | d=$1, cd "$d" && remoteUrl=$(cat ./.git/config |grep "url"|awk '{print $3}'), cd "$d" && remoteHash=$(git ls-remote $remoteUrl|head -n1|awk '{print $1}'), cd "$d" && localHash=$(git rev-parse origin/master), fetchStatus=$?, cd "$d" && lastcomment=$(git reset --hard origin/master | awk '{$1="";$2="";$3="";$4="";$5="";print $0;}') > /dev/null 2>&1, resetStatus=$?, cd "$d" && pullLog=$(git pull origin master) > /dev/null 2>&1, pullStatus=$?, |
| 1. COMMENT - $lastcomment        |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2. Warning message from git pull |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

| /pi/updatePiget                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                      | [beta] [caution]                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Description                               | Update all piget modules (this can erase changes)                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Usage                                     | /pi/updatePiget                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Variables                                 | moduleName=$(basename "${D}"), cd "${D}" && remoteUrl=$(cat ./.git/config |grep "url"|awk '{print $3}'), cd "${D}" && remoteHash=$(git ls-remote $remoteUrl|head -n1|awk '{print $1}'), cd "${D}" && localHash=$(git rev-parse origin/master), fetchStatus=$?, cd "${D}" && lastcomment=$(git reset --hard origin/master | awk '{$1="";$2="";$3="";$4="";$5="";print $0;}') > /dev/null 2>&1, resetStatus=$?, cd "${D}" && pullLog=$(git pull origin master) > /dev/null 2>&1, pullStatus=$?, |
| System                                    | #/system/downloadModule $moduleName,                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 1. PIGET : Update all modules             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 1. COMMENT - $lastcomment                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2. Warning message from git pull          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 3. Module $moduleName not saved or broken |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

