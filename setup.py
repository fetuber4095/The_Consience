#The Universal Consience
from os import system
from time import sleep as delay
from random import randint 

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
		Kernel()
	else:
		Kernel()


