import pygame as pg #imports PyGame with the alias pg
import os #imports OS specific commands, in our case allowing us to path to files no matter the OS
import sys #imports system specific parameters and functions (we use this to quit the game correctly)

from player import Player

screenWidth, screenHeight = 128, 64 #sets the size of the game window
tileSize = 8 #sets the tilesize to 8 pixels
tileOffset = 4 #sets the offset to 4 pixels (so we can make the player central)
screen = pg.display.set_mode((screenWidth, screenHeight)) #creates the main display as screen
clock = pg.time.Clock() #creates a clock object, which can be used to interact with the FPS
		
plr = Player((screen.get_width()/2)-tileOffset, (screen.get_height()/2)-tileOffset) #creates an instance of player called plr, and at the centre of the screen
plr.sprite.convert()

while True:
	screen.blit(plr.sprite, plr.position) #blits the player to the screen surface at the player's current position

	for y in range (0, round(screen.get_height()/tileSize)*2+1): #for every row of tiles
		for x in range (0, round(screen.get_height()/tileSize)*2+1): #for every column of tiles within said rows
			screen.set_at(((x*tileSize)+tileOffset, (y*tileSize)+tileOffset), (255, 0, 0)) #draw a red pixel at the top-left of the tile
	
	for event in pg.event.get(): #for every event in the queue
		if event.type == pg.QUIT: #if it's the window being exited
			pg.quit() #quit pygame
			sys.exit() #exit the window

		elif event.type == pg.KEYDOWN: #otherwise, if it's the rising edge of a keypress
			if event.key == pg.K_w: #if said key is w
				plr.move((0, -tileSize)) #move the player up
			elif event.key == pg.K_s: #otherwise, if said key is s
				plr.move((0, tileSize)) #move the player down
			elif event.key == pg.K_a: #otherwise, if said key is a
				plr.move((-tileSize, 0)) #move the player left
			elif event.key == pg.K_d: #otherwise, if said key is d
				plr.move((tileSize, 0)) #move the player right

	print(round(clock.get_fps()), "fps") #print the FPS to the console
	clock.tick(60) #limit the game to 60 frames per second
	pg.display.flip() #update all displays (this will be replaced by a dirty rect updater)
	screen.fill((0, 0, 0)) #wipe the screen to black, so none of the previous frame remains
