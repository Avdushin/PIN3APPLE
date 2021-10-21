import pyfiglet, platform, time, os, sys
from tqdm import tqdm
from pyfiglet import figlet_format
from termcolor import colored
from printy import printy

ver = "[rB]1.2.0"

os.system("clear")
print((colored(figlet_format("PIN3APPLE"), color="yellow")))
print((colored(figlet_format("UNINSTALLER"), color="red")))
# printy("\n[yB]PINEAPPLE\n@[rB]UNINSTALL\n")
# printy(ver+"\n")

# progress bar
def progress():
	for i in tqdm (range (100), desc="Uninstalling..."):
		time.sleep(0.01)
	print("PIN3APPLE I3 config was uninstalled...")
	printy("[yB]Your system will be@ [rB]reboot@ [yB]now!")
	time.sleep(2)


def uninst_choose():
	print("1)Solus")
	print("2)Ubuntu")
	print("3)Manjaro")
	print("4)Fedora")
	print("5)Info")
	print("7)Install")
	print("0)Exit")
	comand = input("Choose your distro: ")

	if comand == "1":
		rmquest = input("Are you sure you want to remove the Solus config? [y/n]: ")
		if rmquest == "y":
			os.system('sh Solus/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh Solus/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass
	
	if comand == "2":
		rmquest = input("Are you sure you want to remove the Ubuntu config? [y/n]: ")
		if rmquest == "y":
			os.system('sh Ubuntu/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh Ubuntu/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass

	if comand == "3":
		rmquest = input("Are you sure you want to remove the Manjaro config? [y/n]: ")
		if rmquest == "y":
			os.system('sh Manjaro/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh Manjaro/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass

	if comand == "4":
		rmquest = input("Are you sure you want to remove the Fedora config? [y/n]: ")
		if rmquest == "y":
			os.system('sh Fedora/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh Fedora/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass
	
	elif comand == "5":
		printy("\n[B]Choose youre distro to@ [rB]remove@ [yB]config... \n")
		uninst_choose()
	if comand == "4":
		rmquest = input("Are you sure you want to remove the Fedora config? [y/n]: ")
		if rmquest == "y":
			os.system('sh Fedora/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh Fedora/uninst.sh')
			progress()
			printy("[rB]!!!Reboot!!!")
			os.system('reboot')
		else:
			pass

	elif comand == "7":
			os.system('python3 pineapple.py')
	else:
	  		uninst_choose()

# start general function
uninst_choose()