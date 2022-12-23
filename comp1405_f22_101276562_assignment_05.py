# Kieran Fitzgerald 101276562

""" 
- must NOT import anything other than the pygame, random, and sys libraries
• must get the name of the source image as a command-line argument
• must use nested loops to visit each pixel of the source image and get its colour value
• must use one or more loops to draw an appropriate1 number of 'points' in your 'new' image
• must randomly alter the position of the drawn 'points' in your 'new' image2
• must NOT use colours for drawing 'points' other than red, green, blue and (if you wish) black3
• can assume that the user will always provide the name of a valid image when prompted
"""

import pygame
import sys
import random

#initialize pygame
pygame.init()

#initialize image source as the command line argument user provides
img_src = pygame.image.load(sys.argv[1])

#set width and height variables by calling get_size function
(wid,hgt) = img_src.get_size()

#set new width and new height variables
new_wid = wid * 5

new_hgt = hgt * 5

#create a blank window surface that is 4 times larger than original
win_sfc = pygame.display.set_mode((new_wid,new_hgt))

#start nested loop (first loop is for rows, second is for columns)
for y in range(hgt):
    for x in range(wid):

        #retrieving red green and blue values from each pixel that we iterate over
        (r,g,b, _) = img_src.get_at((x,y))

        #determining how many of each color pixel will be used in this block of pixels
        #if all three amount to 0, nothing will be printed so it will just be black in that region
        num_red = (r/50)
        num_green = (g/50)
        num_blue = (b/50)
    
        #precondition while loop that ends when we have printed all of the red pixels that we need to print
        while num_red > 0:
            #draw a circle at a random position in a range of 25 possible values
            pygame.draw.circle(win_sfc,(255,0,0),(random.randint((x*5)-5,(x*5)),random.randint((y*5)-5,(y*5))),1)
            #subtract one from number of pixels for the precondition
            num_red = num_red - 1
        while num_green > 0:
            pygame.draw.circle(win_sfc,(0,255,0),(random.randint((x*5)-5,(x*5)),random.randint((y*5)-5,(y*5))),1)
            num_green = num_green - 1
        while num_blue > 0:
            pygame.draw.circle(win_sfc,(0,0,255), (random.randint((x*5)-5,(x*5)),random.randint((y*5)-5,(y*5))),1)
            num_blue = num_blue - 1

#update the display
pygame.display.update()

#run while loop and check for user hitting quit button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()