"""
PIN3APPLE - утилита для быстрой установки моей конфигурации I3wm
АВТОР - ANANAZ(https://github.com/Avdushin)
Программа поддерживается с 12 сентября, 2021
Avdushin - copyright 2021
"""
import pyfiglet, platform, time, os, sys
from tqdm import tqdm
from pyfiglet import figlet_format
from rich import print

os.system("clear")

# лого
pine = figlet_format("PIN3APPLE")
apple = figlet_format("UNINSTALLER")
print(f"[yellow]{pine}{apple}")
# панель прогресса
def progress():
	for i in tqdm (range (100), desc="Удаление..."):
		time.sleep(0.01)
	print("Конфигурация PIN3APPLE I3 бфла удалена...")
	print("[yellow b]Ваша сиситема будет [red b]перезагружена [yellow b]!")
	time.sleep(2)


def uninst_choose():
	print("\n  1) [b]Solus   2) Ubuntu\n")
	print("  3) [b]Manjaro 4) Fedora\n")
	print("  5) [yellow b]Мануал  [cyan b]7)[green b] Установка\n")
	print("  0) [red b]Выход\n")
	comand = input("Выберите ваш дистрибутив: ")

	if comand == "1":
		rmquest = input("Вы уверены что хотите удалить конфиг для Solus? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Solus/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Solus/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		else:
			pass
	
	if comand == "2":
		rmquest = input("Вы уверены что хотите удалить конфиг для Ubuntu? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Ubuntu/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Ubuntu/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		else:
			pass

	if comand == "3":
		rmquest = input("Вы уверены что хотите удалить конфиг для Manjaro? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Manjaro/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Manjaro/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		else:
			pass

	if comand == "4":
		rmquest = input("Вы уверены что хотите удалить конфиг для Fedora? [y/n]: ")
		if rmquest == "y":
			os.system('sh src/distros/Fedora/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		elif rmquest == "Y":
			os.system('sh src/distros/Fedora/uninst.sh')
			progress()
			print("[red b]!!! ПЕРЕЗАГРУЗКА !!!")
			os.system('reboot')
		else:
			pass
	
	elif comand == "5":
		print("\n[yellow b]Choose youre distro to [red b]REMOVE [yellow b]config... \n")
	elif comand == "7":
			os.system('python3 ./pineapple-ru.py')
	elif comand == "0":
		print("[red]Выход")
	else:
	  		uninst_choose()

# start general function
uninst_choose()