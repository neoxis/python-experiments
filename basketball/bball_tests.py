import player
import util
import unittest
# RUN USING: python bball_test.py -v

# ############ #
# Player Tests #
# ############ #
class PlayerTests(unittest.TestCase):
	pg = player.Player("Alexi", "Cameron", 3, "SG", 11, 14, 12, 12)
	
	def test_get_set_first_name(self):
		self.assertEqual(self.pg.get_first_name(), "Alexi")
		test_name = "Brad"
		self.pg.set_first_name(test_name)
		self.assertEqual(test_name, self.pg.get_first_name())
		
	def test_get_set_last_name(self):
		self.assertEqual(self.pg.get_last_name(), "Cameron")
		test_name = "Stiff"
		self.pg.set_last_name(test_name)
		self.assertEqual(test_name, self.pg.get_last_name())
		
	def test_get_set_number(self):
		self.assertEqual(self.pg.get_number(), "3")
		test_number = "7"
		self.pg.set_number(test_number)
		self.assertEqual(test_number, self.pg.get_number())
		
	def test_get_set_position(self):
		self.assertEqual(self.pg.get_position(), "SG")
		test_position = "PG"
		self.pg.set_position(test_position)
		self.assertEqual(test_position, self.pg.get_position())
		
	def test_get_set_outside_shooting(self):
		self.assertEqual(self.pg.get_outside_shooting(), 11)
		test_value = 13
		self.pg.set_outside_shooting(test_value)
		self.assertEqual(test_value, self.pg.get_outside_shooting())
		
	def test_get_set_outside_defense(self):
		self.assertEqual(self.pg.get_outside_defense(), 12)
		test_value = 13
		self.pg.set_outside_defense(test_value)
		self.assertEqual(test_value, self.pg.get_outside_defense())
		
	def test_get_set_inside_shooting(self):
		self.assertEqual(self.pg.get_inside_shooting(), 14)
		test_value = 13
		self.pg.set_inside_shooting(test_value)
		self.assertEqual(test_value, self.pg.get_inside_shooting())
		
	def test_get_set_inside_defense(self):
		self.assertEqual(self.pg.get_inside_defense(), 12)
		test_value = 13
		self.pg.set_inside_defense(test_value)
		self.assertEqual(test_value, self.pg.get_inside_defense())
		
class UtilTests(unittest.TestCase):
	def test_random_position(self):
		self.assertEqual(util.random_position(1), "PG")
	
if __name__ == '__main__':
	unittest.main()