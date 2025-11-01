import sys
import random as rd
import pygame
from pygame.locals import *
from classes import *
import pytest

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
def test_UFO():
    c1 = rd.randint(0,255)
    c2 = rd.randint(0,255)
    c3 = rd.randint(0,255)
    color = (c1,c2,c3)
    x = UFO(color, screen, 20,20,rd.randint(0,width),0) 
    assert x.return_color()
