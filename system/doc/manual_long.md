| /do/core/system/addAptRepository                   |                                                                                                                                                                                                                           |
|:---------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                               | [alpha] [undocumented]                                                                                                                                                                                                    |
| Description                                        | add an APT Repository                                                                                                                                                                                                     |
| Usage                                              | /system/addAptRepository repoUrl keyUrl                                                                                                                                                                                   |
| Example                                            | /system/addAptRepository deb http://apt.pilight.org/ stable main http://apt.pilight.org/pilight.key                                                                                                                       |
| Arguments                                          | 1:repo, 2:key,                                                                                                                                                                                                            |
| Variables                                          | repo=$1, key=$2,                                                                                                                                                                                                          |
| System                                             | /system/autoBackup /etc/apt/sources.list, /show/usage "/system/addAptRepository repoUrl keyUrl", /show/example '/system/addAptRepository "deb http://apt.pilight.org/ stable main" "http://apt.pilight.org/pilight.key"', |
| 1. Add custom repositories $repo into sources.list |                                                                                                                                                                                                                           |
| 2. Add key $key                                    |                                                                                                                                                                                                                           |

| /do/core/system/addPath          |                                         |
|:---------------------------------|:----------------------------------------|
| Info                             | [alpha] [undocumented]                  |
| Description                      | Add a path into /root/.bashrc           |
| Usage                            | /string/addPath newPath                 |
| Example                          | /string/addPath /opt/usercode           |
| Arguments                        | 1:newpath,                              |
| Variables                        | newpath=$1, export PATH=$PATH:$newpath, |
| 1. Add $newpath to /root/.bashrc |                                         |

| /do/core/system/aptLog                                    |                        |
|:----------------------------------------------------------|:-----------------------|
| Info                                                      | [alpha] [undocumented] |
| 1. APT-GET LOG                                            |                        |
| 1. Display /var/log/pat/term.log (PRESS [CTRL-C] to quit) |                        |

| /do/core/system/aptRemoveLock   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |
| 1. APT: Fix lock error          |                        |

| /do/core/system/autoBackup   |                                                                                           |
|:-----------------------------|:------------------------------------------------------------------------------------------|
| Info                         | [alpha] [undocumented]                                                                    |
| Description                  | Backup a file to /boot/piget/backups                                                      |
| Usage                        | autoBackup fileToBackup                                                                   |
| Example                      | autoBackup /etc/hosts                                                                     |
| Arguments                    | 1:filename,                                                                               |
| Variables                    | filename=$1, basename=$(basename $filename), timestamp=$(date +%Y%m%d)'_'$(date +%H%M%S), |
| System                       | /system/createDir /boot/piget/backups,                                                    |

| /do/core/system/bcmToWpi   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/changeColor                   |                                                       |
|:----------------------------------------------|:------------------------------------------------------|
| Info                                          | [alpha] [undocumented]                                |
| Arguments                                     | 1:colorName,                                          |
| Variables                                     | currentColor=$(/system/getColorNumber), colorName=$1, |
| System                                        | currentColor=$(/system/getColorNumber),               |
| 1. [TERMINAL COLOR] $colorName ($colorNumber) |                                                       |

| /do/core/system/checkPermissions                        |                        |
|:--------------------------------------------------------|:-----------------------|
| Info                                                    | [alpha] [undocumented] |
| 1. Check permissions for config files in /user/settings |                        |

| /do/core/system/cleanForBackup   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/system/clearLog   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/convertScript   |                           |
|:--------------------------------|:--------------------------|
| Info                            | [alpha] [undocumented]    |
| Softwares                       | dos2unix,                 |
| System                          | /system/install dos2unix, |

| /do/core/system/createDir   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/system/createScript     |                                                  |
|:---------------------------------|:-------------------------------------------------|
| Info                             | [alpha] [dev]                                    |
| Description                      | Generate a script to be edited on Windows        |
| Usage                            | /do/core/system/createScript script              |
| Example                          | /do/core/system/createScript /do/example/install |
| Arguments                        | 1:script,                                        |
| Variables                        | script=$1,                                       |
| Modules                          | /show/example "$0 /do/example/install",          |
| 1. [CREATE SCRIPT] $script       |                                                  |
| 1. Type: nano $script to edit it |                                                  |
| 2. Script already existed        |                                                  |

| /do/core/system/downloadFile   |                                                                                                                                                                                              |
|:-------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                           | [alpha] [undocumented]                                                                                                                                                                       |
| Usage                          | /system/downloadFile url destination                                                                                                                                                         |
| Example                        | /system/downloadFile http://www.foobar.com/file.zip /tmp/foobar.zip                                                                                                                          |
| Arguments                      | 1:url, 2:destination,                                                                                                                                                                        |
| Variables                      | url=$1, destination=$2, wgeterror=$?,                                                                                                                                                        |
| System                         | /system/wgetErrorManager $wgeterror /tmp/wget.temp, /show/usage "/system/downloadFile url destination", /show/example "/system/downloadFile http://www.foobar.com/file.zip /tmp/foobar.zip", |

| /do/core/system/downloadGithubFile                        |                                                                           |
|:----------------------------------------------------------|:--------------------------------------------------------------------------|
| Info                                                      | [beta] [service] [systemctl]                                              |
| Description                                               | Download a file on github                                                 |
| Usage                                                     | /do/core/system/downloadGithubFile repo source destination                |
| Example                                                   | /do/core/system/downloadGithubFile pigetnet/smb piget /etc/samba/smb.conf |
| Arguments                                                 | 1:reponame, 2:source, 3:destination,                                      |
| Variables                                                 | reponame=$1, source=$2, destination=$3, wgeterror=$?,                     |
| System                                                    | /system/wgetErrorManager $wgeterror /tmp/wget.temp,                       |
| 1. #  Github: pigetnet/$reponame/$source ==> $destination |                                                                           |
| 2. Here is a list of available files                      |                                                                           |

| /do/core/system/downloadModule                   |                                                                                                            |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| Info                                             | [dev] [beta]                                                                                               |
| Description                                      | Download a module on github.com                                                                            |
| Usage                                            | /do/core/system/downloadModule module or user/module                                                       |
| Example                                          | /do/core/system/downloadModule samba or maditnerd/example                                                  |
| Arguments                                        | 1:reponame,                                                                                                |
| Variables                                        | reponame=$1, username=${reponame%/*}, reponame=${reponame#*/}, username=$(cat /user/settings/pi/repo.txt), |
| Modules                                          | /show/description "[GITHUB] $username/$reponame => /do/$reponame",                                         |
| System                                           | /system/gitcloner $username/$reponame /opt/piget/$reponame,                                                |
| 1. [GITHUB] $username/$reponame => /do/$reponame |                                                                                                            |
| 1. No repo founded                               |                                                                                                            |

| /do/core/system/file2web   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/firmwareUpdate   |                             |
|:---------------------------------|:----------------------------|
| Info                             | [alpha] [undocumented]      |
| Softwares                        | /rpi-update,                |
| System                           | /system/install/rpi-update, |
| 1. rpi-update                    |                             |

| /do/core/system/getColor   |                                                                                   |
|:---------------------------|:----------------------------------------------------------------------------------|
| Info                       | [alpha] [undocumented]                                                            |
| Variables                  | colorNumber=$(cat /root/.bashrc |grep PS1|cut -f1 -d"m"|awk -F[ '{ print $NF }'), |

| /do/core/system/getColorNumber   |                                                                                   |
|:---------------------------------|:----------------------------------------------------------------------------------|
| Info                             | [alpha] [undocumented]                                                            |
| Variables                        | colorNumber=$(cat /root/.bashrc |grep PS1|cut -f1 -d"m"|awk -F[ '{ print $NF }'), |

| /do/core/system/getRepo   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/system/gitcloner   |                                                                                                |
|:----------------------------|:-----------------------------------------------------------------------------------------------|
| Info                        | [alpha] [undocumented]                                                                         |
| Arguments                   | 1:repo, 2:directory,                                                                           |
| Variables                   | repo=$1, directory=$2, giterror=$?, # git --work-tree=$2 --git-dir=$2/.git pull origin master, |
| 1. #  ---> ALREADY CLONED   |                                                                                                |
| 2. #	 Clone $1 inside $2    |                                                                                                |

| /do/core/system/h3ToBcm   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/system/install           |                                                                          |
|:----------------------------------|:-------------------------------------------------------------------------|
| Info                              | [alpha] [undocumented]                                                   |
| Softwares                         | debconf-apt-progress --  -q -y $PACKAGE, /show/colecho ->  diagnosis , , |
| Arguments                         | 1:PACKAGE,                                                               |
| Variables                         | PACKAGE=$1,                                                              |
| 2. -> Package state:$check        |                                                                          |
| 4. -> apt-get install diagnosis   |                                                                          |
| 6. UNABLE TO CONTINUE             |                                                                          |
| 7. #  Install: $PACKAGE [SKIPPED] |                                                                          |

| /do/core/system/installWiringPi   |                                                |
|:----------------------------------|:-----------------------------------------------|
| Info                              | [beta] [orangepi]                              |
| Description                       | Download and install WiringPi (to manage GPIO) |
| Usage                             | /do/core/system/installWiringPi                |
| Softwares                         | git-core,                                      |
| Variables                         | hardware=$(/pi/getBoard),                      |
| System                            | /system/install git-core,                      |
| 1. [WiringPi] Installation        |                                                |
| 3. installed                      |                                                |
| 4. [WiringPi] Check Update        |                                                |

| /do/core/system/logInit   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| Arguments                 | 1:scriptName,          |
| Variables                 | scriptName=$1,         |

| /do/core/system/makedir   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| Arguments                 | 1:dir,                 |
| Variables                 | dir=$1,                |

| /do/core/system/modifyBashStartup   |                                                     |
|:------------------------------------|:----------------------------------------------------|
| Info                                | [alpha] [undocumented]                              |
| System                              | /system/downloadGithubFile bashrc $1 /root/.bashrc, |

| /do/core/system/password     |                        |
|:-----------------------------|:-----------------------|
| Info                         | [alpha] [undocumented] |
| Arguments                    | 1:user, 2:password,    |
| Variables                    | user=$1, password=$2,  |
| 1. [SSH PASSWORD] User $user |                        |
| 1. Failed                    |                        |

| /do/core/system/remove   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |
| 1. Remove : $1 [SKIPPED] |                        |

| /do/core/system/removeAccount   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |
| 1. Removing user $1             |                        |

| /do/core/system/removeModule                  |                                             |
|:----------------------------------------------|:--------------------------------------------|
| Info                                          | [alpha] [undocumented]                      |
| Usage                                         | removeModule reponame                       |
| Example                                       | removeModule samba                          |
| Arguments                                     | 1:reponame,                                 |
| Variables                                     | reponame=$1,                                |
| Modules                                       | /show/description "Removing /do/$reponame", |
| System                                        | /system/removePath /opt/piget/$reponame,    |
| 1. Removing /do/$reponame                     |                                             |
| 1. You were really close to delete everything |                                             |
| 2. You were really close to delete piget      |                                             |
| 3. No module specified                        |                                             |
| 4. Directory does not exists                  |                                             |

| /do/core/system/removePath      |                                                                        |
|:--------------------------------|:-----------------------------------------------------------------------|
| Info                            | [alpha] [undocumented]                                                 |
| Usage                           | addPath newPath                                                        |
| Example                         | addPath /opt/usercode                                                  |
| Arguments                       | 1:oldpath,                                                             |
| Variables                       | oldpath=$1, /string/removeLine "/root/.bashrc" "PATH=$oldpath:\$PATH", |
| 1. Remove $oldpath from .bashrc |                                                                        |

| /do/core/system/removePiget                                |                        |
|:-----------------------------------------------------------|:-----------------------|
| Info                                                       | [alpha] [undocumented] |
| 1. This will erase Piget and all users data! Backup first! |                        |
| 1. Remove symbolic link                                    |                        |
| 2. Remove Users Files                                      |                        |
| 3. Remove Piget core and modules                           |                        |

| /do/core/system/restart   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| 1. #  Restarting $1       |                        |

| /do/core/system/scriptOnNextReboot   |                        |
|:-------------------------------------|:-----------------------|
| Info                                 | [alpha] [undocumented] |
| Arguments                            | 1:script,              |
| Variables                            | script=$1,             |
| 1. Execute $script at next boot      |                        |

| /do/core/system/searchPackage   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/system/syslog   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/system/wgetErrorManager   |                            |
|:-----------------------------------|:---------------------------|
| Info                               | [alpha] [undocumented]     |
| Arguments                          | 2:filename, 1:wgeterror,   |
| Variables                          | filename=$2, wgeterror=$1, |
| 1. Wrong wget commands             |                            |
| 2. File not founded                |                            |
| 3. Wrong filename                  |                            |

