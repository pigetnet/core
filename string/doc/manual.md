| /do/core/string/add   |                                                                  |
|:----------------------|:-----------------------------------------------------------------|
| Description           | Add a parameters in a configuration file                         |
| Example               | /do/core/string/add /string/add /boot/config.txt dtparam=i2c1=on |
| Info                  | [alpha] [2 args] [danger]                                        |
| Arguments             | 1:file, 2:string_to_add,                                         |

| /do/core/string/addAfterLine   |                                                                  |
|:-------------------------------|:-----------------------------------------------------------------|
| Example                        | /string/addAfterLine /etc/hosts raspberrypi 192.168.0.254 router |
| Info                           | [alpha] [undocumented]                                           |
| Arguments                      | 1:filename, 2:addAfterString, 3:stringToReplace,                 |

| /do/core/string/addAfterLineIfNotExists   |                                                                            |
|:------------------------------------------|:---------------------------------------------------------------------------|
| Example                                   | /string/addAfterLineIfNotExists /etc/hosts 127.0.0.1 127.0.0.1 raspberrypi |
| Info                                      | [alpha] [undocumented]                                                     |

| /do/core/string/addLine   |                                                                               |
|:--------------------------|:------------------------------------------------------------------------------|
| Example                   | /string/addLine /etc/apt/sources.list deb http://apt.pilight.org/ stable main |
| Info                      | [alpha] [undocumented]                                                        |

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
| Description              | get All fields of a configuration file                 |
| Example                  | /do/core/string/getAll /string/getAll /boot/config.txt |
| Info                     | [alpha] [1 args]                                       |
| Arguments                | 1:file,                                                |

| /do/core/string/getConfigFormat   |                        |
|:----------------------------------|:-----------------------|
| Info                              | [alpha] [undocumented] |

| /do/core/string/getJson   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/string/getLine   |                                       |
|:--------------------------|:--------------------------------------|
| Example                   | /string/getLine /etc/rc.local # Print |
| Info                      | [alpha] [undocumented]                |
| Arguments                 | 1:filename, 2:stringToSearch,         |

| /do/core/string/removeLine   |                                     |
|:-----------------------------|:------------------------------------|
| Example                      | removeLine /etc/samba/ netbios name |
| Info                         | [alpha] [undocumented]              |

| /do/core/string/replaceLine   |                                                                                                               |
|:------------------------------|:--------------------------------------------------------------------------------------------------------------|
| Description                   | Change name in /etc/hosts and /etc/hostname                                                                   |
| Example                       | /do/core/string/replaceLine \/etc/hosts\ \127.0.0.1\ \127.0.0.1 raspberrypi\ \ff02::2         ip6-allrouters\ |
| Info                          | [beta] [string] [avahi] [bonjour]                                                                             |

| /do/core/string/replaceLineIfExists   |                                                        |
|:--------------------------------------|:-------------------------------------------------------|
| Example                               | replaceLine /etc/hosts 127.0.0.1 127.0.0.1 raspberrypi |
| Info                                  | [alpha] [undocumented]                                 |

| /do/core/string/searchString   |                        |
|:-------------------------------|:-----------------------|
| Info                           | [alpha] [undocumented] |
| Arguments                      | 1:file, 2:string,      |

| /do/core/string/stripAccents   |                        |
|:-------------------------------|:-----------------------|
| Info                           | [alpha] [undocumented] |

| /do/core/string/ToAlphaNumeric   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/string/ToNetbios   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/string/Trim   |                        |
|:-----------------------|:-----------------------|
| Info                   | [alpha] [undocumented] |

| /do/core/string/upperToLower   |                        |
|:-------------------------------|:-----------------------|
| Info                           | [alpha] [undocumented] |

