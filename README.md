# Pointillism-Art
This is a program that takes an image in the command line and converts it to a larger scale version of the image with a pointillism affect, 
similar to pointillism art.

The image is scaled up by a factor of 5 in order to maintain the detail in the image

then in a nested for loop, the r,g,b values of each pixel is taken, and the program determines how many of each colour pixel should be in the new block
of pixels(since it is scaled up 1 pixel is represented by 25 pixels in the new image)

The determined amount of red, green, and blue pixels is printed to the screen and after the loop is complete, the new pointillism art is created and
displayed on the screen

The program uses the pygame library
