#!/bin/bash
sudo eopkg it i3 i3blocks i3status i3-devel i3lock polybar kitty krita xkill fish ack vim neofetch feh rofi discord steam telegram gcolor3 lxappearance  flatpak xdg-desktop-portal-gtk font-awesome-4 font-awesome-ttf -y && sudo wget https://download.sublimetext.com/sublime_text_build_4113_x64.tar.xz && wget https://github.com/lawl/NoiseTorch/releases/download/0.11.3/NoiseTorch_x64.tgz && sudo tar -C $HOME -xzf NoiseTorch_x64.tgz && gtk-update-icon-cache && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo && sudo mkdir -p ~/.config/i3/ && sudo cp config config-polybar ~/.config/i3/ && sudo mkdir -p ~/.appz && sudo cp -r kitty/ ~/.config/ && sudo flatpak install flathub com.rafaelmardojai.Blanket -y && fish && sudo echo "# remove welcome text
 set -g fish_greeting" > ~/.config/fish/config.fish && sudo echo "fish
     source /usr/share/defaults/etc/profile
     #noisetorch
     if [ -d "$HOME/.local/bin" ] ; then
         PATH="$HOME/.local/bin:$PATH"
     fi" > ~/.bashrc  && sudo cp -r polybar/ ~/.config/ && sudo cp -r /walls/ ~/ && sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz && reboot && 