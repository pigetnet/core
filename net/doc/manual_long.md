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

| /do/core/net/isWifi   |                                                                              |
|:----------------------|:-----------------------------------------------------------------------------|
| Info                  | [alpha] [undocumented]                                                       |
| Variables             | isConnected=$(iwconfig $interface 2>/dev/null |grep "Not-Associated"|wc -l), |

| /do/core/net/resetHost                   |                                                                        |
|:-----------------------------------------|:-----------------------------------------------------------------------|
| Info                                     | [beta] [network] [avahi] [bonjour]                                     |
| Description                              | Change name in /etc/hosts and /etc/hostname                            |
| Usage                                    | /do/core/net/resetHost [newname] (default:/boot/piget/config/name.txt) |
| Example                                  | /do/core/net/resetHost raspberrypi                                     |
| Variables                                | NEW_HOSTNAME=$NewString,                                               |
| System                                   | /system/autoBackup /etc/hostname, /system/restart avahi-daemon,        |
| 1. #  Bonjour Name : $NEW_HOSTNAME.local |                                                                        |

| /do/core/net/resetInterfaces                                             |                                             |
|:-------------------------------------------------------------------------|:--------------------------------------------|
| Info                                                                     | [alpha] [undocumented]                      |
| System                                                                   | /system/autoBackup /etc/network/interfaces, |
| 1. Reset interfaces to default                                           |                                             |
| 1. Copy /boot/piget/config/network/interfaces to /etc/network/interfaces |                                             |

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

| /do/core/net/wifiBridge                              |                                                                                                                                                    |
|:-----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Info                                                 | [alpha] [undocumented]                                                                                                                             |
| Modules                                              | /do/dhcpd/wlan0asHotSpot, /do/hostapd/install, /do/hostapd/start,                                                                                  |
| System                                               | /system/downloadModule dhcpd, /system/autoBackup "/etc/network/interfaces", /system/autoBackup "/etc/sysctl.conf", /system/downloadModule hostapd, |
| 1. Use wifi (wlan0) as an hotspot                    |                                                                                                                                                    |
| 2. Configure wifi with static address (192.168.42.1) |                                                                                                                                                    |
| 1. Turn off wlan0                                    |                                                                                                                                                    |
| 2. Modify /etc/network/interfaces                    |                                                                                                                                                    |
| 3. move WPASupplicant.service                        |                                                                                                                                                    |
| 3. BRIDGE ETH0 => WLAN0                              |                                                                                                                                                    |
| 1. Modify /etc/sysctl.conf                           |                                                                                                                                                    |
| 2. Setup iptables (firewall)                         |                                                                                                                                                    |
| 3. Save iptables                                     |                                                                                                                                                    |
| 4. Reset wlan0 to 192.168.42.1                       |                                                                                                                                                    |

| /do/core/net/wifiCheck   |                        |
|:-------------------------|:-----------------------|
| Info                     | [alpha] [undocumented] |

| /do/core/net/wifiDriver       |                        |
|:------------------------------|:-----------------------|
| Info                          | [alpha] [undocumented] |
| 1. Installing driver for wifi |                        |

| /do/core/net/wifiDriverLocal                    |                        |
|:------------------------------------------------|:-----------------------|
| Info                                            | [alpha] [undocumented] |
| 1. Installing driver for wifi from /boot/piget/ |                        |

| /do/core/net/wifiDriverRalink              |                                  |
|:-------------------------------------------|:---------------------------------|
| Info                                       | [alpha] [undocumented]           |
| Softwares                                  | firmware-ralink,                 |
| System                                     | /system/install firmware-ralink, |
| 1. Install drivers for ralink WI-FI dongle |                                  |
| 2. Reboot to finish installation           |                                  |

| /do/core/net/wifiFixSlow   |                                      |
|:---------------------------|:-------------------------------------|
| Info                       | [alpha] [undocumented]               |
| System                     | /system/autoBackup /etc/sysctl.conf, |
| 1. Fix wifi slowliness     |                                      |

| /do/core/net/wifiHotSpot                             |                                                                                                |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| Info                                                 | [alpha] [undocumented]                                                                         |
| Modules                                              | /do/dhcpd/wlan0asHotSpot, /do/hostapd/install, /do/hostapd/redirectTraffic, /do/hostapd/start, |
| System                                               | /system/autoBackup "/etc/network/interfaces", /system/downloadModule hostapd,                  |
| 1. Use wifi (wlan0) as an hotspot                    |                                                                                                |
| 2. Configure wifi with static address (192.168.42.1) |                                                                                                |
| 1. Turn off wlan0                                    |                                                                                                |
| 2. Modify /etc/network/interfaces                    |                                                                                                |
| 3. move WPASupplicant.service                        |                                                                                                |
| 4. Reset wlan0 to 192.168.42.1                       |                                                                                                |

| /do/core/net/wifiHotSpotRemove   |                                                         |
|:---------------------------------|:--------------------------------------------------------|
| Info                             | [alpha] [undocumented]                                  |
| System                           | /system/remove isc-dhcp-server, /system/remove hostapd, |
| 1. move WPASupplicant.service    |                                                         |

