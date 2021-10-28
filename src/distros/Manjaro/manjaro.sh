#!/bin/bash
sudo pacman -Syu
clear
echo -e "\e[0;92mManjaro script starting..."
sudo pacman -Syu yay i3 i3blocks i3status i3lock polybar kitty krita fish ack vim bottom neofetch flameshot variety feh rofi discord python-pip steam telegram-desktop gcolor3 lxappearance picom flatpak xdg-desktop-portal-gtk awesome-terminal-fonts -y 
sudo mkdir -p ~/.appz
sudo mkdir -p ~/.config/i3/
sudo mkdir -p ~/.local/share/Trash/files
sudo tar -C $HOME -xzf NoiseTorch_x64.tgz
sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz && gtk-update-icon-cache && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo cp Manjaro/config ~/.config/i3
sudo cp -r polybar/ ~/.config/  
sudo cp -r kitty/ ~/.config/
sudo flatpak install flathub com.rafaelmardojai.Blanket -y 
sudo cp -r .bashrc ~/ 
sudo chsh -s /usr/bin/fish
chsh -s /usr/bin/fish 
sudo cp -r Themes/Solarized-Dark-Blue Themes/Solarized-Dark-Cyan /usr/share/themes/ 
sudo cp -r icons/Tela-blue/ icons/Tela-blue-dark/ /usr/share/icons/ 
sudo cp -r .fonts ~/ 
echo -e "\e[0;92mDONE!"
echo -e "\e[0;91m!\e[0;1;33mYour system will be \e[0;91mREBOOT!"
sleep 5
reboot 
