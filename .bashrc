fish
source /usr/share/defaults/etc/profile

#noisetorch

if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

echo " 
#fish_config
if status is-interactive
    # Commands to run in interactive sessions can go here
set -g fish_greeting
end " > ~/.config/fish/config.fish