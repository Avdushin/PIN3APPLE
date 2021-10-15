import sys
import pyfiglet
import platform
import os
#from tqdm import tqdm
from pyfiglet import figlet_format
from termcolor import colored

clear = os.system('clear')
#welcome = pyfiglet.print_figlet("PIN3APPLE-PY",'slant')
print((colored(figlet_format("PIN3APPLE"), color="yellow")))
# autor
author = colored("Author - https://github.com/Avdushin\n", 'green')
print(author)
# version
ver = colored("1.0")
version_output = colored(f"VERSION: {ver}\n", 'red')
print(version_output)
# os name
# os_name = platform.system()
# about_os = colored("Your system is " + os_name, "blue",)
# print(about_os)

# distro choose
distro = colored("Choose your distro...\n", 'yellow')
print(distro)

"""Distro choose"""

def choose_dist():

	print("1)Solus")
	print("2)Ubuntu")
	print("3)Manjaro")
	print("4)Fedora")
	print("5)Info")
	print("0)Exit")
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
	    os.system('sh nfo.sh')
	    choose_dist()
	elif comand == "0":
		ext = colored("Exit", 'red')
		print(ext)
	else:
  		choose_dist()

# start general function
choose_dist()