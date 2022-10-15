import pygame
import os
from pygame import font
from pygame.locals import( # more to be added as needed
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import colours as c # use c.[colour], right now only very basic colours supported

class textItem:
    colour = ''
    content = ''
    fontObj = None # The pygame font object goes here
    itself = None # The pygame surface object goes here
    selected = False
    
    def __init__(self, colour, content, font, fontSize):
        self.colour = colour
        self.content = content
        self.fontObj = pygame.font.Font(font, fontSize)
        self.itself = self.fontObj.render(content, True, colour)
    
    def select(self):
        self.itself = self.fontObj.render(('===' + self.content + '==='), True, c.red)
        self.fontObj.bold = True
        self.selected = True
    
    def unselect(self):
        self.fontObj.bold = False
        self.selected = False
        self.itself = self.fontObj.render(self.content, True, self.colour)

    def display(self, x, y):
        screen.blit(self.itself, (x, y))
    pass

# let pygame do it's thing
pygame.init()

# prepare the display surface
width, height = 1024, 768
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("TEST")

# define some colours 
# MOVED to colours.py so that colours can be used in class functions

# bools for the game and menu loops 
menu = True
running = False

# for proper FPS
clock = pygame.time.Clock()

# globals... yuck! Look into a better way to do this!
titleText = textItem(c.white, 'DEADHEARTH', 'courbd.ttf', 96)
menuOptions = [textItem(c.white, 'START GAME', 'cour.ttf', 40), textItem(c.white, 'QUIT', 'cour.ttf',40)]  
menuOptions[0].select()
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
            running = True
        if event.type == KEYDOWN:
            # quit on escape key
            if event.key == pygame.K_ESCAPE: 
                menu = False
                running = True
            # move down the menu
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                for i in range(len(menuOptions)): # maybe make this function a part of textItem class?
                    if menuOptions[i].selected and i != (len(menuOptions)) - 1:
                        menuOptions[i].unselect()
                        menuOptions[i + 1].select()
                        break
            # move up the menu
            if event.key == (pygame.K_UP or pygame.K_w):
                for i in range(len(menuOptions)): # maybe make this function a part of textItem class?
                    if menuOptions[i].selected and i != 0:
                        menuOptions[i].unselect()
                        menuOptions[i - 1].select()
                        break
            

            


while running: # if player has not quit game, loop for the main game
    clock.tick(60) # set to 60 fps
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # User clicks the X
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()