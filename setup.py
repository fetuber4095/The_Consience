#The Universal Consience
from os import system
from time import sleep as delay
from random import randint 
from getpass import getpass

__version__ = ["alpha 1.0", "Kernel Implemetation"]



def clear():
	system("clear")
	pass

class Kernel:
	def __init__(self):
		input("COMMING SOON. . .")

if __name__ == '__main__':
	try:
		login = open("LOGIN")
		login.close()
	except FileNotFoundError:
		login = open("LOGIN", "wt+")
		print("Hello, Welcome to the UNIVERSAL CONSIENCE CONSOLE")
		print("To continue you need create an username to log at Server\n\n")
		username = input("login: ").split()
		password = getpass("password: ").split()
		print("\n\nNow you are registred!")
		print("The Universal Console is a Protected Software, you need be authorized to acess")
		print("If you have a special Key please insert here. Else press ENTER!")
		entered_key = input("KEY: ")
		if entered_key == __version__[2]:
			entered_key = True
			print(f"{username}, your account have permission to acess the SECRET SERVER"), sleep(5)
		else:
			entered_key = False
			clear()
			print(f"Oh {username}, You arent a PERMITTED USER!!!"), sleep(5)

		login.write(f"{username} {password} {entered_key}")
		login.close()
		Kernel()
	else:
		Kernel()


