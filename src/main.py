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

""" sys funcs """

# cls
def cls():
	os.system('clear')

# logo
def logo():
	prname = figlet_format(" PIN3APPLE")
	print(f"[yellow]{prname}")
	# ver
	# print(f" [yellow]VERSION: {ver}")

# unlogo
def unlogo():
	prname = figlet_format(" UNINSTALLER")
	print(f"[yellow]{prname}")

# my os
def myos():
	cls()
	logo()
	os.system('screenfetch')
	mm()

# my os ru
def myosru():
	cls()
	logo()
	os.system('screenfetch')
	mmru()

#  languages
def language():
	cls()
	logo()
	print("\n 1) 🇷🇺 РУССКИЙ \n\n 2) 🇬🇧 English \n\n 5) Back  0) [red b]Quit\n\n")
	
	lang = input(" Выберите язык/Choose language: ")
	
	#  language coose / выбор языка
	if lang == "1":
		cls()
		logo()
		mmru()
	elif lang == "2":
		cls()
		logo()
		mm()
	elif lang == "5":
		cls()
		logo()
		mm()
	elif lang == "0":
		print("")
	else:
		language()


""" MENUS """
# ENGLISH

# main menu
def mm():
	print("\n [b cyan]1)[yellow] DISTROS [b cyan] 2) [yellow]MY OS")
	print("\n [b cyan]3)[yellow] INFO    [b cyan] 4) [yellow]Uninstall[cyan]\n\n 5) [yellow]language [cyan]0) [red]Quit \n")
	wtd = input(" Coose an action: ")
	print("")

	# choose logical
	if wtd == "1":
		dm();
	elif wtd == "2":
		cls()
		logo()
		myos()
	elif wtd == "3":
		info()
	elif wtd == "4":
		uninstall()
	elif wtd == "5":
		language()
	elif wtd == "0":
		print("")
	else:
		cls()
		logo()
		mm()

# Distros menu
def dm():
	cls()
	logo()
	print("\n [b cyan]1) [#2C67DF]Solus  [b cyan] 2) [#2C50DF] Fedora[b cyan]\n\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]      \n\n 5)[white] Back    [b cyan]0)[b red] Quit\n")
	dist = input(" Choose your distro: ")
	# Install logic
	if dist == "1":
		os.system('sh src/distros/Solus/solus.sh')
	elif dist == "2":
		os.system('sh src/distros/Fedora/fedora.sh')
	elif dist == "3":
		print(" [green b]Installing AUR...")
		os.system('sudo pacman -S yay')
		os.system('sh src/distros/Manjaro/manjaro.sh')
	elif dist == "5":
		cls()
		logo()
		mm()
	elif dist == "0":
		print("")
	else:
		dm()

# info
def info():
	cls()
	logo()
	print(f"[yellow] VERSION: {ver}\n [yellow]EDITION: [white]PIN3APPLE 2021 [Python 3.10]\n [yellow]AUTHOR: [green]https://github.com/Avdushin\n\n [yellow]DOCUMENTATON: [green]https://telegra.ph/PN3APPLE-ENG-INFO-10-23\n\n [cyan]5) [yellow]Back   [cyan]0) [red] Quit\n")

	# nav input
	ifo_nav = input(" Coose an action: ")

	if ifo_nav == "5":
		cls()
		logo()
		mm()
	elif ifo_nav == "0":
		print("")
	else:
		cls()
		info()

""" UNINST """

def uninstall():
	cls()
	unlogo()

	# distros
	print("\n [b cyan]1) [#2C67DF]Solus  [b cyan] 2) [#2C50DF] Fedora[b cyan]\n\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]      \n\n 5)[white] Back    [b cyan]0)[b red] Quit\n")

	# uninstall cfg input
	touninst = input(" Choose to uninstall: ")

	if touninst == "0":
		print("")
	elif touninst == "1":
		os.system('sh distros/Solus/uninst.sh')
	elif touninst == "2":
		os.system('sh distros/Fedora/uninst.sh')
	elif touninst == "3":
		os.system('sh distros/Manjaro/uninst.sh')
	elif touninst == "5":
		cls()
		logo()
		mm()

# RUSSIAN

# main menu ru
def mmru():
	print("\n [b cyan]1)[yellow] ДИСТРИБУТИВЫ [b cyan] 2) [yellow]МОЯ ОС")
	print("\n [b cyan]3)[yellow] О ПРОЕКТЕ    [b cyan] 4) [yellow]ДЕИНСТАЛЛЯТОР[cyan]\n\n 5) [yellow]Язык          [cyan]0) [red b]Выход \n")
	wtd = input(" Выберите действие: ")
	print("")

	# логика выбора
	if wtd == "1":
		dmru();
	elif wtd == "2":
		cls()
		logo()
		myosru()
	elif wtd == "3":
		inforu()
	elif wtd == "4":
		uninstallru()
	elif wtd == "5":
		language()
	elif wtd == "0":
		print("")
	else:
		cls()
		logo()
		mmru()

# distro menu ru
def dmru():
	cls()
	logo()
	print("\n [b cyan]1) [#2C67DF]Solus  [b cyan] 2) [#2C50DF] Fedora[b cyan]\n\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]      \n\n 5)[white] Назад    [b cyan]0)[b red] Выход\n")
	dist = input(" Выберите дистрибутив: ")
	# Install logic
	if dist == "1":
		os.system('sh src/distros/Solus/solus.sh')
	elif dist == "2":
		os.system('sh src/distros/Fedora/fedora.sh')
	elif dist == "3":
		print(" [green b]Установка AUR...")
		os.system('sudo pacman -S yay')
		os.system('sh src/distros/Manjaro/manjaro.sh')
	elif dist == "5":
		cls()
		logo()
		mmru()
	elif dist == "0":
		print("")
	else:
		dmru()

# info ru
def inforu():
	cls()
	logo()
	print(f"[yellow] ВЕРСИЯ: {ver}\n [yellow]ИЗДАНИЕ: [white]PIN3APPLE 2021 [Python 3.10]\n [yellow]АВТОР: [green]https://github.com/Avdushin\n\n [yellow]ДОКУМЕНТАЦИЯ: [green]https://telegra.ph/PN3APPLE-ENG-INFO-10-23\n\n [cyan]5) [yellow]Назад   [cyan]0) [red] Выход\n")

	# nav input
	ifo_nav = input(" Выберите действие: ")

	if ifo_nav == "5":
		cls()
		logo()
		mmru()
	elif ifo_nav == "0":
		print("")
	else:
		cls()
		inforu()


# uninstall ru
def uninstallru():
	cls()
	unlogo()

	# distros
	print("\n [b cyan]1) [#2C67DF]Solus  [b cyan] 2) [#2C50DF] Fedora[b cyan]\n\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]      \n\n 5)[white] Назад    [b cyan]0)[b red] Выход\n")

	# uninstall cfg input
	touninst = input(" Выберите что удалить: ")

	if touninst == "0":
		print("")
	elif touninst == "1":
		os.system('sh distros/Solus/uninst.sh')
	elif touninst == "2":
		os.system('sh distros/Fedora/uninst.sh')
	elif touninst == "3":
		os.system('sh distros/Manjaro/uninst.sh')
	elif touninst == "5":
		cls()
		logo()
		mmru()

""" EXEC """

cls()
logo()
mm()