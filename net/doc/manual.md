| /do/core/net/internetOff   |                                                           |
|:---------------------------|:----------------------------------------------------------|
| Description                | Remove default gateway to simulate internet disconnection |
| Info                       | [release] [danger] [network] [gateway]                    |

| /do/core/net/internetOn   |                                          |
|:--------------------------|:-----------------------------------------|
| Description               | Recreate default route to gateway        |
| Example                   | /net/internetOn 192.168.1.1              |
| Info                      | [ip route] [release] [network] [gateway] |

| /do/core/net/readme.md   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/net/resetHost   |                                             |
|:-------------------------|:--------------------------------------------|
| Description              | Change name in /etc/hosts and /etc/hostname |
| Example                  | /do/core/net/resetHost raspberrypi          |
| Info                     | [beta] [network] [avahi] [bonjour]          |

| /do/core/net/resetNetwork   |                                                            |
|:----------------------------|:-----------------------------------------------------------|
| Description                 | Replace /etc/network/interfaces with default configuration |
| Info                        | [beta] [/etc/networkg/interfaces] [network]                |

| /do/core/net/socketRead   |                            |
|:--------------------------|:---------------------------|
| Description               | Read a socket              |
| Example                   | /do/core/net/socketRead 22 |
| Info                      | [exec] [socket] [local]    |
| Arguments                 | 1:port,                    |

| /do/core/net/socketSend   |                            |
|:--------------------------|:---------------------------|
| Description               | Send a message to a socket |
| Example                   | /net/socketSend 22 hello   |
| Info                      | [echo] [/dev/tcp] [local]  |
| Arguments                 | 1:port, 2:message,         |

