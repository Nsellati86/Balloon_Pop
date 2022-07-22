import pygame
import sys
import random
from math import *

pygame.init()

width = 700
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon_Pop")
clock = pygame.time.Clock()

margin = 100
lowerBound = 100
score = 0
