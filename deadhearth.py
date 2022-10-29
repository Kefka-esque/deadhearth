import pygame
import os
import random
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

# for buildings
class building(pygame.sprite.Sprite):
    
    def __init__(self, name, dimensions):
        super().__init__()
        self.name = name # str for the building type
        self.dimensions = dimensions # tuple for the dimensions, rectangles only
        self.surface = None # will hold the pygame.surface object, created in choosePlace()
    
    def choosePlace(self, surface): # takes in the main display surface and in order to 
        selected = [15, 15] # selection defaults to the middle(ish) of the screen
        self.surface = pygame.surface((self.dimensions[0] * 32, self.dimensions[1] * 24)) # since tilemap size is 32x32, it is initialized as [tile size] * [display surface size / 32]
        tileArray = self.generateTiles()
        for y in range(tileArray):
            for x in range(tileArray):
                pass

        #  This mess is commented out for now. Why the hell did I think this was an OK way to do this???
        # while True:
        #     for i in range(selected[0], selected[0] + self.dimensions[0]):
        #         theMap[selected[0]][i].colour = c.yellow
        #         theMap[selected[0]][i + self.dimensions[1]] = c.yellow
        #         theMap[selected[0]][i].render = theMap[selected[0]][i].fontObj.render(theMap[selected[0]][i].symbol, True, theMap[selected[0]][i].colour)
        #         theMap[selected[0]][i + self.dimensions].render = theMap[selected[0]][i].fontObj.render(theMap[selected[0]][i].symbol, True, theMap[selected[0]][i + self.dimensions[1]].colour)

        #     for i in range(selected[1], selected[1] + self.dimensions[1]):
        #         theMap[i][selected[1]].colour = c.yellow
        #         theMap[i][selected[1]].render = theMap[i][selected[1]].fontObj.render(theMap[i][selected[1]].symbol, True, theMap[i][selected[1]].colour)
        #     for event in pygame.event.get():
        #         if event.type == KEYDOWN:
        #             if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        #                 selected[0] += 1
        #             if event.key == pygame.K_UP or event.key == pygame.K_w:
        #                 if selected[0] != 0:
        #                     selected[0] -= 1
        #             if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #                 if selected[1] != 0:
        #                     selected[1] -= 1
        #             if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #                 selected[1] += 1
        #             if event.key == pygame.K_ESCAPE:
        #                 running = False
        #                 pygame.quit()
        #     screen.fill(c.black)
        #     for i in range(32): #display the map
        #         for o in range(32):
        #             screen.blit(theMap[i][o].render, theMap[i][o].pos)
        #     pygame.display.flip()
    
    def generateTiles(self): # generates the tiles for the new building and returns it as an array
        tiles = [[]]
        buildingWidth = self.dimensions[0]
        buildingHeight = self.dimensions[1]
        if self.name == "Hearth":
            for y in range(0, buildingHeight - 1): # played with making this a nested loop similiar to generateMap(), but it seemed simpler to just do it this way
                if y == 0:
                    tiles[y].append(tile('cWall', (0 * 32, y * 24)))
                    tiles[y].append(tile('hWall', (1 * 32, y * 24)))
                    tiles[y].append(tile('hWall', (2 * 32, y * 24)))
                    tiles[y].append(tile('hWall', (3 * 32, y * 24)))
                    tiles[y].append(tile('cWall', (4 * 32, y * 24)))
                    
                elif y == 4:
                    tiles[y].append(tile('cWall', (0 * 32, y * 24)))
                    tiles[y].append(tile('hWall', (1 * 32, y * 24)))
                    tiles[y].append(tile('door', (2 * 32, y * 24)))
                    tiles[y].append(tile('hWall', (3 * 32, y * 24)))
                    tiles[y].append(tile('cWall', (4 * 32, y * 24)))
                
                else:
                    tiles[y].append(tile('vWall', (0 * 32, y * 24)))
                    tiles[y].append(tile('floor', (1 * 32, y * 24)))
                    tiles[y].append(tile('floor', (2 * 32, y * 24)))
                    tiles[y].append(tile('floor', (3 * 32, y * 24)))
                    tiles[y].append(tile('vWall', (4 * 32, y * 24)))
            
            return tiles
            


# for text
class textItem(pygame.sprite.Sprite):
    colour = ''
    content = ''
    fontObj = None # pygame font object goes here
    itself = None # pygame surface object goes here
    selected = False # for cases where player is selecting from a set of options
    
    def __init__(self, colour, content, font, fontSize):
        super().__init__()
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
class tile(pygame.sprite.Sprite): 
    type = '' # str for tile name
    symbol = '' # symbol to display on map
    moveable = True # can this tile be moved through?
    transparent = True
    
    def __init__(this, type, pos):
        super().__init__()
        this.type = type
        this.pos = pos
        # this a tuple is for the tilemap, but denotes it's position on the main display surface.
        # since tilemap size is 32x32, it is initialized as [tile number] * [surface size / 32]
        # see generateMap() to see what I mean.
        
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
        
        this.fontObj = pygame.font.Font('cour.ttf', 32)
        this.render = this.fontObj.render(this.symbol, True, this.colour)	
    
    def changeType(self, type): # for when tiles need to change type
        # check for what we are changing the tile into
        if type == 'grass':
            self.symbol = '"'
            self.colour = c.green
        
        if type == 'floor':
            self.symbol = '.'
            self.colour = c.white
        
        if type == 'vWall':
            self.symbol = 'ǁ'
            self.colour = c.brown
            self.moveable = False
            self.transparent = False

        if type == 'hWall':
            self.symbol = '='
            self.colour = c.brown
            self.moveable = False
            self.transparent = False

        if type == 'cWall':
            self.symbol = '^'
            self.colour = c.brown
            self.moveable = False
            self.transparent = False

        if type == 'door':
            self.symbol = '∩'
            self.colour = c.tan
            self.moveable = True
            self.transparent = False

        if type == 'water':
            self.symbol = '~'
            self.colour = c.blue
            self.moveable = False

        if type == 'bridge':
            self.symbol = '#'
            self.colour = c.brown
        #change other important variables so everything works
        self.render = self.fontObj.render(self.symbol, True, self.colour)
        self.type = type
    # return the tile type
    def getType(self): 
        return self.type

def generateMap():
    # generates the random map. Initializes a 32x32 grid of tiles, and then picks a side for a river and generates it by changing the necessary tiles.
    map = [[]]
    # generate a 32x32 array of tiles for the map with all grass to start with
    for i in range(32):
        for o in range(32):
            map[i].append(tile('grass', (i * 32, o * 24))) # this should be changed so that it will scale with different display resolutions; this will only work properly with 1024x768
        if i < 31:
            map.append([])
    
    # choose a side for the river
    direction = random.randrange(0, 3) # choose a direction, N E S W = 0 1 2 3
    if direction == 0: 
        # north side river
        for i in range(32):
                if i < 15 or i > 17:
                    map[2][i].changeType('water')
                    map[3][i].changeType('water')
                if i > 14 and i <18:
                    map[2][i].changeType('bridge')
                    map[3][i].changeType('bridge')
    if direction == 1: 
        # east
        for i in range(32):
                if i < 15 or i > 17:
                    map[i][28].changeType('water')
                    map[i][29].changeType('water')
                if i > 14 and i <18:
                    map[i][28].changeType('bridge')
                    map[i][29].changeType('bridge')
    if direction == 2: 
        # south
        for i in range(32):
                if i < 15 or i > 17:
                    map[28][i].changeType('water')
                    map[29][i].changeType('water')
                if i > 14 and i <18:
                    map[28][i].changeType('bridge')
                    map[29][i].changeType('bridge')
    if direction == 3: 
        # west
        for i in range(32):
                if i < 15 or i > 17:
                    map[i][2].changeType('water')
                    map[i][3].changeType('water')
                if i > 14 and i <18:
                    map[i][2].changeType('bridge')
                    map[i][3].changeType('bridge')

    return map


def menu(): # function to run at game start to handle the menu
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
screenSize = (1024, 768)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Deadhearth")

# define some colours 
# MOVED to colours.py so that colours can be used in class functions

# for proper FPS
clock = pygame.time.Clock()

running = menu() # run the main menu and return a bool for the main loop

theMap = generateMap()
house = building((5, 5), 'Hearth')
house.choosePlace(theMap)

while running: # loop for the main game
    clock.tick(60) # set to 60 fps
    screen.fill(c.black)
    for i in range(32): #display the map
        for o in range(32):
            screen.blit(theMap[i][o].render, theMap[i][o].pos)
    pygame.display.flip()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # User clicks the X
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
