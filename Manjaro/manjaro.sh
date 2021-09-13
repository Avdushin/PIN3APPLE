#!/bin/bash
sudo mkdir -p ~/.appz && sudo mkdir -p ~/.config/i3/ &&  sudo tar -C $HOME -xzf NoiseTorch_x64.tgz && sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz && gtk-update-icon-cache && sudo cp Solus/config ~/.config/i3 && sudo cp -r polybar/ ~/.config/  && sudo cp -r kitty/ ~/.config/ && sudo echo "# remove welcome text
 set -g fish_greeting" > ~/.config/fish/config.fish && sudo echo "fish
     source /usr/share/defaults/etc/profile
     #noisetorch
     if [ -d "$HOME/.local/bin" ] ; then
         PATH="$HOME/.local/bin:$PATH"
     fi" > ~/.bashrc && sudo cp -r walls/ ~/ && echo "DONE!" && reboot && exit
