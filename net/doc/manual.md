| /do/core/net/internetOff   |                                 |
|:---------------------------|:--------------------------------|
| Description                | Remove default route to gateway |
| Example                    | /net/internetOff                |
| Info                       | [alpha] [undocumented]          |

| /do/core/net/internetOn   |                                   |
|:--------------------------|:----------------------------------|
| Description               | Recreate default route to gateway |
| Example                   | /net/internetOn 192.168.1.1       |
| Info                      | [alpha] [undocumented]            |

| /do/core/net/resetHost   |                                             |
|:-------------------------|:--------------------------------------------|
| Description              | Change name in /etc/hosts and /etc/hostname |
| Example                  | /do/core/net/resetHost raspberrypi          |
| Info                     | [beta] [network] [avahi] [bonjour]          |

| /do/core/net/resetNetwork   |                        |
|:----------------------------|:-----------------------|
| Info                        | [alpha] [undocumented] |

| /do/core/net/socketRead   |                                  |
|:--------------------------|:---------------------------------|
| Description               | Send text to a socket            |
| Example                   | /net/socketSend hello world 9060 |
| Info                      | [alpha] [undocumented]           |
| Arguments                 | 1:port,                          |

| /do/core/net/socketSend   |                                  |
|:--------------------------|:---------------------------------|
| Description               | Send text to a socket            |
| Example                   | /net/socketSend hello world 9060 |
| Info                      | [alpha] [undocumented]           |
| Arguments                 | 1:port, 2:message,               |

