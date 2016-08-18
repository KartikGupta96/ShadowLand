"""
Shadowland Game
Author: Kartik Gupta
Date started: 8/17/16

Version 1 (8/17/16):
Currently Has a menu interface. When hovering over the play and instructions button there
the color changes. Will add functionality to pressing the button at a later stage.

"""
import pygame, sys

#Variables for width, height, font style and various colors
width = 800
height = 400
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
fontStyle ='hillBelly_TRIAL.ttf'

pygame.init()

#Create a window with the width and height from above.
#The caption of the window is Shadowland the name of the game.
#A clock and background image for the menu are initialized
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shadowland")
clock = pygame.time.Clock()
menuBG = pygame.image.load('MenuImage.jpg').convert()

#used to render the surface on which the text is written
def text_objects(text, font, color):

    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Creates the text for the play and instructions button.
#Changes color when hovered upon.
def mouseNtext():
    mouse = pygame.mouse.get_pos()
    if (440 > mouse[0] > 355 and 205 > mouse[1] > 190):
        playText = pygame.font.Font(fontStyle, 20)
        textSurf, textRect = text_objects("Find Out", playText, black)
        textRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(textSurf, textRect)

    else:
        playText = pygame.font.Font(fontStyle, 20)
        textSurf, textRect = text_objects("Find Out", playText, red)
        textRect.center = ((width / 2), (height / 2))
        gameDisplay.blit(textSurf, textRect)

    if (455 > mouse[0] > 345 and 242.5 > mouse[1] > 227.5):
        text = pygame.font.Font(fontStyle, 20)
        textSurf, textRect = text_objects("Instructions", text, black)
        textRect.center = ((width / 2), (height / 2) + 37.5)
        gameDisplay.blit(textSurf, textRect)

    else:
        playText = pygame.font.Font(fontStyle, 20)
        textSurf, textRect = text_objects("Instructions", playText, blue)
        textRect.center = ((width / 2), (height / 2)+ 37.5)
        gameDisplay.blit(textSurf, textRect)

#Game menu function. Will call the mouseNText function and will update the menu
def game_menu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()

        gameDisplay.blit(menuBG,(0,0))

        mouseNtext()
        pygame.display.flip()
        clock.tick(10)
#Currently not needed but will be used when the play button is clicked.
def game_loop():
    gameWorking = True

    while gameWorking:

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                gameWorking = False

        pygame.display.flip()
        clock.tick(10)

#functions called in order to run the game.
game_menu()
game_loop()
pygame.quit()
