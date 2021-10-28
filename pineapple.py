"""
PIN3APPLE - it's a little util to fast setup ANANAZZ I3 configuration.
AUTHOR - ANANAZ(https://github.com/Avdushin)
Program support from September 12, 2021
Avdushin - copyright 2021
"""
import sys
import pyfiglet
import platform
import os
from rich import print
from pyfiglet import figlet_format

# clear console
clear = os.system('clear')
# print logo
prname = figlet_format("PIN3APPLE")
print(f"[yellow]{prname}")

# autor
print("[green]Author - https://github.com/Avdushin\n")

# version 
ver = ("[red]1.3.5")
# print version
print(f"[red]VERSION: {ver}\n")

# distro choose
print("[yellow]Choose your distro...")

"""Distro choose function"""

def choose_dist():
	print("\n1) Solus   2) Ubuntu")
	print("3) Manjaro 4) Fedora")
	print("5) Info    9) Uninstall")
	print("0) Exit\n")
	comand = input("Choose an action: ")
	if comand == "1":
	    os.system('sh Solus/solus.sh')
	elif comand == "2":
		os.system('sh Ubuntu/ubuntu.sh')
	elif comand == "3":
	    os.system('sh Manjaro/manjaro.sh')
	elif comand == "4":
	    os.system('sh Fedora/fedora.sh')
	elif comand == "5":
	    print("\n[yellow b]HOW IT WORKS?\nCHOOSE YOUR DISTRO, WAIT SOME MINUTES AND RELAX!\n\n[white]INSTRUCTION:\n[#46C959][[#CE270B]RUS[/#CE270B]][/#46C959] - [green]https://telegra.ph/PN3APPLE-RUS-INFO-10-23\n[#46C959][[#CE270B]ENG[/#CE270B]][/#46C959] - [green]https://telegra.ph/PN3APPLE-ENG-INFO-10-23\n")
	    choose_dist()
	elif comand == "9":
		os.system('sh uninstall.sh')
	elif comand == "0":
		print("[red]Exit")
	else:
  		choose_dist()

# start general function
choose_dist()