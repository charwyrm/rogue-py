from __init__ import *
from map import *
from entity import Entity

class Game():
	def __init__(self, mapData):

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

		#128x64 = 16x8 tiles(1x)
		#1440x900 = 180x113 tiles(1x), 90x57(2x), 60x38(3x), 45x29(4x)
		#1920x1080 = 240x135 tiles

		self.frameTileWidth, self.frameTileHeight = 16, 8
		self.spriteResolution = 8
		self.frameScale = 2
		self.frameWidth, self.frameHeight = self.frameTileWidth*self.spriteResolution*self.frameScale, self.frameTileHeight*self.spriteResolution*self.frameScale
		#os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
		self.window = pg.display.set_mode((self.frameWidth, self.frameHeight))#, pg.NOFRAME)
		self.tileSize = 8*self.frameScale #sets the tilesize to 8 pixels
		self.tileOffset = 4*self.frameScale #sets the offset to 4 pixels (so we can make the player central)
		self.clock = pg.time.Clock() #creates a clock object, which can be used to interact with the FPS
		self.keyDelay = 0 #keystrokes are registered straight away
		self.isRunning = True
		self.pressedUp, self.pressedDown, self.pressedLeft, self.pressedRight = False, False, False, False

		self.spr = {"error":pg.image.load(os.path.join("content", "error.png")).convert(),
		"chest":pg.image.load(os.path.join("content", "chest.png")).convert(),
		"door":pg.image.load(os.path.join("content", "door.png")).convert(),
		"floor":pg.image.load(os.path.join("content", "floor.png")).convert(),
		"gold":pg.image.load(os.path.join("content", "gold.png")).convert_alpha(),
		"grass_ld":pg.image.load(os.path.join("content", "grass_ld.png")).convert(),
		"grass_md":pg.image.load(os.path.join("content", "grass_md.png")).convert(),
		"grass_hd":pg.image.load(os.path.join("content", "grass_hd.png")).convert(),
		"ladder":pg.image.load(os.path.join("content", "ladder.png")).convert(),
		"player":pg.image.load(os.path.join("content", "player.png")).convert_alpha(),
		"stairs_dsc":pg.image.load(os.path.join("content", "stairs_dsc.png")).convert(),
		"wall":pg.image.load(os.path.join("content", "wall.png")).convert(),
		"wallside":pg.image.load(os.path.join("content", "wallside.png")).convert(),
		"road":pg.image.load(os.path.join("content", "road.png")).convert()}

		for i in self.spr:
			self.spr[i] = pg.transform.scale(self.spr[i], (self.tileSize, self.tileSize))

		self.player = Entity((64, 59), self.spr["player"])
		self.map = TileMap(mapData) #creates an instance of map using the current map data
		#self.map.Shade() - Used with some texture packs
		self.frame = pg.Surface((len(self.map.tileMap[1])*self.tileSize,len(self.map.tileMap)*self.tileSize))

	def run(self):

		while self.isRunning:
			self.CheckInput() #checks for keys that are pressed or released and sets values accordingly
			self.ProcessInput() #acts upon the pressed keys' values

			self.window.fill(self.clr["black"]) #clears the window
			self.frame.fill(self.clr["black"])  #Layer 0
			self.DrawTileMap()                  #Layer 1
			self.DrawEntityMap()                #Layer 2

			self.clock.tick(60) #limit the game to 60 frames per second

			pg.transform.scale(self.frame, (self.frameWidth*self.frameScale, self.frameHeight*self.frameScale)) #scales the screen surface
			self.window.blit(self.frame, (self.player.position[0]*-self.tileSize+(self.frameWidth/2)-self.tileOffset, self.player.position[1]*-self.tileSize+(self.frameHeight/2)-self.tileOffset))

			pg.display.flip() #update window

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
				else:
					self.keyDelay = 0

	def ProcessInput(self):
		p = self.player.position #just a temporary variable to stop the code from being too verbose
		self.keyDelay -= self.clock.get_time() #decreases the delay by the milliseconds since the last frame

		if self.keyDelay <= 0: #if the delay is over
			
			if self.pressedUp and self.pressedLeft: #if up is pressed
				if 0 <= p[1]-1 and 0 <= p[0]-1: #if the space above is within bounds and
					if self.map.tileMap[p[1]-1][p[0]-1].isPassable: #if the move is into something passable (without collision)
						self.player.move((-1, -1)) #move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedUp and self.pressedRight: #if up is pressed
				if 0 <= p[1]-1 and len(self.map.tileMap[1]) > p[0]+1: #if the space above is within bounds and
					if self.map.tileMap[p[1]-1][p[0]+1].isPassable: #if the move is into something passable (without collision)
						self.player.move((1, -1)) #move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedDown and self.pressedLeft: #if up is pressed
				if 0 <= p[1]-1 and 0 <= p[0]-1: #if the space above is within bounds and
					if self.map.tileMap[p[1]+1][p[0]-1].isPassable: #if the move is into something passable (without collision)
						self.player.move((-1, 1)) #move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedDown and self.pressedRight: #if up is pressed
				if 0 <= p[1]-1 and len(self.map.tileMap[1]) > p[0]+1: #if the space above is within bounds and
					if self.map.tileMap[p[1]+1][p[0]+1].isPassable: #if the move is into something passable (without collision)
						self.player.move((1, 1)) #move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds
						
			elif self.pressedUp: #if up is pressed
				if 0 <= p[1]-1: #if the space above is within bounds and
					if self.map.tileMap[p[1]-1][p[0]].isPassable: #if the move is into something passable (without collision)
						self.player.move((0, -1)) #move the player up
						self.keyDelay = 180 #reset the delay to 200 milliseconds

			elif self.pressedDown: #if down is pressed
				if len(self.map.tileMap) > p[1]+1: #if the space below is within bounds and
					if self.map.tileMap[p[1]+1][p[0]].isPassable: #if the move is into something passable (without collision)
						self.player.move((0, 1)) #move the player down
						self.keyDelay = 180 #reset the delay to 200 milliseconds

			elif self.pressedLeft: #if left is pressed
				if 0 <= p[0]-1: #if the space to the left is within bounds and
					if self.map.tileMap[p[1]][p[0]-1].isPassable: #if the move is into something passable (without collision)
						self.player.move((-1, 0)) #move the player left
						self.keyDelay = 180 #reset the delay to 200 milliseconds

			elif self.pressedRight: #if right is pressed
				if len(self.map.tileMap[1]) > p[0]+1: #if the space to the right is within bounds and
					if self.map.tileMap[p[1]][p[0]+1].isPassable: #if the move is into something passable (without collision)
						self.player.move((1, 0)) #move the player right
						self.keyDelay = 180 #reset the delay to 200 milliseconds

	def DrawTileMap(self):
		for y in range (max(self.player.position[1]-round(self.frameTileHeight/2)-1, 0), min(self.player.position[1]+round(self.frameTileHeight/2)+1, len(self.map.tileMap))):
			for x in range (max(self.player.position[0]-round(self.frameTileWidth/2)-1, 0), min(self.player.position[0]+round(self.frameTileWidth/2)+1, len(self.map.tileMap[0]))):
				self.frame.blit(self.spr[self.map.tileMap[y][x].name], self.map.tileMap[y][x].GetPosition(self.tileSize))
	def DrawEntityMap(self):
		for i in Entity.Instances:
			self.frame.blit(i.sprite, i.GetPosition(self.tileSize))
