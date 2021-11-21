clear
echo -e "\e[0;92mUpdating..."
sudo eopkg up -y
clear
sudo apt-get update -y
sudo apt install python3-pip -y
clear
sudo pacman -Suy
sudo pacman -S python-pip
clear
sudo dnf update -y
clear
echo -e "\e[0;92mInstalling requirements...\e[0;1;33m"
/usr/bin/python3.9 -m pip install --upgrade pip
pip3 install rich
pip3 install pyfiglet
pip3 install tqdm
echo -e "\e[0;92mDONE!"
sleep 2
clear
python3 src/pineapple.py
