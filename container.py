from __init__ import *
class Container():
	
	def __init__(self, position): #the class constructor, which takes an x and y value
		self.contents = {}
		
	def AddItem(self, item):
		if self.contents[item]:
			self.contents[item] +=1
		else:
			self.contents[item] = 1
		
	def RemoveItem(self, item):
		if self.contents[item]:
			if self.contents[item] > 1:
				self.contents[item] -=1
			elif self.contents[item] <= 1:
				del self.contents[item]
