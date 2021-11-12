"""
PIN3APPLE - it's a little util to fast setup ANANAZZ I3 configuration.
AUTHOR - ANANAZ(https://github.com/Avdushin)
Program support from September 12, 2021
Avdushin - copyright 2021
"""
import pyfiglet, platform, time, os, sys
from tqdm import tqdm
from pyfiglet import figlet_format
from rich import print

ver = "[red b]3.0"

os.system("clear")

#logo 
pine = figlet_format("PIN3APPLE")
apple = figlet_format("UNINSTALLER")
print(f"[yellow]{pine}{apple}")
# progress bar
def progress():
	for i in tqdm (range (100), desc="Uninstalling..."):
		time.sleep(0.01)
	print("PIN3APPLE I3 config was uninstalled...")
	print("[yellow b]Your system will be [red b]reboot [yellow b]now!")
	time.sleep(2)


def uninst_choose():
	print("\n  1) [b]Solus   2) Ubuntu\n")
	print("  3) [b]Manjaro 4) Fedora\n")
	print("  5) [yellow b]Info    [cyan b]7)[green b] Install\n")
	print("  0) [red b]Exit\n")
	comand = input("Choose your distro: ")

	if comand == "1":
		rmquest = input("Are you sure you want to remove the Solus config? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Solus/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Solus/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass
	
	if comand == "2":
		rmquest = input("Are you sure you want to remove the Ubuntu config? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Ubuntu/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Ubuntu/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass

	if comand == "3":
		rmquest = input("Are you sure you want to remove the Manjaro config? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Manjaro/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Manjaro/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass

	if comand == "4":
		rmquest = input("Are you sure you want to remove the Fedora config? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Fedora/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Fedora/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass
	
	elif comand == "5":
		print("\n[yellow b]Choose youre distro to [red b]REMOVE [yellow b]config... \n")
	if comand == "4":
		rmquest = input("Are you sure you want to remove the Fedora config? [[red]y/n[/red]]: ")
		if rmquest == "y":
			os.system('sh src/distros/Fedora/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Fedora/uninst.sh')
			progress()
			print("[red b]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass
	elif comand == "7":
			os.system('python3 pineapple.py')
	elif comand == "0":
		print("[red]Exit")
	else:
	  		uninst_choose()

# start general function
uninst_choose()