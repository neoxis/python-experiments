from player import Player
import random

def create_random_player(position=None, star_rating=None):
	f_name = random_first_name()
	l_name = random_last_name()
	number = random_player_number()
	position = random_position(position)
	o_shooting, o_defense, i_shooting, i_defense = random_player_stats(star_rating)
	
	player = Player(f_name, l_name, number, position, o_shooting, i_shooting, o_defense, i_defense)
	print(player.get_info())
	
def random_first_name():
	first_names = ['Brad','Steve','James','Alexi','Mark','Thomas','Zack','Kyle']
	return first_names[random.randint(0, len(first_names) - 1)]
	
def random_last_name():
	last_names = ['Smith','Johnson','Williams','Brown','Jones','Miller','Davis','Garcia','Rodriguez','Wilson']
	return last_names[random.randint(0, len(last_names) - 1)]
	
def random_player_number():
	number = random.randint(0, 100)
	if number == 100:
		return '00'
	return str(number)
	
def random_position(position=None):
	positions = ['PG','SG','SF','PF','C']
	if position != None and int(position) > 0 and int(position) < 6:
		return positions[int(position) - 1]
	return positions[random.randint(0, 4)]
	
def random_player_stats(star_rating=None):
	def create_stat(rating):
		if rating == 0:
			return random.randint(10,15)
		elif rating == 1:
			return random.randint(15,20)
		elif rating == 2:
			return random.randint(20,25)
		elif rating == 3:
			return random.randint(25,30)
		else:
			return random.randint(30,35)
			
	rating = random.randint(0,4)
	if star_rating != None and int(star_rating) > 0 and int(star_rating) < 6:
		rating = int(star_rating)
	
	o_shooting = create_stat(rating)
	o_defense = create_stat(rating)
	i_shooting = create_stat(rating)
	i_defense = create_stat(rating)
	return o_shooting, o_defense, i_shooting, i_defense

	