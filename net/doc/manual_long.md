| /do/core/net/internetOff   |                                 |
|:---------------------------|:--------------------------------|
| Info                       | [alpha] [undocumented]          |
| Description                | Remove default route to gateway |
| Usage                      | /net/internetOff                |
| Example                    | /net/internetOff                |
| 1. -> INTERNET [DOWN]      |                                 |

| /do/core/net/internetOn          |                                   |
|:---------------------------------|:----------------------------------|
| Info                             | [alpha] [undocumented]            |
| Description                      | Recreate default route to gateway |
| Usage                            | /net/internetOn GATEWAY_IP        |
| Example                          | /net/internetOn 192.168.1.1       |
| 1. -> INTERNET ROUTER --> [ $1 ] |                                   |

| /do/core/net/readme.md   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/net/resetHost   |                                                                       |
|:-------------------------|:----------------------------------------------------------------------|
| Info                     | [beta] [network] [avahi] [bonjour]                                    |
| Description              | Change name in /etc/hosts and /etc/hostname                           |
| Usage                    | /do/core/net/resetHost [newname] (default:/user/settings/pi/name.txt) |
| Example                  | /do/core/net/resetHost raspberrypi                                    |
| Variables                | NEW_HOSTNAME=$NewString,                                              |
| System                   | /system/restart avahi-daemon,                                         |

| /do/core/net/resetNetwork   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/net/socketRead   |                                  |
|:--------------------------|:---------------------------------|
| Info                      | [alpha] [undocumented]           |
| Description               | Send text to a socket            |
| Usage                     | /net/socketSend message port     |
| Example                   | /net/socketSend hello world 9060 |
| Arguments                 | 1:port,                          |
| Variables                 | port=$1,                         |

| /do/core/net/socketSend   |                                  |
|:--------------------------|:---------------------------------|
| Info                      | [alpha] [undocumented]           |
| Description               | Send text to a socket            |
| Usage                     | /net/socketSend message port     |
| Example                   | /net/socketSend hello world 9060 |
| Arguments                 | 1:port, 2:message,               |
| Variables                 | port=$1, message=$2,             |

