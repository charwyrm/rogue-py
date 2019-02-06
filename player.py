import pygame as pg #imports PyGame with the alias pg
import os #imports OS specific commands, in our case allowing us to path to files no matter the OS

class Player(): #creates a player class
	sprite = pg.image.load(os.path.join("content", "player.bmp")) #gives it the variable sprite, which is set to player.bmp, an image in the content folder
	def __init__(self, x, y): #the class constructor, which takes an x and y value
		self.position = (x, y) #sets an instance's position to the given x and y values, which are placed within a tuple
	def move(self, vector): #a class function called move, that takes a vector
		self.position = (self.position[0] + vector[0], self.position[1] + vector[1]) #modifies the player's position by the given vector
