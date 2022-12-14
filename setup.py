#The Universal Consience
from os import system
from time import sleep 
from random import randint 
from getpass import getpass


import socket


tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)


__version__ = ["snapshot r23w23", "Extructure IMPLEMETEND - PART I", "fetuber4095"]
pwd = r"E:\TC"


def prompt(text, player):
	print(f"{text}")
	while True:
		x = input("[S/N] ").strip()
		if x == "s" or x == "S":
			result = True
			break
		elif x == "n" or x == "N"
			result = False
			break
		else:
			continue
 	return result



def clear():
	system("cls")
	pass

class Kernel:
	def __init__(self):
		settings = open("settings.dat", "rt").read()
		settings = settings.split()
		self.player = settings[0]
		self.password = settings[1]
		self.peraccount = settings[2]
		self.serial = settings[3]
		clear()
		print(f"Universal Consience Console [{__version__[0]} - {__version__[1]}]")
		print(f"CONNECTED: {self.player}@{IPAddr} - https://github.com/fetuber4095/The_Consience")
		print(f"")
		while True:
			try:
				cmd = str(input(f"{self.player}@{hostname}: ")).strip()
				if cmd.startswith("atrribute"):
					print("Comming Soon...")

				elif cmd.startswith("asset"):
					print("Comming Soon...")
				elif cmd.startswith("attemp"):
					print("Comming Soon...")
				elif cmd.startswith("ask"):
					cmd = cmd.replace("ask", "")
					cmd = cmd.replace("ask ", "")
					if cmd == "":
						while True:
							x = input("[S/N] ").strip()
							if x == "s" or x == "S":
								result = True
								break
							elif x == "n" or x == "N"
								result = False
								break
							else: 
								continue
					else:
						sla = prompt(cmd, self.player):
						del sla

				elif cmd.startswith("acess"):
					print("Comming Soon...")

				elif cmd == "architure":

				elif cmd.startswith("am"):
					print("Comming Soon...")

				elif cmd.startswith("akward"):
					print("Comming Soon...")

				elif cmd.startswith("again"):
					print("Comming Soon...")

				elif cmd.startswith("about"):
					print("Comming Soon...")

				elif cmd.startswith("assing"):
					print("Comming Soon...")

				elif cmd.startswith("alias"):
					print("Comming Soon...")

				elif cmd.startswith("alchemy"):
					print("Comming Soon...")





				elif cmd == "exit":
					print("Closing programs. . ."), sleep(randint(1, 5))
					print("Exiting. . ."), sleep(randint(1, 3))
					break
				

				elif cmd == "":
					print("")
					continue	
				else:
					cmd = cmd.split()
					print(f"{cmd[0]}: Unknow Command!")
			except Exception as Erro:
				print(f"{Erro}, It can be an error of code, you can report in the GitHub")	
if __name__ == '__main__':
	clear()
	try:
		login = open(fr"settings.dat", "rt")
		login.close()
	except FileNotFoundError:
		login = open(fr"settings.dat", "wt+")
		print("Hello, Welcome to the UNIVERSAL CONSIENCE CONSOLE")
		print("To continue you need create an username to log at Server")
		print("========================================================")
		username = input("login: ").strip()
		password = getpass("password: ").strip()
		serial = randint(10000000000, 9999999999999999)
		print("\n\nNow you are registred!")
		print("========================================================")
		print("The Universal Console is a Protected Software, you need be authorized to acess")
		print("If you have a special Key please insert here. Else press ENTER!")
		entered_key = getpass("key: ").strip()
		if entered_key == __version__[2]:
			entered_key = True
			print(f"{username}, your account have permission to acess the SECRET SERVER"), sleep(3)
		else:
			entered_key = False
			print(f"Oh {username}, You arent a PERMITTED USER!!!"), sleep(3)

		login.write(f"{username} {password} {entered_key} {serial}")
		login.close()
		Kernel()
	else:
		login = open(fr"settings.dat", "rt").read()
		login = login.split()
		clear()
		try_passed = getpass(f"password for {login[0]}: ").strip()
		if try_passed == login[1]:
			del login
			Kernel()
		else:
			print(f"Sorry, but this isnt the password to {login[1]}")
			print("The program will be closed, if you forgot you password type {reset}"), sleep(3)



