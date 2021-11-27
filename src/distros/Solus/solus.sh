#!/bin/bash
sudo eopkg up -y
clear
echo -e "\e[0;92mSolus script starting..."
sudo eopkg it i3 i3blocks i3status i3-devel i3lock polybar kitty krita xkill fish ack vim bottom neofetch variety feh flameshot rofi discord steam telegram gcolor3 lxappearance picom flatpak xdg-desktop-portal-gtk font-awesome-4 font-awesome-ttf -y 
sudo mkdir -p ~/.appz
sudo mkdir -p ~/.config/i3/
sudo tar -C $HOME -xzf src/packages/NoiseTorch_x64.tgz
sudo tar -xf src/packages/sublime_text_build_4113_x64.tar.xz  -C ~/.appz && gtk-update-icon-cache
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 
sudo cp src/distros/Solus/config ~/.config/i3/
sudo cp -r src/polybar/ ~/.config/
sudo cp -r src/kitty/ ~/.config/
sudo flatpak install flathub com.rafaelmardojai.Blanket -y
sudo cp -r src/dots/.bashrc ~/
sudo chsh -s /usr/bin/fish
chsh -s /usr/bin/fish
sudo cp -r src/assets/walls/ ~/
sudo cp -r src/assets/Themes/Solarized-Dark-Blue src/assets/Themes/Solarized-Dark-Cyan /usr/share/themes/
sudo cp -r src/assets/icons/Tela-blue/ src/assets/icons/Tela-blue-dark/ /usr/share/icons/
sudo cp -r src/dots/.fonts ~/
sudo cp -r src/dots/git_token ~/
echo -e "\e[0;92mDONE!"
echo -e "\e[0;91m!\e[0;1;33mYour system will be \e[0;91mREBOOT!"
sleep 5
reboot 