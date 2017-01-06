| /do/core/pi/delayedCommand   |                        |
|:-----------------------------|:-----------------------|
| Info                         | [alpha] [undocumented] |

| /do/core/pi/getBoard   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/pi/install   |                                                         |
|:----------------------|:--------------------------------------------------------|
| Description           | Download a module at github.com/pigetnet and install it |
| Example               | /do/core/pi/install samba                               |
| Info                  | [beta]                                                  |
| Arguments             | 1:moduleName,                                           |

| /do/core/pi/installNodeJS   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/pi/ledBlink   |                          |
|:-----------------------|:-------------------------|
| Description            | Make the green led blink |
| Info                   | [release]                |

| /do/core/pi/ledOff   |                        |
|:---------------------|:-----------------------|
| Description          | Turn off the green led |
| Info                 | [release] [orangepi]   |

| /do/core/pi/ledOn   |                       |
|:--------------------|:----------------------|
| Description         | Turn on the green led |
| Info                | [release] [orangepi]  |

| /do/core/pi/ledReset   |                                        |
|:-----------------------|:---------------------------------------|
| Description            | Reset the green led to SDcard activity |
| Info                   | [release] [orangepi]                   |

| /do/core/pi/linker   |                                                  |
|:---------------------|:-------------------------------------------------|
| Description          | create a link to a command inside /usr/local/bin |
| Example              | /do/core/pi/linker /pi/ledOn turn_on_led         |
| Info                 | [beta] [2 args]                                  |
| Arguments            | 1:scriptToLink, 2:link,                          |

| /do/core/pi/list   |                        |
|:-------------------|:-----------------------|
| Info               | [alpha] [undocumented] |

| /do/core/pi/logBook   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/pi/logTerminal   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/pi/modules   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/pi/name   |                                            |
|:-------------------|:-------------------------------------------|
| Description        | Rename your Raspberry Pi using avahi/samba |
| Example            | /do/core/pi/name raspberrypi               |
| Info               | [beta]                                     |
| Arguments          | 1:NEW_HOSTNAME,                            |

| /do/core/pi/pinOut   |                        |
|:---------------------|:-----------------------|
| Info                 | [alpha] [undocumented] |

| /do/core/pi/prepare   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /do/core/pi/readme.md   |                        |
|:------------------------|:-----------------------|
| Info                    | [alpha] [undocumented] |

| /do/core/pi/removeDefaultUser   |                                      |
|:--------------------------------|:-------------------------------------|
| Description                     | Remove pi user (if it is not logged) |
| Example                         | /pi/removeDefaultUser                |
| Info                            | [alpha] [undocumented]               |

| /do/core/pi/removeDesktop   |                                                                           |
|:----------------------------|:--------------------------------------------------------------------------|
| Description                 | Remove all desktop applications (WARNING THIS TAKES MORE THAN 30 MINUTES) |
| Example                     | /pi/removeDesktop                                                         |
| Info                        | [alpha] [undocumented]                                                    |

| /do/core/pi/removeRaspiNotice   |                                                 |
|:--------------------------------|:------------------------------------------------|
| Description                     | remove notice to use raspi-config on connection |
| Info                            | [release]                                       |

| /do/core/pi/resizeSD   |                                                               |
|:-----------------------|:--------------------------------------------------------------|
| Description            | Expand SDcard on next boot using raspi-config unattended mode |
| Info                   | [release] [reboot] [danger]                                   |

| /do/core/pi/setup   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |

| /do/core/pi/start   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |

| /do/core/pi/syncFile   |                                                      |
|:-----------------------|:-----------------------------------------------------|
| Description            | Save configuration file into /user/settings/pi/files |
| Info                   | [alpha] [WIP] [danger] [dev]                         |
| Arguments              | 1:file,                                              |

| /do/core/pi/syncFromUser   |                                 |
|:---------------------------|:--------------------------------|
| Description                | Sync /user/settings/pi/* into / |
| Info                       | [alpha] [WIP] [danger] [dev]    |

| /do/core/pi/syncToUser   |                                         |
|:-------------------------|:----------------------------------------|
| Description              | Sync backed-up configuration into /user |
| Info                     | [alpha] [WIP] [danger] [dev]            |

| /do/core/pi/timeZone   |                         |
|:-----------------------|:------------------------|
| Description            | Modify timezone         |
| Info                   | [release] [interactive] |

| /do/core/pi/update   |                          |
|:---------------------|:-------------------------|
| Description          | Update apt-get and Piget |
| Info                 | [beta] [long]            |

| /do/core/pi/updateAllGitRepo   |                                           |
|:-------------------------------|:------------------------------------------|
| Description                    | Update all git repositories on the system |
| Info                           | [alpha] [caution]                         |

| /do/core/pi/updateGitRepo   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |
| Arguments                   | 1:d,                   |

| /do/core/pi/updatePiget   |                                                   |
|:--------------------------|:--------------------------------------------------|
| Description               | Update all piget modules (this can erase changes) |
| Info                      | [beta] [caution]                                  |

| /do/core/pi/wifi   |                        |
|:-------------------|:-----------------------|
| Info               | [alpha] [undocumented] |
| Arguments          | 1:text, 2:color,       |

| /do/core/pi/wifiSettings   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

