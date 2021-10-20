import os
import sys, time 
import platform
from tqdm import tqdm

# os.system('sh rem-test.sh')

for i in tqdm (range (100), desc="Uninstalling..."):
	time.sleep(0.01)
print("PIN3APPLE I3 config was uninstalled...")

os.system('sh uninstall.sh')
