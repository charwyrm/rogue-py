from __init__ import *
class Camera():
	def __init__(self, width, height):
		self.camera = pg.Rect(0, 0, width, height)
		self.width = width
		self.height = height

	def Apply(self, entity):
		return entity.rect.move(self.camera.topleft)

	def Update(self, target):
		
		x = -target.rect.x + int(WIDTH / 2)
		y = -target.rect.y + int(HEIGHT / 2)

		#limit scrolling to map size
		x = min(0, x)  # left
		y = min(0, y)  # top
		x = max(-(self.width - WIDTH), x)  # right
		y = max(-(self.height - HEIGHT), y)  # bottom
		self.camera = pg.Rect(x, y, self.width, self.height)

		

###PARTS OF WHAT CAMERA IS MADE OF###
#-What should camera do?-
#>Follow the player, keeping them central EXCEPT when the camera would otherwise display outside of the boundaries
#>>To do this, we need to give an offset from the player's position, which needs to be multiplied by TILESIZE, and then returned
#
#
#
#
#
#
