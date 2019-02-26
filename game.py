from __init__ import *
from map import Map
from entity import Entity

class Game():
	def __init__(self):
		self.screenScale = 1
		screenWidth, screenHeight = 128*self.screenScale, 64*self.screenScale
		self.screen = pg.display.set_mode((screenWidth, screenHeight))

		self.spr = {"error":pg.image.load(os.path.join("content", "error.bmp")).convert(),
		"chest":pg.image.load(os.path.join("content", "chest.bmp")).convert(),
		"door":pg.image.load(os.path.join("content", "door.bmp")).convert(),
		"floor":pg.image.load(os.path.join("content", "floor.bmp")).convert(),
		"gold":pg.image.load(os.path.join("content", "gold.bmp")).convert(),
		"grass_ld":pg.image.load(os.path.join("content", "grass_ld.bmp")).convert(),
		"grass_md":pg.image.load(os.path.join("content", "grass_md.bmp")).convert(),
		"grass_hd":pg.image.load(os.path.join("content", "grass_hd.bmp")).convert(),
		"ladder":pg.image.load(os.path.join("content", "ladder.bmp")).convert(),
		"smile":pg.image.load(os.path.join("content", "smile.bmp")).convert(),
		"stairs_dsc":pg.image.load(os.path.join("content", "stairs_dsc.bmp")).convert(),
		"wall":pg.image.load(os.path.join("content", "wall.bmp")).convert()}

		self.tileSize = 8*self.screenScale #sets the tilesize to 8 pixels
		self.tileOffset = 4*self.screenScale #sets the offset to 4 pixels (so we can make the player central)

		for i in self.spr:
			self.spr[i] = pg.transform.scale(self.spr[i], (self.tileSize, self.tileSize))

		self.clr = {"black":(0, 0, 0),
		"dark gray":(63, 63, 63),
		"gray":(127, 127, 127),
		"light gray":(224, 224, 224),
		"white":(255, 255, 255),
		"red":(255, 0, 0),
		"orange":(255, 127, 0),
		"yellow":(255, 255, 0),
		"lime":(127, 255, 0),
		"green":(0, 255, 0),
		"mint":(0, 255, 127),
		"cyan":(0, 255, 255),
		"azure":(0, 127, 255),
		"blue":(0, 0, 255),
		"purple":(127, 0, 255),
		"magenta":(255, 0, 255),
		"pink":(255, 0, 127)}

		self.player = Entity((7, 3), self.spr["smile"])
		self.clock = pg.time.Clock() #creates a clock object, which can be used to interact with the FPS
		self.keyDelay = 0 #keystrokes are registered straight away
		self.isRunning = True
		self.pressedUp, self.pressedDown, self.pressedLeft, self.pressedRight = False, False, False, False

		mapData = [
		"#######D#######",
		"#.............#",
		"#.c.........c.#",
		"D........g.ggGD",
		"#.H...g.g.g6<6#",
		"#......g.gGG66#",
	  "#######D#######"]

		self.map = Map(mapData) #creates an instance of map using the current map data

	def run(self):

		while self.isRunning:
			self.DrawMap()#draws the map to the screen
			#self.DrawEntities() #coming soon - will draw entities to the screen
			self.screen.blit(self.player.sprite, self.player.GetPosition(self.tileSize, self.tileOffset)) #blits the player to the screen surface at the player's current position

			#for y in range (0, round(self.screen.get_height()/self.tileSize)*2+1): #for every row of tiles
			#	for x in range (0, round(self.screen.get_height()/self.tileSize)*2+1): #for every column of tiles within said rows
			#		self.screen.set_at(((x*self.tileSize)+self.tileOffset, (y*self.tileSize)+self.tileOffset), (255, 0, 0)) #draw a red pixel at the top-left of the tile
	
			self.CheckInput() #checks for keys that are pressed or released and sets values accordingly
			self.ProcessInput() #acts upon the pressed keys' values

			print("{}fps, player at {}".format((round(self.clock.get_fps())), self.player.position)) #print the FPS to the console
			self.clock.tick(60) #limit the game to 60 frames per second
			pg.transform.scale(self.screen, (256, 128))
			pg.display.flip() #update all displays
			self.screen.fill(self.clr["black"]) #wipe the screen to black, so none of the previous frame remains

	def CheckInput(self):
		for event in pg.event.get(): #for every event in the event queue
			if event.type == pg.QUIT: #if it's the window being exited (hitting the red x)
				pg.quit() #stop pygame
				sys.exit() #exit the window

			elif event.type == pg.KEYDOWN: #otherwise, if it's the rising edge of a keypress (the instant a keystroke happens, not the key being held down)
				if event.key == pg.K_w: #if said key is w
					self.pressedUp = True #move the player up
				elif event.key == pg.K_s: #otherwise, if said key is s
					self.pressedDown = True #move the player down
				elif event.key == pg.K_a: #otherwise, if said key is a
					self.pressedLeft = True #move the player left
				elif event.key == pg.K_d: #otherwise, if said key is d
					self.pressedRight = True #move the player right

			elif event.type == pg.KEYUP: #otherwise, if it's the falling edge of a keypress (when a key is released)
				if event.key == pg.K_w: #if said key is w
					self.pressedUp = False #move the player up
				elif event.key == pg.K_s: #otherwise, if said key is s
					self.pressedDown = False #move the player down
				elif event.key == pg.K_a: #otherwise, if said key is a
					self.pressedLeft = False #move the player left
				elif event.key == pg.K_d: #otherwise, if said key is d
					self.pressedRight = False #move the player right
				self.keyDelay = 0

	def ProcessInput(self):
		p = self.player.position #just a temporary variable to stop the code from being too verbose
		self.keyDelay -= self.clock.get_time() #decreases the delay by the milliseconds since the last frame

		if self.keyDelay <= 0: #if the delay is over
			if self.pressedUp: #if up is pressed
				if not p[1]-1 <= -1: #if the space above is within bounds and
					if self.map.tileMap[p[1]-1][p[0]].isPassable: #if the move is into something passable (without collision)
						self.player.move((0, -1)) #move the player up
						self.keyDelay = 200 #reset the delay to 200 milliseconds

			if self.pressedDown: #if down is pressed
				if not p[1]+1 >= 7: #if the space below is within bounds and
					if self.map.tileMap[p[1]+1][p[0]].isPassable: #if the move is into something passable (without collision)
						self.player.move((0, 1)) #move the player down
						self.keyDelay = 200 #reset the delay to 200 milliseconds

			if self.pressedLeft: #if left is pressed
				if not p[0]-1 <= -1: #if the space to the left is within bounds and
					if self.map.tileMap[p[1]][p[0]-1].isPassable: #if the move is into something passable (without collision)
						self.player.move((-1, 0)) #move the player left
						self.keyDelay = 200 #reset the delay to 200 milliseconds

			if self.pressedRight: #if right is pressed
				if not p[0]+1 >= 15: #if the space to the right is within bounds and
					if self.map.tileMap[p[1]][p[0]+1].isPassable: #if the move is into something passable (without collision)
						self.player.move((1, 0)) #move the player right
						self.keyDelay = 200 #reset the delay to 200 milliseconds

	def DrawMap(self):
		for y in self.map.tileMap: #for every row in map.map
			for x in y: #for every position in that row
				self.screen.blit(self.spr[x.name], x.GetPosition(self.tileSize, self.tileOffset)) #blit that tile's sprite to it's screen position