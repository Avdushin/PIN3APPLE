#!/bin/bash
sudo apt-get update -y
clear
echo -e "\e[0;92mUbuntu script starting..."
sudo apt-get install i3 i3blocks i3status i3-gaps i3lock polybar kitty krita fish ack vim bottom neofetch flameshot variety feh rofi discord steam telegram-desktop picom gcolor3 lxappearance flatpak xdg-desktop-portal-gtk fontawesome-fonts -y
sudo mkdir -p ~/.appz
sudo mkdir -p ~/.config/i3/
sudo mkdir -p ~/.local/share/Trash/files
sudo tar -C $HOME -xzf src/packages/NoiseTorch_x64.tgz
sudo tar -xf src/packages/sublime_text_build_4113_x64.tar.xz  -C ~/.appz && gtk-update-icon-cache && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo cp src/distros/Ubuntu/config ~/.config/i3/
sudo cp -r src/polybar/ ~/.config/
sudo cp -r src/kitty/ ~/.config/
sudo flatpak install flathub com.rafaelmardojai.Blanket -y
sudo cp -r src/dots/.bashrc ~/
sudo chsh -s /usr/bin/fish
chsh -s /usr/bin/fish
sudo cp -r src/assets/walls/ ~/
sudo cp -r src/assets/Themes/Solarized-Dark-Blue Themes/Solarized-Dark-Cyan /usr/share/themes/
sudo cp -r src/assets/icons/Tela-blue/ icons/Tela-blue-dark/ /usr/share/icons/
sudo cp -r src/dots/.fonts ~/
echo -e "\e[0;92mDONE!"
echo -e "\e[0;91m!\e[0;1;33mYour system will be \e[0;91mREBOOT!"
sleep 5
reboot 
