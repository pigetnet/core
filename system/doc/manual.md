| /do/core/system/addAptRepository   |                                                                                                     |
|:-----------------------------------|:----------------------------------------------------------------------------------------------------|
| Description                        | add an APT Repository                                                                               |
| Example                            | /system/addAptRepository deb http://apt.pilight.org/ stable main http://apt.pilight.org/pilight.key |
| Info                               | [alpha] [undocumented]                                                                              |
| Arguments                          | 1:repo, 2:key,                                                                                      |

| /do/core/system/addPath   |                               |
|:--------------------------|:------------------------------|
| Description               | Add a path into /root/.bashrc |
| Example                   | /string/addPath /opt/usercode |
| Info                      | [alpha] [undocumented]        |
| Arguments                 | 1:newpath,                    |

| /do/core/system/aptLog   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/system/aptRemoveLock   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/system/autoBackup   |                                      |
|:-----------------------------|:-------------------------------------|
| Description                  | Backup a file to /boot/piget/backups |
| Example                      | autoBackup /etc/hosts                |
| Info                         | [alpha] [undocumented]               |
| Arguments                    | 1:filename,                          |

| /do/core/system/bcmToWpi   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/changeColor   |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |
| Arguments                     | 1:colorName,           |

| /do/core/system/checkPermissions   |                        |
|:-----------------------------------|:-----------------------|
| Info                               | [alpha] [undocumented] |

| /do/core/system/cleanForBackup   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/system/clearLog   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/convertScript   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/system/createDir   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/system/createScript   |                                                  |
|:-------------------------------|:-------------------------------------------------|
| Description                    | Generate a script to be edited on Windows        |
| Example                        | /do/core/system/createScript /do/example/install |
| Info                           | [alpha] [dev]                                    |
| Arguments                      | 1:script,                                        |

| /do/core/system/downloadFile   |                                                                     |
|:-------------------------------|:--------------------------------------------------------------------|
| Example                        | /system/downloadFile http://www.foobar.com/file.zip /tmp/foobar.zip |
| Info                           | [alpha] [undocumented]                                              |
| Arguments                      | 1:url, 2:destination,                                               |

| /do/core/system/downloadGithubFile   |                                                                           |
|:-------------------------------------|:--------------------------------------------------------------------------|
| Description                          | Download a file on github                                                 |
| Example                              | /do/core/system/downloadGithubFile pigetnet/smb piget /etc/samba/smb.conf |
| Info                                 | [beta] [service] [systemctl]                                              |
| Arguments                            | 1:reponame, 2:source, 3:destination,                                      |

| /do/core/system/downloadModule   |                                                           |
|:---------------------------------|:----------------------------------------------------------|
| Description                      | Download a module on github.com                           |
| Example                          | /do/core/system/downloadModule samba or maditnerd/example |
| Info                             | [dev] [beta]                                              |
| Arguments                        | 1:reponame,                                               |

| /do/core/system/file2web   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/firmwareUpdate   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/system/getColor   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |

| /do/core/system/getColorNumber   |                        |
|:---------------------------------|:-----------------------|
| Info                             | [alpha] [undocumented] |

| /do/core/system/getRepo   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/system/gitcloner   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |
| Arguments                   | 1:repo, 2:directory,   |

| /do/core/system/h3ToBcm   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/system/install   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| Arguments                 | 1:PACKAGE,             |

| /do/core/system/installWiringPi   |                                                |
|:----------------------------------|:-----------------------------------------------|
| Description                       | Download and install WiringPi (to manage GPIO) |
| Info                              | [beta] [orangepi]                              |

| /do/core/system/logInit   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| Arguments                 | 1:scriptName,          |

| /do/core/system/makedir   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |
| Arguments                 | 1:dir,                 |

| /do/core/system/modifyBashStartup   |                        |
|:------------------------------------|:-----------------------|
| Info                                | [alpha] [undocumented] |

| /do/core/system/password   |                        |
|:---------------------------|:-----------------------|
| Info                       | [alpha] [undocumented] |
| Arguments                  | 1:user, 2:password,    |

| /do/core/system/remove   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/system/removeAccount   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/system/removeModule   |                        |
|:-------------------------------|:-----------------------|
| Example                        | removeModule samba     |
| Info                           | [alpha] [undocumented] |
| Arguments                      | 1:reponame,            |

| /do/core/system/removePath   |                        |
|:-----------------------------|:-----------------------|
| Example                      | addPath /opt/usercode  |
| Info                         | [alpha] [undocumented] |
| Arguments                    | 1:oldpath,             |

| /do/core/system/removePiget   |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |

| /do/core/system/restart   |                        |
|:--------------------------|:-----------------------|
| Info                      | [alpha] [undocumented] |

| /do/core/system/scriptOnNextReboot   |                        |
|:-------------------------------------|:-----------------------|
| Info                                 | [alpha] [undocumented] |
| Arguments                            | 1:script,              |

| /do/core/system/searchPackage   |                        |
|:--------------------------------|:-----------------------|
| Info                            | [alpha] [undocumented] |

| /do/core/system/syslog   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/system/wgetErrorManager   |                          |
|:-----------------------------------|:-------------------------|
| Info                               | [alpha] [undocumented]   |
| Arguments                          | 2:filename, 1:wgeterror, |

