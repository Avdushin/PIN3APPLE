"""
PIN3APPLE - утилита для быстрой установки моей конфигурации I3wm
АВТОР - ANANAZ(https://github.com/Avdushin)
Программа поддерживается с 12 сентября, 2021
Avdushin - copyright 2021
"""
from rich import print
from pyfiglet import figlet_format
from ver import ver

import pyfiglet, platform, os, sys

os.system('clear')

# лого
prname = figlet_format(" PIN3APPLE")
print(f"[yellow]{prname}")

# версия
print(f" [yellow]ВЕРСИЯ: {ver}")

# ос
myos = platform.platform()

# информация
def info():
	 print("\n[yellow b]Как это работает?\nВыберите ваш дистрибутив, и дождитесь окончания установки.\n\n[white]ИНСТРУКЦИЯ:\n[#46C959][[#CE270B]РУС[/#CE270B]][/#46C959] - [green]https://telegra.ph/PN3APPLE-RUS-INFO-10-23\n[#46C959][[#CE270B]ENG[/#CE270B]][/#46C959] - [green]https://telegra.ph/PN3APPLE-ENG-INFO-10-23\n")

""" МЕНЮ """

# главное меню
def menu():
	import os
	print("\n [b cyan]1)[yellow] ДИСТРИБУТИВЫ [b cyan]2) [yellow]МОЯ СИСТЕМА")
	print("\n [b cyan]3)[yellow] Мануал       [b cyan]4) [yellow]Удалить изменения[cyan]\n\n 5) [yellow]Язык [cyan]        0) [red]Выход \n")
	wtd = input(" Выберите действие: ")
	print("")

	# логика выбора действий
	if wtd == "1":
		distros()
	elif wtd == "2":
		print(f'Ваша система {myos}')
		menu()
	elif wtd == "3":
		info()
		menu()
	elif wtd == "4":
		import os
		os.system('sh uninstall.sh')
	elif wtd == "5":
		os.system('python3 main.py')
	elif wtd == "0":
		print("")
	else:
		menu()

# дистрибутивы
def distros():
	import os
	print("\n [b cyan]1) [#DF5B2C]Ubuntu  [b cyan]2) [#2C67DF]Solus")
	print("\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]4)[#2C50DF] Fedora[b cyan]\n\n 5)[white] Назад    [b cyan] 0)[b red] Выход\n")
	dist = input(" Выберите ваш дистрибутив: ")
	# логика установки
	if dist == "1":
		os.system('sh src/distros/Ubuntu/ubuntu.sh') 
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