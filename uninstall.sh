clear
echo -e "\e[0;31mUNINSTALLING PIN3APPLE CONFIG...\e[0m"
sudo rm -rf ~/.config/i3/config ~/.config/polybar/ ~/.config/kitty/ ~/.config/variety/ ~/.appz/ ~/walls/
sudo eopkg rm i3 i3blocks i3status i3-devel i3lock polybar kitty krita xkill fish ack bottom vim neofetch variety feh flameshot rofi discord steam telegram gcolor3 lxappearance picom flatpak xdg-desktop-portal-gtk font-awesome-4 font-awesome-ttf -y 
echo -e "\e[0;92mDONE!"