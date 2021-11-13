import pyfiglet, os, sys

from rich import print
from pyfiglet import figlet_format

# clear terminal / очистка терминала
os.system('clear')

# logo / лого
prname = figlet_format(" PIN3APPLE")
print(f"[yellow]{prname}")

def language():
	print("\n 1)РУССКИЙ \n\n 2)English\n")
	
	lang = input(" Выберите язык/Choose language: ")

#  language coose / выбор языка
	if lang == "1":
		os.system("python3 pineapple-ru.py")
	elif lang == "2":
		os.system("python3 pineapple.py")
	else:
		language()
language()