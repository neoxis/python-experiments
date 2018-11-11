import player
import util
import unittest
# RUN USING: python bball_test.py -v

# ############ #
# Player Tests #
# ############ #
class PlayerTests(unittest.TestCase):
	pg = player.Player("Alexi", "Cameron", 3, "SG", 11, 14, 12, 12)
	
	def test_get_first_name(self):
		self.assertEqual(self.pg.get_first_name(), "Alexi")
		
	def test_set_first_name(self):
		test_name = "Brad"
		self.pg.set_first_name(test_name)
		self.assertEqual(test_name, self.pg.get_first_name())

class UtilTests(unittest.TestCase):
	def test_random_position(self):
		self.assertEqual(util.random_position(1), "PG")
	
if __name__ == '__main__':
	unittest.main()
#pg = player.Player("Alexi", "Cameron", 3, "SG", 11, 14, 12, 12)
'''
print(pg.get_info())

# get tests
print(pg.get_first_name())
print(pg.get_last_name())
print(pg.get_number())
print(pg.get_position())

print(pg.get_outside_shooting())
print(pg.get_outside_defense())
print(pg.get_inside_shooting())
print(pg.get_inside_defense())

# set tests
pg.set_first_name("Brad")
pg.set_last_name("Stiff")
pg.set_number(7)
pg.set_position("pg")

pg.set_outside_shooting(13)
pg.set_outside_defense(13)
pg.set_inside_shooting(13)
pg.set_inside_defense(13)

print(pg.get_info())

util.create_random_player()

input("Press Enter to quit")
'''
