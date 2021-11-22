"""
PIN3APPLE - it's a little util to fast setup ANANAZZ I3 configuration.
AUTHOR - ANANAZ(https://github.com/Avdushin)
Program support from September 12, 2021
Avdushin - copyright 2021
"""
from rich import print
from pyfiglet import figlet_format
from ver import ver

import pyfiglet, webbrowser, platform, os, sys

os.system('clear')

# logo
prname = figlet_format(" PIN3APPLE")
print(f"[yellow]{prname}")

# ver
print(f" [yellow]VERSION: {ver}")

# os
myos = platform.platform()

#  languages
def language():
	print("\n 1) 🇷🇺 РУССКИЙ \n\n 2) 🇬🇧 English \n\n 5) Back\n\n 0) [red b]Quit\n\n")
	
	lang = input(" Выберите язык/Choose language: ")

#  language coose / выбор языка
	if lang == "1":
		os.system("python3 src/pineapple-ru.py")
	elif lang == "2":
		os.system("python3 src/pineapple.py")
	elif lang == "5":
		menu()
	elif lang == "0":
		print("")
	else:
		language()

# info
def info():
	man = "https://telegra.ph/PN3APPLE-ENG-INFO-10-23"
	webbrowser.open(man, new=2)
	print("[green b]  The documentation was opened in a browser!")

""" MENUS """

# general menu
def menu():
	import os
	print("\n [b cyan]1)[yellow] DISTROS [b cyan] 2) [yellow]MY OS")
	print("\n [b cyan]3)[yellow] INFO    [b cyan] 4) [yellow]Uninstall[cyan]\n\n 5) [yellow]language [cyan]0) [red]Quit \n")
	wtd = input(" Coose an action: ")
	print("")

	# choose logical
	if wtd == "1":
		distros()
	elif wtd == "2":
		print(f' Your system is {myos}')
		menu()
	elif wtd == "3":
		info()
		menu()
	elif wtd == "4":
		import os
		os.system('sh src/uninstall.sh')
	elif wtd == "5":
		language()
	elif wtd == "0":
		print("")
	else:
		menu()

# distros 
def distros():
	import os
	print("\n [b cyan]1) [#808080]Ubuntu  [b cyan]2) [#2C67DF]Solus")
	print("\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]4)[#2C50DF] Fedora[b cyan]\n\n 5)[white] Back    [b cyan] 0)[b red] Quit\n")
	dist = input(" Choose your distro: ")
	# Install logic
	if dist == "1":
		print('\n[red b]Ubuntu support has been suspended...')
		distros()
		# os.system('sh src/distros/Ubuntu/ubuntu.sh')
	elif dist == "2":
		os.system('sh src/distros/Solus/solus.sh')
	elif dist == "3":
		os.system('sh src/distros/Manjaro/manjaro.sh')
	elif dist == "4":
		os.system('sh src/distros/Fedora/fedora.sh')
	elif dist == "5":
		menu()
	elif dist == "0":
		print("")
	else:
		distros()
menu()