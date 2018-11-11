class Player:
	def __init__(self, f_name, l_name, number, position, o_shooting, i_shooting, o_defense, i_defense):
		self.f_name = str(f_name)
		self.l_name = str(l_name)
		self.number = str(number)
		self.position = str(position)
		self.o_shooting = int(o_shooting)
		self.i_shooting = int(i_shooting)
		self.o_defense = int(o_defense)
		self.i_defense = int(i_defense)
	
	def get_first_name(self):
		return self.f_name
		
	def set_first_name(self, new_name):
		self.f_name = str(new_name)
		
	def get_last_name(self):
		return self.l_name
		
	def set_last_name(self, new_last):
		self.l_name = str(new_last)
		
	def get_number(self):
		return self.number
		
	def set_number(self, new_number):
		self.number = str(new_number)
		
	def get_position(self):
		return self.position
		
	def set_position(self, new_position):
		self.position = str(new_position).upper()
		
	def get_outside_shooting(self):
		return self.o_shooting
		
	def set_outside_shooting(self, new_outside_shooting):
		self.o_shooting = int(new_outside_shooting)
		
	def get_outside_defense(self):
		return self.o_defense
		
	def set_outside_defense(self, new_outside_defense):
		self.o_defense = int(new_outside_defense)
		
	def get_inside_shooting(self):
		return self.i_shooting
		
	def set_inside_shooting(self, new_inside_shooting):
		self.i_shooting = int(new_inside_shooting)
		
	def get_inside_defense(self):
		return self.i_defense
		
	def set_inside_defense(self, new_inside_defense):
		self.i_defense = int(new_inside_defense)
		
	def get_box_score_name(self):
		return self.f_name[:1] + ". " + self.l_name
		
	def get_info(self):
		stats = self.f_name + " " + self.l_name + " " + self.number + " " + self.position
		stats += "\n OFF:\t\tDEF:"
		stats += "\n 3sht: " + str(self.o_shooting) + "\tpDef: " + str(self.o_defense)
		stats += "\n 2sht: " + str(self.i_shooting) + "\tiDef: " + str(self.i_defense)
		return stats
		