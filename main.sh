clear
echo "Installing requirements..."
/usr/bin/python3.9 -m pip install --upgrade pip
pip3 install termcolor
pip3 install pyfiglet
echo "DONE!"
sleep 2
clear
python3 main.py
