#!/usr/bin/env python2

import pygame
import random


WIDTH = 700
HEIGHT = 700
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
num = input("Enter path pls: ")
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS

test_image = pygame.image.load(num+".png").convert(8)
pallete = test_image.get_palette()

# Get only different colors, ignore multiple colors
set_of_pallete = []
for i in pallete:
        if i not in set_of_pallete:
            set_of_pallete.append(i)


another_random_pallete = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(len(set_of_pallete))]

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                another_random_pallete = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in range(len(set_of_pallete))]


    #2 Update
    test_image.set_palette(set_of_pallete)      # Set back to original palette
    #3 Draw/render
    screen.fill(BLACK)
    x = 64
    y = 4
    num = 0

    for color in set_of_pallete:
        num+=1
        pygame.draw.rect(screen,color,(x+16*num,y,16,16))

    num+=1 # leave a space bettween palettes
    for color in another_random_pallete:
        num+=1
        pygame.draw.rect(screen,color,(x+16*num,y,16,16))
    
    test_image_rect = screen.blit(test_image,(64,32))
    test_image.set_palette(another_random_pallete)
    screen.blit(test_image,test_image_rect.topright)

    pygame.display.update()

pygame.quit()