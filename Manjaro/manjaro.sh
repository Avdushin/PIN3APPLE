<<<<<<< HEAD
#!/bin/bash
=======
     #!/bin/bash
>>>>>>> 2f768ba0fcee8acb33008f9387e472c3a4fe61f8
sudo pacman -Syu yay i3 i3blocks i3status i3lock polybar kitty krita fish ack vim neofetch flameshot feh rofi discord steam telegram-desktop gcolor3 lxappearance flatpak xdg-desktop-portal-gtk awesome-terminal-fonts -y && sudo mkdir -p ~/.appz && sudo mkdir -p ~/.config/i3/ && sudo mkdir -p ~/.local/share/Trash/files &&  sudo tar -C $HOME -xzf NoiseTorch_x64.tgz && sudo tar -xf sublime_text_build_4113_x64.tar.xz  -C ~/.appz && gtk-update-icon-cache && flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo && sudo cp Manjaro/config ~/.config/i3 && sudo cp -r polybar/ ~/.config/  && sudo cp -r kitty/ ~/.config/ && sudo flatpak install flathub com.rafaelmardojai.Blanket -y && fish && sudo echo "# remove welcome text
 set -g fish_greeting" > ~/.config/fish/config.fish && sudo echo "fish
     source /usr/share/defaults/etc/profile
     #noisetorch
     if [ -d "$HOME/.local/bin" ] ; then
         PATH="$HOME/.local/bin:$PATH"
     fi" > ~/.bashrc && sudo cp -r walls/ ~/ && echo "DONE!" && reboot && exit