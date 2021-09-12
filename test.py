import os
import sys

# welcome logo
os.system('sh welcome.sh')

# distros = ['Ubuntu, Manjaro, Solus']

def lol():
	os.system('cat lol')
pass

distros_list = {
    1: 'ubuntu', 
    2: 'Manjaro', 
    3: 'Solus', 
    4: lol,
}

distro = int(input('Choose the os: (1)ubuntu (2)Manjaro (3)Solus: '))
print(distros_list[distro])



print("Your system is " + os.name )

