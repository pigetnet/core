# ~/.bashrc: executed by bash(1) for non-login shells.

# Custom prompt
PS1='\[\033[31m\]\h.local\[\033[0m\]:\[\033[01;34m\]\w \$\[\033[00m\] '

# Pretty Terminal
export LS_OPTIONS='--color=auto'
eval "`dircolors`"
alias ls='ls $LS_OPTIONS'
alias ll='ls $LS_OPTIONS -l'
alias l='ls $LS_OPTIONS -lA'

#Easy coloring scripts
export OK="\\033[1;32m"
export NORMAL="\\033[0;39m"
export ERR="\\033[1;31m"
export INFO="\\033[1;34m"
export WARN="\\033[1;33m"
export PICOLOR="\\033[1;35m"
export BLACK="\\033[0;30m"
export BLUE="\\0034[0;34m"
export GREEN="\\033[0;32m"

# Logo
echo -ne $OK
clear
cat<<EOF
██████╗ ██╗ ██████╗ ███████╗████████╗
██╔══██╗██║██╔════╝ ██╔════╝╚══██╔══╝
██████╔╝██║██║  ███╗█████╗     ██║
██╔═══╝ ██║██║   ██║██╔══╝     ██║
██║     ██║╚██████╔╝███████╗   ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝   ╚═╝
EOF

# Help
echo -ne $NORMAL
echo "-------------------------"
echo -e "Display help:$OK /show/help $NORMAL"
echo -e "Display help for a command:$OK /show/help $ERR command $NORMAL or $ERR command $NORMAL $OK--help $NORMAL"
echo -e "Setup your Raspberry pi: $OK /pi/setup $NORMAL"
echo -e "Setup WIFI: $OK /pi/wifi $NORMAL"
echo "-------------------------"


