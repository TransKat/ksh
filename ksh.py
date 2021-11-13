# Kat's Shell

import os

# init variables
username = os.getenv('username') # get the windows username
pcname = os.environ['COMPUTERNAME'] # get the windows pc name
version = "0.5.1"

# print welcome text and start the loop
clear = lambda: os.system('cls')
clear()
print(f"Welcome to ksh verison {version}\n\n")
while True:
    sinput = input(f"[{username} ~ {pcname}] ")
    os.system(sinput)
    if sinput == "exit":
        print("\n * 150")
        clear()
        exit()
    elif sinput == "clear":
        print("\n * 150")
        clear()
