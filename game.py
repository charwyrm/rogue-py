from __init__ import *
from map import Map
from camera import Camera
from entity import Entity

class Game():
	def __init__(self, mapData):
		
		self.window = pg.display.set_mode((WIDTH, HEIGHT))#, pg.NOwindow)
		
		for i in SPR:
			SPR[i] = pg.transform.scale(SPR[i], (TILESIZE, TILESIZE))
			SPR[i] = SPR[i].convert_alpha()

		self.clock = pg.time.Clock() #creates a clock object, which can be used to interact with the FPS
		self.keyDelay = 0 #keystrokes are registered straight away from loading up the game
		
		self.player = Entity((0, 0), SPR["player"])
		self.map = Map(mapData) #creates an instance of map using the current map Data
		self.camera = Camera(self.map.width, self.map.height)
		self.pressedUp, self.pressedDown, self.pressedLeft, self.pressedRight = False, False, False, False
		
	def Run(self):
		print(len(self.map.Data))
		while True:
			self.CheckInput() #checks for keys that are pressed or released and sets values accordingly
			self.ProcessInput() #acts upon the pressed keys' values
			print(self.player.position)
			self.window.fill(CLR["black"],self.camera.camera)
			#self.DrawEntityMap()
			self.clock.tick(60) #limit the game to 60 windows per second
			pg.display.set_caption("DungeonSK - {}fps".format(round(self.clock.get_fps())))
			self.DrawData()
			self.camera.Update(self.player)
			pg.display.flip() #update window

	def CheckInput(self):
		for event in pg.event.get(): #for every event in the event queue
			if event.type == pg.QUIT: #if it's the window being exited (hitting the red x)
				pg.quit() #stop pygame
				sys.exit() #exit the window

			elif event.type == pg.KEYDOWN: #otherwise, if it's the rising edge of a keypress (the instant a keystroke happens, not the key being held down)
				if event.key == pg.K_w: #if said key is w
					self.pressedUp = True #Move the player up
				elif event.key == pg.K_s: #otherwise, if said key is s
					self.pressedDown = True #Move the player down
				elif event.key == pg.K_a: #otherwise, if said key is a
					self.pressedLeft = True #Move the player left
				elif event.key == pg.K_d: #otherwise, if said key is d
					self.pressedRight = True #Move the player right
				elif event.key == pg.K_ESCAPE:
					self.quit()
					sys.exit()

			elif event.type == pg.KEYUP: #otherwise, if it's the falling edge of a keypress (when a key is released)
				if event.key == pg.K_w: #if said key is w
					self.pressedUp = False #Move the player up
				elif event.key == pg.K_s: #otherwise, if said key is s
					self.pressedDown = False #Move the player down
				elif event.key == pg.K_a: #otherwise, if said key is a
					self.pressedLeft = False #Move the player left
				elif event.key == pg.K_d: #otherwise, if said key is d
					self.pressedRight = False #Move the player right

	def ProcessInput(self):
		p = self.player.position #just a temporary variable to stop the code from being too verbose
		self.keyDelay -= self.clock.get_time() #decreases the delay by the milliseconds since the last window

		if self.keyDelay <= 0: #if the delay is over
			
			if self.pressedUp and self.pressedLeft: #if up is pressed
				if 0 <= p[1] - 1 and 0 <= p[0] - 1: #if the space above is within bounds and
					if self.map.Data[p[1] - 1][p[0] - 1].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((-1, -1)) #Move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedUp and self.pressedRight: #if up is pressed
				if 0 <= p[1] - 1 and len(self.map.Data[1]) > p[0] + 1: #if the space above is within bounds and
					if self.map.Data[p[1] - 1][p[0] + 1].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((1, -1)) #Move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedDown and self.pressedLeft: #if up is pressed
				if  len(self.map.Data) - 1 >= p[1] + 1 and 0 <= p[0] - 1: #if the space below is within bounds and
					if self.map.Data[p[1] + 1][p[0] - 1].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((-1, 1)) #Move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedDown and self.pressedRight: #if up is pressed
				if len(self.map.Data) - 1 >= p[1] + 1 and len(self.map.Data[1]) > p[0] + 1: #if the space below is within bounds and
					if self.map.Data[p[1] + 1][p[0] + 1].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((1, 1)) #Move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedUp: #if up is pressed
				if 0 <= p[1] - 1: #if the space above is within bounds and
					if self.map.Data[p[1] - 1][p[0]].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((0, -1)) #Move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds

			elif self.pressedDown: #if down is pressed
				if len(self.map.Data) > p[1] + 1: #if the space below is within bounds and
					if self.map.Data[p[1] + 1][p[0]].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((0, 1)) #Move the player down
						self.keyDelay = 180 #reset the delay to 200 milliseconds

			elif self.pressedLeft: #if left is pressed
				if 0 <= p[0] - 1: #if the space to the left is within bounds and
					if self.map.Data[p[1]][p[0] - 1].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((-1, 0)) #Move the player left
						self.keyDelay = 180 #reset the delay to 200 milliseconds

			elif self.pressedRight: #if right is pressed
				if len(self.map.Data[1]) > p[0] + 1: #if the space to the right is within bounds and
					if self.map.Data[p[1]][p[0] + 1].isPassable: #if the Move is into something passable (without collision)
						self.player.Move((1, 0)) #Move the player right
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
	
		# return ((max(self.player.position[1] - 1 - math.ceil(TILESHIGH / 2), 0),
		# min(self.player.position[1] + 1 + math.ceil(TILESHIGH / 2), len(self.map.Data))),
		# (max(self.player.position[0] - 1 - math.ceil(TILESWIDE / 2), 0), 
		# min(self.player.position[0] + 1 + math.ceil(TILESWIDE / 2), len(self.map.Data[0]))))
	
	def DrawOutput(self):
		pass

	def DrawData(self):
		x, y = 0, 0
		for row in self.map.Data:#range(max(self.player.position[1] - math.ceil(TILESHIGH / 2) - 1, 0), min(self.player.position[1] + math.ceil(TILESHIGH / 2) + 1, len(self.map.Data))):
			for column in row:#range(max(self.player.position[0] - math.ceil(TILESWIDE / 2) - 1, 0), min(self.player.position[0] + math.ceil(TILESWIDE / 2) + 1, len(self.map.Data[0]))):
				self.window.blit(SPR[self.map.Data[y][x].name], self.camera.Apply(self.map.Data[y][x]))
				x+=1
			x=0
			y+=1
	
	def DrawEntityMap(self):
		for i in Entity.Instances:
				self.window.blit(i.sprite, self.camera.Apply(i))
			
