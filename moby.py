#################################################
#                   Moby
# Moby Dick is a sailing simulator
# intended to cross the seven seas.
#
# Usage:
# > python3 moby.py
#
# v0.006
# Issue 3
# 20180217-
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
# import random
# import math


# Global variables
SCREENSIZE = (1024, 576)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGREY = (230, 230, 230)
BACKGROUND = (60, 185, 240)


# load image function
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = SCREENSIZE
        self.bgcolour = BACKGROUND
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('Moby Dick')
        # background image and its enclosing rectangle
        if image_file:
            self.image = load_image(image_file)
            self.rect = self.image.get_rect()
        else:
            self.image = ''
            self.rect = Rect(0, 0, 0, 0)
        # show image
        self.show()

    def show(self):
        # fill screen with solid colour
        self.display.fill(self.bgcolour)
        # blit background image
        if self.image != '':
            self.display.blit(self.image, (0, 0))


# the Heads Up Display
class Hud(object):
    """
    The HUD (Heads Up Display) will show on screen all relevant information
    """
    def __init__(self):
        self.left = ['Wind Direction', 'Wind Intensity']
        self.middle = ['Absolute Sail','Relative Sail', 'Point of Sail']
        self.right = ['Heading', 'Tiller', 'Rudder']

    def draw(self, fnt, scr):
        # HUD text
        scr.display.blit(writetext(fnt, self.left[0], LIGHTGREY), (5, 5))
        scr.display.blit(writetext(fnt, self.left[1], LIGHTGREY), (5, 20))
        scr.display.blit(writetext(fnt, self.middle[0], LIGHTGREY), (150, 5))
        scr.display.blit(writetext(fnt, self.middle[1], LIGHTGREY), (150, 20))
        scr.display.blit(writetext(fnt, self.middle[2], LIGHTGREY), (150, 35))
        scr.display.blit(writetext(fnt, self.right[0], LIGHTGREY), (300, 5))
        scr.display.blit(writetext(fnt, self.right[1], LIGHTGREY), (300, 20))
        scr.display.blit(writetext(fnt, self.right[2], LIGHTGREY), (300, 35))
        # HUD values
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (100, 5))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (100, 20))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (240, 5))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (240, 20))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (240, 35))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (355, 5))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (355, 20))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (355, 35))


# event loop
def eventloop(scr, fnt, clk, hud):
    # arguments: scr=screen, fnt=font, clk=clock, hud=HUD
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(60)
        # write text
        # scr.display.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        hud.draw(fnt, scr)
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Moby :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('fonts/Chicago Normal.ttf', 12)
    clock = pygame.time.Clock()
    # score = 0
    # start the display
    screen = Screen()
    # screen = Screen('background green 640x480.png')
    # initialize HUD
    hud = Hud()
    # start the event loop
    eventloop(screen, font1, clock, hud)


# execute main
if __name__ == '__main__': 
    main()


