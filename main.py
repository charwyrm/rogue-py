import pygame as pg #imports PyGame with the alias pg
import os #imports OS specific commands, in our case allowing us to path to files no matter the OS
import sys #imports system specific parameters and functions (we use this to quit the game correctly)

screenWidth, screenHeight = 128, 64 #sets the size of the game window
tileSize = 8 #sets the tilesize to 8 pixels
tileOffset = 4 #sets the offset to 4 pixels (so we can make the player central)
screen = pg.display.set_mode((screenWidth, screenHeight)) #creates the main display as screen
clock = pg.time.Clock() #creates a clock object, which can be used to interact with the FPS
sprite = pg.image.load(os.path.join("content", "player.bmp")).convert() #gives it the variable sprite, which is set to player.bmp, an image in the content folder

		
playerX, playerY = (screen.get_width()/2)-tileOffset, (screen.get_height()/2)-tileOffset #sets the player's X and Y to the centre of the screen

while True:
	screen.blit(sprite, (playerX, playerY)) #blits the player to the screen surface at the player's current position

	for y in range (0, round(screen.get_height()/tileSize)*2+1): #for every row of tiles
		for x in range (0, round(screen.get_height()/tileSize)*2+1): #for every column of tiles within said rows
			screen.set_at(((x*tileSize)+tileOffset, (y*tileSize)+tileOffset), (255, 0, 0)) #draw a red pixel at the top-left of the tile
	
	for event in pg.event.get(): #for every event in the queue
		if event.type == pg.QUIT: #if it's the window being exited
			pg.quit() #quit pygame
			sys.exit() #exit the window

	print(round(clock.get_fps()), "fps") #print the FPS to the console
	clock.tick(60) #limit the game to 60 frames per second
	pg.display.flip() #update all displays (this will be replaced by a dirty rect updater)
	screen.fill((0, 0, 0)) #wipe the screen to black, so none of the previous frame remains
