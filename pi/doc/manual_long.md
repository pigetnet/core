| /do/core/pi/delayedCommand   |                        |
|:-----------------------------|:-----------------------|
| Info                         | [alpha] [undocumented] |

| /do/core/pi/getBoard   |                                                                   |
|:-----------------------|:------------------------------------------------------------------|
| Info                   | [alpha] [undocumented]                                            |
| Variables              | hardware=$(cat  /proc/cpuinfo |grep "Hardware"|awk '{print $3}'), |

| /do/core/pi/install   |                                                                  |
|:----------------------|:-----------------------------------------------------------------|
| Info                  | [beta]                                                           |
| Description           | Download a module at github.com/pigetnet and install it          |
| Usage                 | /do/core/pi/install module                                       |
| Example               | /do/core/pi/install samba                                        |
| Arguments             | 1:moduleName,                                                    |
| Variables             | moduleName=$1,                                                   |
| Modules               | if [ -e /do/$moduleName/install ];then, /do/$moduleName/install, |
| System                | /system/downloadModule $moduleName,                              |

| /do/core/pi/installNodeJS    |                         |
|:-----------------------------|:------------------------|
| Info                         | [alpha] [undocumented]  |
| Softwares                    | node,                   |
| Variables                    | nodeversion=$(node -v), |
| System                       | /system/install node,   |
| 1. Install nodejs (adafruit) |                         |
| 3. Node version $nodeversion |                         |

| /do/core/pi/ledBlink                                |                          |
|:----------------------------------------------------|:-------------------------|
| Info                                                | [release]                |
| Description                                         | Make the green led blink |
| Usage                                               | /do/core/pi/ledBlink     |
| 1. As for now This doesnt works on a Raspberry Pi 3 |                          |
| 2. try /pi/update to see if the issue is resolved   |                          |

| /do/core/pi/ledOff                                |                        |
|:--------------------------------------------------|:-----------------------|
| Info                                              | [release] [orangepi]   |
| Description                                       | Turn off the green led |
| Usage                                             | /do/core/pi/ledOff     |
| 1. This doesnt seems to works on your board       |                        |
| 2. try /pi/update to see if the issue is resolved |                        |

| /do/core/pi/ledOn                                 |                       |
|:--------------------------------------------------|:----------------------|
| Info                                              | [release] [orangepi]  |
| Description                                       | Turn on the green led |
| Usage                                             | /do/core/pi/ledOn     |
| 1. This doesnt seems to works on your board       |                       |
| 2. try /pi/update to see if the issue is resolved |                       |

| /do/core/pi/ledReset                              |                                        |
|:--------------------------------------------------|:---------------------------------------|
| Info                                              | [release] [orangepi]                   |
| Description                                       | Reset the green led to SDcard activity |
| Usage                                             | /do/core/pi/ledReset                   |
| 1. As for now This doesnt works on your board     |                                        |
| 2. try /pi/update to see if the issue is resolved |                                        |

| /do/core/pi/linker   |                                                  |
|:---------------------|:-------------------------------------------------|
| Info                 | [beta] [2 args]                                  |
| Description          | create a link to a command inside /usr/local/bin |
| Usage                | /do/core/pi/linker command link                  |
| Example              | /do/core/pi/linker /pi/ledOn turn_on_led         |
| Arguments            | 1:scriptToLink, 2:link,                          |
| Variables            | scriptToLink=$1, link=$2,                        |

| /do/core/pi/list      |                             |
|:----------------------|:----------------------------|
| Info                  | [alpha] [undocumented]      |
| System                | /system/getRepo "pigetnet", |
| 1. Availables modules |                             |

| /do/core/pi/logBook                          |                                                                                                                          |
|:---------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| Info                                         | [alpha] [undocumented]                                                                                                   |
| Softwares                                    | dos2unix,                                                                                                                |
| Variables                                    | wifi=$(/net/isWifi), name=$(/show/name), modules=$(/show/modules), timeStamp=$(date), ip_eth0=$ipAddr, ip_wlan0=$ipAddr, |
| System                                       | /system/install dos2unix,                                                                                                |
| 1. [CREATE LOG] /boot/logBook.txt            |                                                                                                                          |
| 1. Type nano /boot/logBook.txt to modify log |                                                                                                                          |

| /do/core/pi/logTerminal   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/pi/modules   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/pi/name                          |                                                                                                                                                         |
|:------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                      | [beta]                                                                                                                                                  |
| Description                               | Rename your Raspberry Pi using avahi/samba                                                                                                              |
| Usage                                     | /do/core/pi/name [newname] (default:/user/settings/pi/name.txt)                                                                                         |
| Example                                   | /do/core/pi/name raspberrypi                                                                                                                            |
| Softwares                                 | samba, avahi-daemon,                                                                                                                                    |
| Arguments                                 | 1:NEW_HOSTNAME,                                                                                                                                         |
| Variables                                 | OLD_HOSTNAME=$(/show/smbGetName), NEW_HOSTNAME=$OLD_HOSTNAME, NEW_HOSTNAME=$(cat /user/settings/pi/name.txt), NEW_HOSTNAME=$1, NEW_HOSTNAME=$NewString, |
| System                                    | /system/install samba, /system/install avahi-daemon, /system/restart samba,                                                                             |
| 1. [Name] $OLD_HOSTNAME --> $NEW_HOSTNAME |                                                                                                                                                         |
| 1. #  Samba Name : $NEW_HOSTNAME $1       |                                                                                                                                                         |

| /do/core/pi/pinOut   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/pi/prepare   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/pi/readme.md   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/pi/removeDefaultUser                                                                    |                                                                               |
|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| Info                                                                                             | [alpha] [undocumented]                                                        |
| Description                                                                                      | Remove pi user (if it is not logged)                                          |
| Usage                                                                                            | /pi/removeDefaultUser                                                         |
| Example                                                                                          | /pi/removeDefaultUser                                                         |
| Variables                                                                                        | isRootEnable=$(passwd -S|awk '{print $2}'),                                   |
| System                                                                                           | /system/removeAccount pi, /system/scriptOnNextReboot "/pi/removeDefaultUser", |
| 1. ROOT IS NOT ENABLE, ERASING DEFAULT ACCOUNT WILL BLOCKED YOU FROM ACCESSING YOUR RASPBERRY PI |                                                                               |

| /do/core/pi/removeDesktop      |                                                                           |
|:-------------------------------|:--------------------------------------------------------------------------|
| Info                           | [alpha] [undocumented]                                                    |
| Description                    | Remove all desktop applications (WARNING THIS TAKES MORE THAN 30 MINUTES) |
| Usage                          | /pi/removeDesktop                                                         |
| Example                        | /pi/removeDesktop                                                         |
| 1. Remove Desktop applications |                                                                           |
| 1. This can take a long time   |                                                                           |

| /do/core/pi/removeRaspiNotice   |                                                 |
|:--------------------------------|:------------------------------------------------|
| Info                            | [release]                                       |
| Description                     | remove notice to use raspi-config on connection |
| Usage                           | /do/core/pi/removeRaspiNotice                   |

| /do/core/pi/resizeSD   |                                                               |
|:-----------------------|:--------------------------------------------------------------|
| Info                   | [release] [reboot] [danger]                                   |
| Description            | Expand SDcard on next boot using raspi-config unattended mode |
| Usage                  | /do/core/pi/resizeSD                                          |
| Variables              | unusedDisk=$(/show/unusedDisk),                               |

| /do/core/pi/setup            |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                         | [alpha] [undocumented]                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Variables                    | HOSTNAME=$(cat /etc/hostname), newHostname=$(whiptail --title "Prepare your Raspberry Pi" --inputbox "Current name: $HOSTNAME" --title "Name" 0 0 3>&1 1>&2 2>&3), newPassword=$(whiptail --title "Prepare your Raspberry Pi" --inputbox "User: pi" --title "Terminal password" 0 0 3>&1 1>&2 2>&3), currentColor=$(/system/getColor), optionsColor=$(whiptail --title "Prepare your Raspberry Pi" --menu "Current Color:$currentColor" 0 0 0 \, |
| System                       | /system/password pi $newPassword, currentColor=$(/system/getColor), /system/changeColor $optionsColor,                                                                                                                                                                                                                                                                                                                                           |
| 1. Prepare your Raspberry Pi |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

| /do/core/pi/start   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |

| /do/core/pi/syncFile                   |                                                          |
|:---------------------------------------|:---------------------------------------------------------|
| Info                                   | [alpha] [WIP] [danger] [dev]                             |
| Description                            | Save configuration file into /user/settings/pi/files     |
| Usage                                  | /do/core/pi/syncFile /etc/samba/smb.conf                 |
| Arguments                              | 1:file,                                                  |
| Variables                              | file=$1, filename=$(basename $1), dirname=$(dirname $1), |
| 1. $file ==> /user/settings/files$file |                                                          |

| /do/core/pi/syncFromUser                |                                 |
|:----------------------------------------|:--------------------------------|
| Info                                    | [alpha] [WIP] [danger] [dev]    |
| Description                             | Sync /user/settings/pi/* into / |
| Usage                                   | /do/core/pi/syncFromUser        |
| 1. Sync Configuration : /user ==> LOCAL |                                 |

| /do/core/pi/syncToUser                 |                                         |
|:---------------------------------------|:----------------------------------------|
| Info                                   | [alpha] [WIP] [danger] [dev]            |
| Description                            | Sync backed-up configuration into /user |
| Usage                                  | /do/core/pi/syncToUser                  |
| Variables                              | FILES=$(find ./ -type f -name '*.*'),   |
| 1. Sync Configuration : LOCAL ==> user |                                         |

| /do/core/pi/timeZone   |                         |
|:-----------------------|:------------------------|
| Info                   | [release] [interactive] |
| Description            | Modify timezone         |
| Usage                  | /do/core/pi/timeZone    |
| 1. Settings timezone   |                         |

| /do/core/pi/update                  |                          |
|:------------------------------------|:-------------------------|
| Info                                | [beta] [long]            |
| Description                         | Update apt-get and Piget |
| Usage                               | /do/core/pi/update       |
| 1. Update everything                |                          |
| 1. Update Applications with apt-get |                          |
| 2. Update PiGet                     |                          |

| /do/core/pi/updateAllGitRepo                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                                 | [alpha] [caution]                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Description                                          | Update all git repositories on the system                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Usage                                                | /do/core/pi/updateAllGitRepo                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Variables                                            | d=$(dirname $d), cd "$d" && remoteUrl=$(cat ./.git/config |grep "url"|awk '{print $3}'), cd "$d" && remoteHash=$(git ls-remote $remoteUrl|head -n1|awk '{print $1}'), cd "$d" && localHash=$(git rev-parse origin/master), fetchStatus=$?, cd "$d" && lastcomment=$(git reset --hard origin/master | awk '{$1="";$2="";$3="";$4="";$5="";print $0;}') > /dev/null 2>&1, resetStatus=$?, cd "$d" && pullLog=$(git pull origin master) > /dev/null 2>&1, pullStatus=$?, |
| 1. PIGET : Update all git repositories on the system |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1. COMMENT - $lastcomment                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2. Warning message from git pull                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| /do/core/pi/updateGitRepo        |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                             | [alpha] [undocumented]                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Arguments                        | 1:d,                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Variables                        | d=$1, cd "$d" && remoteUrl=$(cat ./.git/config |grep "url"|awk '{print $3}'), cd "$d" && remoteHash=$(git ls-remote $remoteUrl|head -n1|awk '{print $1}'), cd "$d" && localHash=$(git rev-parse origin/master), fetchStatus=$?, cd "$d" && lastcomment=$(git reset --hard origin/master | awk '{$1="";$2="";$3="";$4="";$5="";print $0;}') > /dev/null 2>&1, resetStatus=$?, cd "$d" && pullLog=$(git pull origin master) > /dev/null 2>&1, pullStatus=$?, |
| 1. COMMENT - $lastcomment        |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2. Warning message from git pull |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

| /do/core/pi/updatePiget                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                      | [beta] [caution]                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Description                               | Update all piget modules (this can erase changes)                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Usage                                     | /do/core/pi/updatePiget                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Variables                                 | moduleName=$(basename "${D}"), cd "${D}" && remoteUrl=$(cat ./.git/config |grep "url"|awk '{print $3}'), cd "${D}" && remoteHash=$(git ls-remote $remoteUrl|head -n1|awk '{print $1}'), cd "${D}" && localHash=$(git rev-parse origin/master), fetchStatus=$?, cd "${D}" && lastcomment=$(git reset --hard origin/master | awk '{$1="";$2="";$3="";$4="";$5="";print $0;}') > /dev/null 2>&1, resetStatus=$?, cd "${D}" && pullLog=$(git pull origin master) > /dev/null 2>&1, pullStatus=$?, |
| System                                    | #/system/downloadModule $moduleName,                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 1. PIGET : Update all modules             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 1. COMMENT - $lastcomment                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2. Warning message from git pull          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 3. Module $moduleName not saved or broken |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| /do/core/pi/wifi   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info               | [alpha] [undocumented]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Arguments          | 1:text, 2:color,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Variables          | text=$1, color=$2, interface=$(iwconfig 2>/dev/null | grep -o "^\w*"), essid=$(iwlist $interface scan|grep "ESSID:"|tr -d '"'|sed -e 's/ESSID://'), essid=$(iwlist $interface scan|grep "ESSID:"|tr -d '"'|sed -e 's/ESSID://'), menu_options[ $i ]=$access, essid_selected=$(whiptail --backtitle "Wifi Configuration" --title "$interface" --menu "Choose your Wireless Network" 0 0 0 "${menu_options[@]}" 3>&1 1>&2 2>&3 ), password=$(whiptail --backtitle "Wifi Configuration" --inputbox "$essid_selected" 0 0 --title "Enter Password" 3>&1 1>&2 2>&3), isConnected=$(iwconfig $interface 2>/dev/null |grep "Not-Associated"|wc -l), |

| /do/core/pi/wifiSettings   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

