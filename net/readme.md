core/net
--------

This sub-module manages network connection    
[Dev manual](https://github.com/pigetnet/core/blob/dev/net/doc/manual.md)    
[Dev manual (long)](https://github.com/pigetnet/core/blob/dev/net/doc/manual_long.md)    


# Internet connection

Disconnect Raspberry Pi by removing default route
```
/net/internetOff
```

Reconnect gateway
```
/net/internetOn GATEWAY_IP
/net/internetOn 192.168.0.254
```
# Socket

Send a message to a socket
```
/net/socketSend PORT MESSAGE
/net/socketSend 80 "Hello World"
```
Read a message from a socket
```
/net/socketRead PORT
/net/socketRead "Hello World"
```

# Hosts / interfaces files
Change hostname in /etc/hostname and /etc/hosts    
**Default :** reset name to /user/settings/pi/name.txt
```
/net/resetHost
/net/resetHost NAME
/net/resetHost raspberrypi
```

Reset /etc/network/interfaces to default
```
/net/resetNetwork
```
