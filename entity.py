from __init__ import *
class Entity(pg.sprite.Sprite): #Entity class
	def __init__(self, position, sprite): #the class constructor, which takes an x and y value
		pg.sprite.Sprite.__init__(self)

		self.position = position #sets an instance's position to the given position tuple
		self.image = pg.Surface((TILESIZE, TILESIZE))
		self.image.blit(sprite, (0, 0))
		self.rect = self.image.get_rect()

	def Move(self, vector): #a class function called move, that takes a vector
		self.image.rect.move(vector)

	def GetPosition(self): #Returns the Pixel position of the Character
		return (self.position[0]*TILESIZE, self.position[1]*TILESIZE)
