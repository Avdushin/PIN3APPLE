sudo pacman -S python-pip --noconfirm
yay -S python39 --noconfirm
clear
echo 'Iinstalling requirements...'
pip3 install -r src/requirements.txt
clear
echo 'Successful installation!'
sh pineapple.sh