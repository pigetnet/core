Piget is a repository for scripts to automate software and components installation on the Raspberry Pi   
Instead of typing complex commands and modify configuration files, you can use short command instead.   

Piget doesn't modify how your Raspberry Pi will works, it's only a bunch of scripts and symbolic links, if
you know how to make scripts and upload code on github, you know how to make scripts for piget.

# How to install Piget
Piget will only works on Raspbian (and was meant to be used with Raspbian Lite)

You just need to copy-paste this command in your terminal  to install Piget.
```
curl -L piget.madnerd.org | sudo bash
```

You can also download a ready-to-go image here:
[piget.zip](https://github.com/pigetnet/core/releases/download/v1.0/piget.zip)    

# Setup your Raspberry Pi
We can setup our Raspberry Pi using a menu, by typing :
```
/pi/setup
```
![/pi/setup](https://github.com/pigetnet/core/raw/master/doc/pi-setup.png)

*  Choose a name for your Raspberry Pi
*  Choose a password for the terminal (user: pi)
*  Choose a colour (This can be useful to differentiate Raspberry Pi)

# Useful commands

* Rename your Raspberry Pi
````
/pi/name name
/pi/name madnerd
````
* Change password
```
passwd pi
```
* Resize SD card
```
/pi/resizeSD
```
* Update Raspberry Pi
/pi/update

* Install a module
```
/pi/install module
/pi/install led
```
* Display help for a command
```
/show/help command
/show/help /pi/name
```
# What happens during install
YOu can find the script here : http://piget.madnerd.org

The installer will
 *  update your Raspberry Pi
 *  install some dependencies
 *  setup Piget
 *  setup the time zone

Here is more details :
* Check your internet connectivity
* Update Raspberry Pi :  (apt-get update / apt-get upgrade)
* Install dependencies :  (git / python-pip / tabulate /  tzupdate )
* Copy bashrc banner
    * /home/pi/.bashrc (Terminal banner for user pi)
    * /root/.bashrc (Terminal banner for user root)
 * Clone github.com/pigetnet/core on /opt/piget/core (This folder contains all core scripts on Piget)
* Create folders 
    * /opt/user (personal files)
    * /opt/user/settings (settings)
* Create symbolic links
    * /opt/user --> /user/ (User data)
    * /opt/piget --> /do/ (Piget modules)
    * /opt/piget/core/pi --> /pi/ (Raspberry Pi settings)
    * /opt/piget/core/net --> /net/ (Network setup)
    * /opt/piget/core/show --> /show/ (Variables / Display)
    * /opt/piget/core/string --> /string/ (String Manipulation)
    * /opt/piget/core/system --> /system/ (System scripts for modules)
*   Setup time zone based on IP thanks to tzupdate.
