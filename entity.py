class Entity(): #Entity class

	Instances = [] #Class array of all instances - each instance adds itself on __init__
	Index = 0 #Current highest index, counts total number of entities

	def __init__(self, position, sprite): #the class constructor, which takes an x and y value
		self.position = position #sets an instance's position to the given position tuple
		self.sprite = sprite #sets the instance's sprite to a given sprite
		
		self.index = type(self).Index #sets the current entity's index to the most recent entity's index +1
		type(self).Instances += [self]
		type(self).Index += 1 #adds one to the current index

	def move(self, vector): #a class function called move, that takes a vector

		self.position = ((self.position[0] + vector[0]), (self.position[1] + vector[1])) #modifies the player's position by the given vector

	def GetPosition(self, tileSize): #Returns the Pixel position of the Character

		return (self.position[0]*tileSize, self.position[1]*tileSize) #modifies each position by setting it to a tile sized grid
