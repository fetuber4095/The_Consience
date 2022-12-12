#The Universal Consience
from os import system
from time import sleep 
from random import randint 
from getpass import getpass

__version__ = ["snaphot a12w49", "IAS [SETUPED]", "fetuber4095"]
pwd = r"E:\TC"


def clear():
	system("cls")
	pass

class Kernel:
	def __init__(self):
		input("COMMING SOON. . .")

if __name__ == '__main__':
	clear()
	try:
		login = open(fr"{pwd}\LOGIN", "rt")
		login.close()
	except FileNotFoundError:
		login = open(fr"{pwd}\LOGIN", "wt+")
		print("Hello, Welcome to the UNIVERSAL CONSIENCE CONSOLE")
		print("To continue you need create an username to log at Server\n\n")
		username = input("login: ").strip()
		password = getpass("password: ").strip()
		print("\n\nNow you are registred!")
		print("The Universal Console is a Protected Software, you need be authorized to acess")
		print("If you have a special Key please insert here. Else press ENTER!")
		entered_key = input("KEY: ")
		if entered_key == __version__[2]:
			entered_key = True
			print(f"{username}, your account have permission to acess the SECRET SERVER"), sleep(5)
		else:
			entered_key = False
			print(f"Oh {username}, You arent a PERMITTED USER!!!"), sleep(5)

		login.write(f"{username} {password} {entered_key}")
		login.close()
		Kernel()
	else:
		login = open(fr"{pwd}\LOGIN", "rt")
		login = login.split()
		print(f"USER:{login[0]} PASSWORD: {login[1]} TIPO DE ACCOUNT")
		print(f"Hello {login[0]}, please insert your password to continue.")
		try_passed = getpass("password: ").strip()
		if try_passed == login[1]:
			Kernel()
		else:
			print("Sorry, but this isnt the password to {login[1]}")


