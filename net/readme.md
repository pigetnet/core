core/net

This module manages network connection

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

# WIFI

Check if WIFI is connected
```
/net/isWifi
```
