import pygame
import os
from pygame import font

from pygame.locals import( 
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
) 

import colours as c # use c.[colour], right now only very basic colours supported

# for text
class textItem:
    colour = ''
    content = ''
    fontObj = None # pygame font object goes here
    itself = None # pygame surface object goes here
    selected = False # for cases where player is selecting from a set of options
    
    def __init__(self, colour, content, font, fontSize):
        self.colour = colour
        self.content = content
        self.fontObj = pygame.font.Font(font, fontSize)
        self.itself = self.fontObj.render(content, True, colour)
    
    def select(self): # shows player selection in a set of options
        self.itself = self.fontObj.render(('===' + self.content + '==='), True, c.red)
        self.fontObj.bold = True
        self.selected = True
    
    def unselect(self): # if player unselects
        self.fontObj.bold = False
        self.selected = False
        self.itself = self.fontObj.render(self.content, True, self.colour)

    def display(self, x, y): # render to screen
        screen.blit(self.itself, (x, y))

# tiles that go in the map array
class tile: 
	type = '' # str for tile name
	symbol = '' # symbol to display on map
	moveable = True # can this tile be moved through?
	transparent = True
	
	def __init__(this, type):
		this.type = type
		if type == 'grass':
			this.symbol = '"'
			this.colour = c.green
		
		if type == 'floor':
			this.symbol = '.'
			this.colour = c.white
		
		if type == 'vWall':
			this.symbol = 'ǁ'
			this.colour = c.brown
			this.moveable = False
			this.transparent = False

		if type == 'hWall':
			this.symbol = '='
			this.colour = c.brown
			this.moveable = False
			this.transparent = False

		if type == 'cWall':
			this.symbol = '^'
			this.colour = c.brown
			this.moveable = False
			this.transparent = False

		if type == 'door':
			this.symbol = '∩'
			this.colour = c.tan
			this.moveable = True
			this.transparent = False

		if type == 'water':
			this.symbol = '~'
			this.colour = c.blue
			this.moveable = False

		if type == 'bridge':
			this.symbol = '#'
			this.colour = c.brown
			
			
	
	# return the tile type
	def getType(this): 
		return this.type

def generateMap():
    
    map = [[]]
    i = 0
    
    for i  in range(32):
        
        for o in range(32):
            map[i].append(tile('grass'))

        if i < 31:
            map.append([])
    return map


def menu():
    titleText = textItem(c.white, 'DEADHEARTH', 'courbd.ttf', 96)
    menuOptions = [textItem(c.white, 'START GAME', 'cour.ttf', 40), textItem(c.white, 'QUIT', 'cour.ttf',40)]  
    menuOptions[0].select()
    menu = True
    # loop for the main menu:
    while menu:
        screen.fill(c.black)
        titleText.display(150, 200)
        menuOptions[0].display(200, 300)
        menuOptions[1].display(200, 345)
        pygame.display.flip()
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # User clicks the X
                menu = False
            if event.type == KEYDOWN:
                # quit on escape key
                if event.key == pygame.K_ESCAPE: 
                    menu = False
                # move down the menu
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    for i in range(len(menuOptions)): # maybe make this function a part of textItem class?
                        if menuOptions[i].selected and i != (len(menuOptions)) - 1:
                            menuOptions[i].unselect()
                            menuOptions[i + 1].select()
                            break
                
                # move up the menu
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    for i in range(len(menuOptions)): # maybe make this function a part of textItem class?
                        if menuOptions[i].selected and i != 0:
                            menuOptions[i].unselect()
                            menuOptions[i - 1].select()
                            break

                # make a menu selection
                if event.key == pygame.K_SPACE or event.key == K_RETURN:
                    # if start game selected:
                    if menuOptions[0].selected:
                        running = True
                        menu = False
                        return running
                        break

                    if menuOptions[1].selected:
                        menu = False
                        break
# let pygame do its thing
pygame.init()

# prepare the display surface
width, height = 1024, 768
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("TEST")

# define some colours 
# MOVED to colours.py so that colours can be used in class functions

# for proper FPS
clock = pygame.time.Clock()

running = menu() # run the main menu and return a bool for the main loop

map = generateMap()

for i in range(32):
    for o in range(32):
        print(map[i][o].colour)
print(len(map))

while running: # loop for the main game
    clock.tick(60) # set to 60 fps
    screen.fill(c.white)
    test = textItem(c.red, 'Game started!', 'cour.ttf', 90)
    test.display(200, 200)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # User clicks the X
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()