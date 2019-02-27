from __init__ import *
from container import Container

class Tile():
	def __init__(self, symbol, position):
		self.symbol = symbol
		self.position = position
		self.Assign()

	def Assign(self):
		if self.symbol == '.':# FLOOR
			self.name = "floor"
			self.isPassable = True

		elif self.symbol == 'c':# CHEST
			self.name = "chest"
			self.container = Container(self.position)
			self.isPassable = False

		elif self.symbol == ',':# RANDOM DENSITY GRASS
			paths = ("grass_ld", "grass_md", "grass_hd")
			self.name = paths[random.randint(0, 2)]
			self.isPassable = True
	
		elif self.symbol == '1':# LOW DENSITY GRASS
			self.name = "grass_ld"
			self.isPassable = True

		elif self.symbol == '2':# MEDIUM DENSITY GRASS
			self.name = "grass_md"
			self.isPassable = True

		elif self.symbol == '3':# HIGH DENSITY GRASS
			self.name = "grass_hd"
			self.isPassable = True

		elif self.symbol == '=':# HIGH DENSITY GRASS
			self.name = "road"
			self.isPassable = True

		elif self.symbol == 'H':# ASCENDING LADDER
			self.name = "ladder"
			self.isPassable = True

		elif self.symbol == '<':# DESCENDING STAIRS
			self.name = "stairs_dsc"
			self.isPassable = True

		elif self.symbol == 'D':# DOOR
			self.name = "door"
			self.isPassable = True

		elif self.symbol == '#':# WALL
			self.name = "wall"
			self.isPassable = False

		else: # ERROR
			self.name = "error"
			self.isPassable = False

	def GetPosition(self, tileSize): #Returns the Pixel position of the tile
		return (self.position[0]*tileSize, self.position[1]*tileSize) #modifies each position by setting it to a tile sized grid
