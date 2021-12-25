"""
PIN3APPLE - утилита для быстрой установки моей конфигурации I3wm
АВТОР - ANANAZ(https://github.com/Avdushin)
Программа поддерживается с 12 сентября, 2021
Avdushin - copyright 2021
"""
from rich import print
from pyfiglet import figlet_format
from ver import ver

import pyfiglet, webbrowser, platform, os, sys

os.system('clear')

# лого
prname = figlet_format(" PIN3APPLE")
print(f"[yellow]{prname}")

# версия
print(f" [yellow]ВЕРСИЯ: {ver}")

# ос
myos = platform.platform()

#  languages
def language():
	print("\n 1) 🇷🇺 РУССКИЙ \n\n 2) 🇬🇧 English \n\n 5) Назад \n\n 0) [red b]Выход\n\n")
	
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

# информация
def info():
	man = "https://telegra.ph/PN3APPLE-RUS-INFO-10-23"
	webbrowser.open(man, new=2)
	print("[green b]  Документация открыта в браузере!\n")
	print("[green b]  Нажмите[red b] ENTER[green b] чтобы открыть главное меню.")

""" МЕНЮ """

# главное меню
def menu():
	import os
	print("\n [b cyan]1)[yellow b] ДИСТРИБУТИВЫ [b cyan]2) [yellow b]МОЯ СИСТЕМА")
	print("\n [b cyan]3)[yellow b] Мануал       [b cyan]4) [yellow b]ДЕИНСТАЛЛЯТОР[cyan]\n\n 5) [yellow b]Язык [cyan]        0) [red]Выход \n")
	wtd = input(" Выберите действие: ")
	print("")

	# логика выбора действий
	if wtd == "1":
		distros()
	elif wtd == "2":
		print(f' Ваша система {myos}')
		menu()
	elif wtd == "3":
		info()
		menu()
	elif wtd == "4":
		import os
		os.system('sh src/uninstallru.sh')
	elif wtd == "5":
		language()
	elif wtd == "0":
		print("")
	else:
		menu()

""" Majaro дополнительные программы """

def alt_1():
	alt_inst = input(" Вы хостите установить betterlockscreen? [Y/n]:")
	if alt_inst == "Y":
		os.system('yay -S betterlockscreen')
	elif alt_inst == "y":
		os.system('yay -S betterlockscreen')
	elif alt_inst == "N":
		alt_2()
	elif alt_inst == "n":
		alt_2()
	else:
		alt_1()

def alt_2():
	alt_inst = input(" Вы хостите установить picom-jonaburg-git (закругленные края окон)? [Y/n]:")
	if alt_inst == "Y":
		os.system('yay -S picom-jonaburg-git')
		os.system('sh src/distros/Manjaro/manjaro.sh')
	elif alt_inst == "y":
		os.system('yay -S picom-jonaburg-git')
		os.system('sh src/distros/Manjaro/manjaro.sh')
	elif alt_inst == "N":
		print('\n [green b]Installing Manjaro I3 config...\n')
		os.system('sh src/distros/Manjaro/manjaro.sh')
	elif alt_inst == "n":
		print('\n [green b]Installing Manjaro I3 config...\n')
		os.system('sh src/distros/Manjaro/manjaro.sh')
	else:
		alt_2()

""" ДИСТРИБУТИВЫ """


# Меню дистрибутивов
def distros():
	import os
	print(" [b cyan]1) [#2C67DF]Solus  [b cyan] 2) [#2C50DF] Fedora[b cyan]\n")
	print(" [b cyan]3) [#2CDF6E]Manjaro [b cyan]\n\n 5)[white] Назад    [b cyan]0)[b red] Выход\n")
	dist = input(" Выберите ваш дистрибутив: ")
	# логика установки
	if dist == "1":
		os.system('sh src/distros/Solus/solus.sh')
	elif dist == "2":
		os.system('sh src/distros/Fedora/fedora.sh')
	elif dist == "3":
		print(" [green b]Установка AUR...")
		os.system('sudo pacman -S yay')
		alt_1()
		alt_2()
	elif dist == "5":
		menu()
	elif dist == "0":
		print("")
	else:
		distros()
menu()