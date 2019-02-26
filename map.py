from __init__ import *
from tile import Tile

class Map:
	def __init__(self, mapData):
		self.Update(mapData)

	def Update(self, mapData):
		lineArray = []
		returnArray = []
		x = 0
		y = 0
		for line in mapData:
			for char in line:
				lineArray.append(Tile(char, (x, y)))
				x += 1
			returnArray.append(lineArray)
			lineArray = []
			x = 0
			y += 1
		self.tileMap = returnArray