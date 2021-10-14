#!/bin/bash
echo -e "\e[0;92mSolus script starting..."
sudo eopkg it i3 i3blocks i3status i3-devel i3lock polybar kitty krita xkill fish ack vim neofetch variety feh flameshot rofi discord steam telegram gcolor3 lxappearance picom flatpak xdg-desktop-portal-gtk font-awesome-4 font-awesome-ttf -y 
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/getsolus/3rd-party/master/network/web/browser/google-chrome-stable/pspec.xml google-chrome-*.eopkg;sudo rm google-chrome-*.eopkg -y 
sudo mkdir -p ~/.appz
sudo mkdir -p ~/.config/i3/
sudo tar -C $HOME -xzf NoiseTorch_x64.tgz
sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz && gtk-update-icon-cache
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 
sudo cp Solus/config ~/.config/i3
sudo cp -r polybar/ ~/.config/
sudo cp -r kitty/ ~/.config/
sudo flatpak install flathub com.rafaelmardojai.Blanket -y
sudo cp -r .bashrc ~/
sudo chsh -s /usr/bin/fish
chsh -s /usr/bin/fish
sudo cp -r walls/ ~/
sudo cp -r Themes/Solarized-Dark-Blue Themes/Solarized-Dark-Cyan /usr/share/themes/
sudo cp -r icons/Tela-blue/ icons/Tela-blue-dark/ /usr/share/icons/
sudo cp -r .fonts ~/
echo "\e[0;92mDONE!"
echo "\e[0;1;33m!Your system will be \e[0;91mREBOOT!"
echo ""
echo ""
echo ""
reboot 