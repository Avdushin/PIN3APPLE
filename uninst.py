import os
import sys, time 
import platform
from tqdm import tqdm

for i in tqdm (range (100), desc="Uninstalling..."):
	time.sleep(0.01)
print("PIN3APPLE I3 config was uninstalled...")

os.system('sh uninstall.sh')
