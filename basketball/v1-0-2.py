import random
import datetime
from os import system, name
import shutil

#clear console screen
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
		
def shoot(time, quarter_info, possession):
	def display_time(time):
		return str(datetime.timedelta(seconds=time%720))[2:]
	def select_shot():
		attempt = random.randint(0,100)
		if attempt <= 40:
			return 0
		elif attempt <= 80:
			return 2
		else:
			return 3
	points = select_shot()
	p_time = random.randint(4,24)
	if time - p_time < 0:
		p_time = time
	if points > 0:
		msg = display_time(time - p_time) + "  Shot Made, +" + str(points) + "pts"
		if possession:
			msg += " h"
		else: msg += " a"
		quarter_info[(4 - int((time-p_time)/720)) - 1].append(msg)
	return p_time, points
	
def create_away_team():
	team_names = ["Lakers","Trail Blazers","Celtics","76ers","Clippers","Rockets","Warriors"]
	return team_names[random.randint(0, len(team_names) - 1)]
	
def announce_winner(home_score, home_team, away_score, away_team):
	winning_team = ''
	if home_score > away_score:
		winning_team = home_team
	else:
		winning_team = away_team
	print("The " + winning_team + " Win!")

def display_quarter(quarter_info):
	for x in quarter_info:
		if x.endswith("h"):
			print(x[:-2])
		else:
			sp = ' ' * 37
			print(sp + x[:-2])

def display_header(h_team_name, h_score, a_team_name, a_score, quarter, quarter_info):
	h_q_points, a_q_points = points_in_quarter(quarter_info)
	d_title = h_team_name + " " + str(h_q_points) + " [" + str(h_score) + "]   "
	if len(d_title) < 29:
		sp = ' ' * (29-len(d_title))
		d_title = sp + d_title
	d_title += "Q" + str(quarter) + "   "
	d_title += "[" + str(a_score) + "] " + str(a_q_points) + " " + a_team_name
	print(d_title)

def points_in_quarter(quarter_info):
	h_points, a_points = 0, 0
	for x in quarter_info:
		if x.endswith("a"):
			a_points += int(x[19])
		else:
			h_points += int(x[19])
	return h_points, a_points
		
def display_quarter_totals(quarter_info):
	cols = shutil.get_terminal_size().columns
	qtr_str = " Q1 + Q2 + Q3 + Q4 + TOTAL"
	home_str, away_str = '',''
	h_f_score, a_f_score = 0,0
	for x in quarter_info:
		h,a = points_in_quarter(x)
		home_str += " " + str(h) + " |"
		h_f_score += h
		away_str += " " + str(a) + " |"
		a_f_score += a
	home_str += "  " + str(h_f_score)
	away_str += "  " + str(a_f_score)
	print(home_str.center(cols))
	print(qtr_str.center(cols))
	print(away_str.center(cols))

def play_again():
	answer = input("Play Again? [Y]es or [N]o\n").lower()
	return (answer == 'yes' or answer == 'y') 

def get_home_team():
	temp = str(input("Enter a team name: "))
	if len(temp) > 17:
		temp = temp[:14] + "..."
	return temp

#main game loop
def basketball_game():
	time = 2880
	q_info = [[],[],[],[]]
	possession = True
	h_score, a_score = 0, 0
	print("Welcome to Python Basketball")
	h_team_name = get_home_team()
	a_team_name = create_away_team()
	clear()
	while time > 0:
		p_time, p_score = shoot(time, q_info, possession)
		time -= p_time
		if possession:
			h_score += p_score
			possession = False
		else:
			a_score += p_score
			possession = True
	
	display_quarter_totals(q_info)
	title = "[H] " + h_team_name + ": " + str(h_score) + " [A] " + a_team_name + ": "+ str(a_score)
	print(title)
	announce_winner(h_score, h_team_name, a_score, a_team_name)
	user_input = '-1'
	while user_input != '':
		user_input = input("Enter Quarter #, or press Enter to quit\n")
		if user_input == '':
			break
		if int(user_input) > 0 and int(user_input) < 5:	
			clear()
			display_quarter_totals(q_info)
			display_header(h_team_name,h_score,a_team_name,a_score,user_input,q_info[int(user_input) - 1])
			print('-'*shutil.get_terminal_size().columns)
			display_quarter(q_info[int(user_input) - 1])
		
width = "60"
height = "45"
system("title Python Basketball")
system("mode con cols="+ width +" lines="+ height)

playing = True
while playing:
	basketball_game()
	playing = play_again()
	clear()