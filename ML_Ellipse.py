#reference (draw ellipse & graphic): https://www.pygame.org/docs/ref/draw.html

# Import a library of functions called 'pygame'
import pygame
import numpy as np
import pylab as pl

import matplotlib.pyplot as plt

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = (0, 0, 0)
white = (255, 255, 255)

# Set the height and width of the screen
size = [1000, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(white)
    pygame.draw.ellipse(screen, black, [700, 260, 109, 100], 1)
    pygame.draw.ellipse(screen, black, [700, 135, 102, 100], 1)
    pygame.draw.ellipse(screen, black, [700, 10, 95, 100], 1)
    pygame.draw.ellipse(screen, black, [325, 260, 106, 100], 1)
    pygame.draw.ellipse(screen, black, [450, 135, 100, 100], 1)
    pygame.draw.ellipse(screen, black, [825, 10, 96, 100], 1)
    pygame.draw.ellipse(screen, black, [575, 260, 108, 100], 1)
    pygame.draw.ellipse(screen, black, [325, 135, 99, 100], 1)
    pygame.draw.ellipse(screen, black, [825, 260, 110, 100], 1)
    pygame.draw.ellipse(screen, black, [75, 10, 90, 100], 1)
    pygame.draw.ellipse(screen, black, [75, 135, 97, 100], 1)
    pygame.draw.ellipse(screen, black, [575, 135, 101, 100], 1)
    pygame.draw.ellipse(screen, black, [325, 10, 92, 100], 1)
    pygame.draw.ellipse(screen, black, [200, 135, 98, 100], 1)
    pygame.draw.ellipse(screen, black, [825, 135, 103, 100], 1)
    pygame.draw.ellipse(screen, black, [450, 10, 93, 100], 1)
    pygame.draw.ellipse(screen, black, [75, 260, 104, 100], 1)
    pygame.draw.ellipse(screen, black, [200, 10, 91, 100],1)
    pygame.draw.ellipse(screen, black, [200, 260, 105, 100], 1)
    pygame.draw.ellipse(screen, black, [575, 10, 94, 100], 1)
    pygame.draw.ellipse(screen, black, [450, 260, 107, 100], 1)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
# Be IDLE friendly
pygame.quit()

x=[]
y=[]

openfile = open('Dataset.txt', 'r')
for i in openfile:
    text = i.splitlines()
    tmp = text[0].split(" ")
    x.append(float(tmp[0]))
    y.append(int(tmp[1]))

x_1_0 = []
elips = []

x_1_0 = y
elips = x

sum_1_or_0 = 0
sum_elips = 0
sum_square_x_1_0 = 0
sum_1_0_multip_elips = 0
sum_square_elips = 0

for i in range(0,len(y)):
    sum_1_or_0 += x_1_0[i]
    sum_elips += elips[i]
    sum_square_x_1_0 += (x_1_0[i] * x_1_0[i])
    sum_1_0_multip_elips += (elips[i] * x_1_0[i])
    sum_square_elips += (elips[i] * elips[i])

x_mean = (sum_elips / 21)
y_mean = (sum_1_or_0 / 21)

n = 21

a = ( (sum_1_or_0 * sum_square_elips) - (sum_elips * sum_1_0_multip_elips) ) / ((n * sum_square_elips) - (sum_elips * sum_elips))
b = ( (n * sum_1_0_multip_elips) - (sum_1_or_0 * sum_elips) ) / ( (n * sum_square_elips) - (sum_square_elips * sum_square_elips) )

print("a = " , a , " b =" , b )
print('y = {0} + {1}x'.format(round(a,4),round(b,4)))

# These lines are for compare to my result  and to draw graph of equation with numpy library
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)
# fit_fn is now a function which takes in x and returns an estimate for y
plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
plt.show()
