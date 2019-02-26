from __init__ import *

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
			self.isPassable = False

		elif self.symbol == 'g':# LOW DENSITY GRASS
			self.name = "grass_ld"
			self.isPassable = True

		elif self.symbol == 'G':# MEDIUM DENSITY GRASS
			self.name = "grass_md"
			self.isPassable = True

		elif self.symbol == '6':# HIGH DENSITY GRASS
			self.name = "grass_hd"
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

		elif self.symbol == '#':# FLOOR
			self.name = "wall"
			self.isPassable = False

		else: # ERROR
			self.name = "error"
			self.isPassable = False

	def GetPosition(self, tileSize, tileOffset): #Returns the Pixel position of the tile
		return ((self.position[0]*tileSize)+tileOffset, (self.position[1]*tileSize)+tileOffset) #modifies each position by setting it to a tile sized grid, and adding an offset