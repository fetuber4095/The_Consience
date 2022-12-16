#The Universal Consience
from os import system
from time import sleep 
from random import randint 
from getpass import getpass


import socket


tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)


__version__ = ["snapshot 22w16irf", "Extructure IMPLEMETEND - PART III", "FeTuber4095"]
pwd = r"E:\TC"


def prompt(text, player):
	while True:
		x = input(rf"{text}[S/N] ").strip()
		if x == "s" or x == "S":
			return True
			break
		elif x == "n" or x == "N":
			return False
			break
		else:
			continue
 	

def update(current_version):
	x = current_version
	if x == __version__[0]:
		system("git fetch")
		system("git pull")
	else: 
		print("Please acess the github repository and UPDATE your system mannualy.")
		input("https://github.com/fetuber4095/The_Consience")
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
		print(f"\033[31mUniversal Consience Console \033[39m[\033[35m{__version__[0]} \033[39m- \033[35m{__version__[1]}\033[39m]")
		print(f"\033[31mCONNECTED: \033[32m{self.player}@{IPAddr} \033[39m- \033[34mhttps://github.com/fetuber4095/The_Consience")
		print(f"")
		while True:
			try:
				cmd = str(input(f"\033[32m{self.player}\033[31m@\033[36m{hostname}\033[37m:~$ ")).strip()
				# A
				if cmd.startswith("atrribute"):
					print("Comming Soon...")
				elif cmd.startswith("asset"):
					print("Comming Soon...")	
				elif cmd.startswith("attemp"):
					print("Comming Soon...")
				elif cmd.startswith("ask"):
					cmd = cmd.replace("ask", "")
					cmd = cmd.replace("ask ", "")
					sla = prompt(cmd, self.player)
				elif cmd.startswith("acess"):
					print("Comming Soon...")
				elif cmd == "architure":
					print("Comming Soon...")
				elif cmd.startswith("av"):
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

				# B
				elif cmd == "break":
					print("Comming Soon...")
				elif cmd.startswith("bridge"):
					print("Comming Soon...")
				elif cmd == "build":
					print("Comming Soon...")
				
				# C
				elif cmd.startswith("cd"):
					print("Comming Soon...")
				elif cmd.startswith("clone"):
					print("Comming Soon...")
				elif cmd == "clear":
					clear()
					continue
				elif cmd.startswith("create"):
					print("Comming Soon...")

				# D
				elif cmd.startswith("disk"):
					print("Comming Soon...")
				elif cmd.startswith("done"):
					print("Comming Soon...")
				elif cmd.startswith("driver"):
					print("Comming Soon...")
				elif cmd.startswith("delete"):
					print("Comming Soon...")

				# E
				elif cmd == "exit":
					print("Closing programs. . ."), sleep(randint(1, 5))
					print("Exiting. . ."), sleep(randint(1, 3))
					break
				elif cmd.startswith("echo"):
					print("Comming Soon...")
				elif cmd.startswith("erro"):
					print("Comming Soon...")
				elif cmd.startswith("end"):
					print("Comming Soon...")
				elif cmd.startswith("else"):
					print("Comming Soon...")
				elif cmd.startswith("engine"):
					print("Comming Soon...")
				elif cmd.startswith("envirroment"):
					print("Comming Soon...")

				# F
				# G
				# H
				# I
				# J
				# K
				# L
				elif cmd.startswith("lagg"):
					cmd = cmd.replace("lagg ", "")
					cmd = cmd.replace("lagg", "")
					if cmd == "install":
						print("To install LAGG you need to give permission to the Console")
						x = getpass(f"password for {self.player}: ")
						if x = self.password
				# M
				# N 
				# O
				# P
				# Q
				# R
				# S
				# T
				# U
				# V
				# W
				# X
				# Y
				# Z






				elif cmd == "":
					print("")
					continue	
				else:
					cmd = cmd.split()
					print(f"{cmd[0]}: Unknow Command!")
			except Exception as Erro:
				system(f"msg * {Erro}: It can be an error of code, you can report in the GitHub\nhttps://github.com/fetuber4095/The_Consience")	
if __name__ == '__main__':
	clear()
	update(__version__[0])
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



