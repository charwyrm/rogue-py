from __init__ import *
from tile import Tile
from entity import Entity
from container import Container

class TileMap:
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
	def Shade(self):
		xpos, ypos = 0, 0
		for y in self.tileMap:
			for x in y:
				if x.name == "wall":
					if self.tileMap[ypos+1][xpos].isPassable:
						x.name = "wallside"
				xpos+=1
			xpos=0
			ypos+=1
		
