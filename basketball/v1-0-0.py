import random
from os import system, name

#clear console screen
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
		
#main game loop
def basketball_game():
	while True:
		print("stuff")
		
basketball_game()