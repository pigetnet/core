| /do/core/net/internetOff   |                                                           |
|:---------------------------|:----------------------------------------------------------|
| Info                       | [release] [danger] [network] [gateway]                    |
| Description                | Remove default gateway to simulate internet disconnection |
| Usage                      | /do/core/net/internetOff                                  |
| 1. -> INTERNET [DOWN]      |                                                           |

| /do/core/net/internetOn          |                                          |
|:---------------------------------|:-----------------------------------------|
| Info                             | [ip route] [release] [network] [gateway] |
| Description                      | Recreate default route to gateway        |
| Usage                            | /net/internetOn GATEWAY_IP               |
| Example                          | /net/internetOn 192.168.1.1              |
| 1. -> INTERNET ROUTER --> [ $1 ] |                                          |

| /do/core/net/resetHost   |                                             |
|:-------------------------|:--------------------------------------------|
| Info                     | [beta] [network] [avahi] [bonjour]          |
| Description              | Change name in /etc/hosts and /etc/hostname |
| Usage                    | /do/core/net/resetHost [newname]            |
| Example                  | /do/core/net/resetHost raspberrypi          |
| Variables                | NEW_HOSTNAME=$NewString,                    |
| System                   | /system/restart avahi-daemon,               |

| /do/core/net/resetNetwork   |                                                            |
|:----------------------------|:-----------------------------------------------------------|
| Info                        | [beta] [/etc/networkg/interfaces] [network]                |
| Description                 | Replace /etc/network/interfaces with default configuration |
| Usage                       | /do/core/net/resetNetwork                                  |

| /do/core/net/socketRead   |                              |
|:--------------------------|:-----------------------------|
| Info                      | [exec] [socket] [local]      |
| Description               | Read a socket                |
| Usage                     | /do/core/net/socketRead port |
| Example                   | /do/core/net/socketRead 22   |
| Arguments                 | 1:port,                      |
| Variables                 | port=$1,                     |

| /do/core/net/socketSend   |                                      |
|:--------------------------|:-------------------------------------|
| Info                      | [echo] [/dev/tcp] [local]            |
| Description               | Send a message to a socket           |
| Usage                     | /do/core/net/socketSend message port |
| Example                   | /net/socketSend 22 hello             |
| Arguments                 | 1:port, 2:message,                   |
| Variables                 | port=$1, message=$2,                 |

