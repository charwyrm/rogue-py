import pygame as pg #imports PyGame with the alias pg
import os #imports OS specific commands, in our case allowing us to path to files no matter the OS
import sys #imports system specific parameters and functions (we use this to quit the game correctly)
import random
import math

WIDTH = 256
HEIGHT = 128
PIXELSIZE = 8
SCALE = 1
TILESWIDE = math.ceil(WIDTH/(PIXELSIZE * SCALE))
TILESHIGH = math.ceil(HEIGHT/(PIXELSIZE * SCALE))
TILESIZE = PIXELSIZE * SCALE
OFFSETX = TILESIZE % WIDTH - (TILESIZE/2)
OFFSETY = TILESIZE % HEIGHT - (TILESIZE/2)
#os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

SPR = {"error":pg.image.load(os.path.join("content", "error.png")),
"chest":pg.image.load(os.path.join("content", "chest.png")),
"door":pg.image.load(os.path.join("content", "door.png")),
"floor":pg.image.load(os.path.join("content", "floor.png")),
"gold":pg.image.load(os.path.join("content", "gold.png")),
"grass_ld":pg.image.load(os.path.join("content", "grass_ld.png")),
"grass_md":pg.image.load(os.path.join("content", "grass_md.png")),
"grass_hd":pg.image.load(os.path.join("content", "grass_hd.png")),
"ladder":pg.image.load(os.path.join("content", "ladder.png")),
"player":pg.image.load(os.path.join("content", "player.png")),
"stairs_dsc":pg.image.load(os.path.join("content", "stairs_dsc.png")),
"wall":pg.image.load(os.path.join("content", "wall.png")),
"wallside":pg.image.load(os.path.join("content", "wallside.png")),
"road":pg.image.load(os.path.join("content", "road.png"))}

CLR = {"black":(0, 0, 0),
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
