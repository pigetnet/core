| /pi/doc.md   |                        |
|:-------------|:-----------------------|
| Info         | [alpha] [undocumented] |

| /pi/install   |                                                         |
|:--------------|:--------------------------------------------------------|
| Description   | Download a module at github.com/pigetnet and install it |
| Example       | /pi/install samba                                       |
| Info          | [beta]                                                  |

| /pi/installWiringPi   |                        |
|:----------------------|:-----------------------|
| Info                  | [alpha] [undocumented] |

| /pi/installWiringPiPython   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /pi/ledBlink   |                          |
|:---------------|:-------------------------|
| Description    | Make the green led blink |
| Info           | [release]                |

| /pi/ledOff   |                        |
|:-------------|:-----------------------|
| Description  | Turn off the green led |
| Info         | [release]              |

| /pi/ledOn   |                       |
|:------------|:----------------------|
| Description | Turn on the green led |
| Info        | [release]             |

| /pi/ledReset   |                                        |
|:---------------|:---------------------------------------|
| Description    | Reset the green led to SDcard activity |
| Info           | [release]                              |

| /pi/linker   |                                                  |
|:-------------|:-------------------------------------------------|
| Description  | create a link to a command inside /usr/local/bin |
| Example      | /pi/linker /pi/ledOn turn_on_led                 |
| Info         | [beta] [2 args]                                  |
| Arguments    | 1:scriptToLink, 2:link,                          |

| /pi/make    |                                                         |
|:------------|:--------------------------------------------------------|
| Description | Launch install script at /boot/piget/scripts/install.sh |
| Example     | /pi/make                                                |
| Info        | [alpha] [undocumented]                                  |

| /pi/name    |                                            |
|:------------|:-------------------------------------------|
| Description | Rename your Raspberry Pi using avahi/samba |
| Example     | /pi/name raspberrypi                       |
| Info        | [alpha] [undocumented]                     |
| Arguments   | 1:NEW_HOSTNAME,                            |

| /pi/prepare   |                        |
|:--------------|:-----------------------|
| Info          | [alpha] [undocumented] |

| /pi/removeDefaultUser   |                                      |
|:------------------------|:-------------------------------------|
| Description             | Remove pi user (if it is not logged) |
| Example                 | /pi/removeDefaultUser                |
| Info                    | [alpha] [undocumented]               |

| /pi/removeDesktop   |                                                                           |
|:--------------------|:--------------------------------------------------------------------------|
| Description         | Remove all desktop applications (WARNING THIS TAKES MORE THAN 30 MINUTES) |
| Example             | /pi/removeDesktop                                                         |
| Info                | [alpha] [undocumented]                                                    |

| /pi/removeRaspiNotice   |                                                 |
|:------------------------|:------------------------------------------------|
| Description             | remove notice to use raspi-config on connection |
| Info                    | [release]                                       |

| /pi/resizeSD   |                                                               |
|:---------------|:--------------------------------------------------------------|
| Description    | Expand SDcard on next boot using raspi-config unattended mode |
| Info           | [release] [reboot]                                            |

| /pi/timeZone   |                         |
|:---------------|:------------------------|
| Description    | Modify timezone         |
| Info           | [release] [interactive] |

| /pi/update   |                          |
|:-------------|:-------------------------|
| Description  | Update apt-get and Piget |
| Info         | [beta] [long]            |

| /pi/updateAllGitRepo   |                                           |
|:-----------------------|:------------------------------------------|
| Description            | Update all git repositories on the system |
| Info                   | [alpha] [caution]                         |

| /pi/updateGitRepo   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |
| Arguments           | 1:d,                   |

| /pi/updatePiget   |                                                   |
|:------------------|:--------------------------------------------------|
| Description       | Update all piget modules (this can erase changes) |
| Info              | [beta] [caution]                                  |

