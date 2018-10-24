import random
import datetime
from os import system, name

#clear console screen
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
		
def shoot(time):
	def display_time(time):
		quarter = 4 - int(time/720)
		return "Q" + str(quarter) + " " + str(datetime.timedelta(seconds=time%720))[2:]
	def select_shot():
		attempt = random.randint(0,100)
		if attempt <= 40:
			return 0
		elif attempt <= 80:
			return 2
		else:
			return 3
	points = select_shot()
	p_time = random.randint(3,24)
	if time - p_time < 0:
		p_time = time
	if points > 0:
		print(display_time(time - p_time) + "  Shot Made, +" + str(points) + "pts")
	else:
		print(display_time(time - p_time) + "  Shot Missed")
	return p_time, points
	
def create_away_team():
	team_names = ["Lakers","Trail Blazers","Celtics","76ers"]
	return team_names[random.randint(0, len(team_names) - 1)]
	
def announce_winner(home_score, home_team, away_score, away_team):
	winning_team = ''
	if home_score > away_score:
		winning_team = home_team
	else:
		winning_team = away_team
	print("The " + winning_team + " Win!")

#main game loop
def basketball_game():
	time = 2880
	possession = True
	h_score, a_score = 0, 0
	print("Wlecome to Python Basketball")
	h_team_name = str(input("Enter a team name: "))
	a_team_name = create_away_team()
	clear()
	while time > 0:
		p_time, p_score = shoot(time)
		time -= p_time
		if possession:
			h_score += p_score
			possession = False
		else:
			a_score += p_score
			possession = True
			
	print("[H] " + h_team_name + ": " + str(h_score) + " [A] " + a_team_name + ": "+ str(a_score))
	announce_winner(h_score, h_team_name, a_score, a_team_name)
	input("Press Enter To End")
		
#main call
basketball_game()