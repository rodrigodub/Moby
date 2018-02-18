#################################################
#                   Moby
# Moby Dick is a sailing simulator
# intended to cross the seven seas.
#
# Usage:
# > python3 moby.py
#
# v0.009
# Issue 2
# 20180217-20180218
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import random
# import math


# Global variables
# sizes and position
SCREENSIZE = (1024, 576)
HUDLEFT = 5
HUDMIDDLE = 200
HUDRIGHT = 400
# colours
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
    def __init__(self, fnt, scr):
        self.left = ['Wind Direction', 'Wind Speed']
        self.middle = ['Absolute Sail','Relative Sail', 'Point of Sail']
        self.right = ['Heading', 'Tiller', 'Rudder']
        self.initial(fnt, scr)

    def initial(self, fnt, scr):
        # HUD text
        scr.display.blit(writetext(fnt, self.left[0], LIGHTGREY), (HUDLEFT, 5))
        scr.display.blit(writetext(fnt, self.left[1], LIGHTGREY), (HUDLEFT, 20))
        scr.display.blit(writetext(fnt, self.middle[0], LIGHTGREY), (HUDMIDDLE, 5))
        scr.display.blit(writetext(fnt, self.middle[1], LIGHTGREY), (HUDMIDDLE, 20))
        scr.display.blit(writetext(fnt, self.middle[2], LIGHTGREY), (HUDMIDDLE, 35))
        scr.display.blit(writetext(fnt, self.right[0], LIGHTGREY), (HUDRIGHT, 5))
        scr.display.blit(writetext(fnt, self.right[1], LIGHTGREY), (HUDRIGHT, 20))
        scr.display.blit(writetext(fnt, self.right[2], LIGHTGREY), (HUDRIGHT, 35))

    def draw(self, fnt, scr, wind):
        # clean
        pygame.draw.rect(scr.display, BACKGROUND, (HUDLEFT + 95, 5, 50, 15), 0)
        pygame.draw.rect(scr.display, BACKGROUND, (HUDLEFT + 95, 20, 50, 15), 0)
        # HUD values
        scr.display.blit(writetext(fnt, ':  {}'.format(wind.direction), LIGHTGREY), (HUDLEFT + 95, 5))
        scr.display.blit(writetext(fnt, ':  {}'.format(wind.speed), LIGHTGREY), (HUDLEFT + 95, 20))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (HUDMIDDLE + 90, 5))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (HUDMIDDLE + 90, 20))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (HUDMIDDLE + 90, 35))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (HUDRIGHT + 55, 5))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (HUDRIGHT + 55, 20))
        scr.display.blit(writetext(fnt, ':  0', LIGHTGREY), (HUDRIGHT + 55, 35))


# the Wind
class Wind(object):
    """
    Everything related to the Wind.
    Wind Speed measured in Knots.
    """
    def __init__(self):
        self.direction = random.randint(0, 360)
        self.speed = random.randint(0, 21)

    def changedirection(self):
        if random.randint(0, 200) == 1:
            self.direction += 2 * (random.randint(0, 2) - 1)
        if self.direction >= 360:
            self.direction = self.direction - 360
        if self.direction < 0:
            self.direction = 360 + self.direction

    def changespeed(self):
        if random.randint(0, 200) == 1:
            self.speed += random.randint(0, 2) - 1
        # limit to Beaufort force 5
        if self.speed < 0:
            self.speed = 0
        if self.speed > 21:
            self.speed = 21

    def update(self):
        self.changedirection()
        self.changespeed()


# event loop
def eventloop(scr, fnt, clk, hud, wind):
    # arguments: scr=screen, fnt=font, clk=clock, hud=HUD, wind=wind
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
        hud.draw(fnt, scr, wind)
        # change wind direction & speed
        wind.update()
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
    hud = Hud(font1, screen)
    # create the Wind
    wind = Wind()
    # start the event loop
    eventloop(screen, font1, clock, hud, wind)


# execute main
if __name__ == '__main__': 
    main()


