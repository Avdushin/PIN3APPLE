clear
echo -e "\e[0;92mUpdating..."
sudo eopkg up -y
clear
sudo apt-get update -y
clear
sudo pacman -Suy
clear
sudo dnf update -y
clear
echo -e "\e[0;92mInstalling requirements...\e[0;1;33m"
/usr/bin/python3.9 -m pip install --upgrade pip
pip3 install rich
pip3 install pyfiglet
pip3 install printy
echo -e "\e[0;92mDONE!"
sleep 2
clear
python3 pineapple.py
