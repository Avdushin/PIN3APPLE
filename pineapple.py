"""
PIN3APPLE - it's a little util to fast setup ANANAZZ I3 configuration.
AUTHOR - ANANAZ(https://github.com/Avdushin)
Program support from September 12, 2021
Avdushin - copyright 2021
"""
from rich import print
from pyfiglet import figlet_format

import pyfiglet, platform, os, sys

os.system('clear')

# logo
prname = figlet_format(" PIN3APPLE")
print(f"[yellow]{prname}")

# version
ver = ("[red]3.0")
print(f" [yellow]VERSION: {ver}")

# os
myos = platform.platform()

# info
def info():
	 print("\n[yellow b]HOW IT WORKS?\nCHOOSE YOUR DISTRO, WAIT SOME MINUTES AND RELAX!\n\n[white]INSTRUCTION:\n[#46C959][[#CE270B]RUS[/#CE270B]][/#46C959] - [green]https://telegra.ph/PN3APPLE-RUS-INFO-10-23\n[#46C959][[#CE270B]ENG[/#CE270B]][/#46C959] - [green]https://telegra.ph/PN3APPLE-ENG-INFO-10-23\n")

""" MENUS """

# general menu
def menu():
	import os
	print("\n [b cyan]1)[yellow] DISTROS [b cyan]2) [yellow]MY OS")
	print("\n [b cyan]3)[yellow] INFO    [b cyan]4) [yellow]Uninstall[cyan]\n\n 0) [red]Quit \n")
	wtd = input(" Coose an action: ")
	print("")

	# choose logical
	if wtd == "1":
		distros()
	elif wtd == "2":
		print(f'Your system is {myos}')
		menu()
	elif wtd == "3":
		info()
		menu()
	elif wtd == "4":
		import os
		os.system('sh uninstall.sh')
	elif wtd == "0":
		print("")
	else:
		menu()

# distros 
def distros():
	import os
	print("\n [b cyan]1) [#DF5B2C]Ubuntu  [b cyan]2) [#2C67DF]Solus")
	print("\n [b cyan]3) [#2CDF6E]Manjaro [b cyan]4)[#2C50DF] Fedora[b cyan]\n\n 5)[white] Back    [b cyan] 0)[b red] Quit\n")
	dist = input("Choose your distro: ")
	# Install logic
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