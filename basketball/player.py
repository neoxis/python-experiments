class Player:
	def __init__(self, f_name, l_name, number, position, o_shooting, i_shooting, o_defense, i_defense):
		self.f_name = f_name
		self.l_name = l_name
		self.number = str(number)
		self.position = position
		self.o_shooting = o_shooting
		self.i_shooting = i_shooting
		self.o_defense = o_defense
		self.i_defense = i_defense
	
	def get_first_name(self):
		return self.f_name
		
	def get_last_name(self):
		return self.l_name
		
	def get_box_score_name(self):
		return self.f_name[:1] + ". " + self.l_name
		
	def get_number(self)
		return self.number
		
	def get_info(self):
		stats = self.f_name + " " + self.l_name + " " + self.number + " " + self.position
		stats += "\n OFF:\t\tDEF:"
		stats += "\n 3sht: " + str(self.o_shooting) + "\tpDef: " + str(self.o_defense)
		stats += "\n 2sht: " + str(self.i_shooting) + "\tiDef: " + str(self.i_defense)
		return stats
		
pg = Player("Alexi", "Cameron", 3, "SG", 11, 14, 12, 12)

print(pg.get_info())
print(pg.get_box_score_name())
input()