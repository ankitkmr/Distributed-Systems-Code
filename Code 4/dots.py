# Poke The Dots
# There are two dots that are moving on a 500 by 400 window
# There is a score board that displays the time in seconds
# since the game started
# If the player clicks inside the window, the dots disappear
# and reappear at some random location
# If the dots collide, the dots stop moving, the score stops 
# changing and Game Over is displayed.
# Version 1
import pygame, sys, time
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # window size
   windowTitle = 'Poke The Dots' #window title 
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize red dot and blue dot
   gameOver = False
   color1=pygame.Color('red')
   center1 = [50, 75] 
   radius1=30
   speed1=[1,2]
   color2=pygame.Color('blue')
   center2=[200,100]
   radius2=40
   speed2=[2,1]

   # Draw objects
   pygame.draw.circle(surface, color1, center1, radius1, 0)
   pygame.draw.circle(surface, color2,center2,radius2,0)
   gameOver = update(surface, color1, center1, radius1, speed1, color2, center2, radius2, speed2)
   # Refresh the display
   pygame.display.update()

   # Loop forever
   while True:
      # Handle events
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         # Handle additional events

      # Update and draw objects for the next frame
      #gameOver = update(center, surface)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def update(surface, color1, center1, radius1, speed1, color2, center2, radius2, speed2):

   #Check if the game is over. If so, end the game and
   #returnTrue. Otherwise, update the game objects, draw
   #them, and return False.
   #This is an example update function - replace it.
   #- center is a list containing the x and y int coords
   #of the center of a circle
   #- surface is the pygame.Surface object for the window
   erasecolor=pygame.Color('black')
   if False: # check if the game is over
      return True
   else: # continue the game
      surface.fill(erasecolor)

      moveDot(surface, color1, center1, radius1)
      moveDot(surface, color2, center2, radius2)
      pygame.draw.circle(surface,color1,center1,radius1,0,0)
      pygame.draw.circle(surface,color2,center2,radius2,0,0)
      return False



def moveDot(surface,center,radius,speed):
   size=surface.get_size()
   for coord in range(0,2):
      center[coord]=center[coord]+speed[coord]
      if center [coord]<radius:
         speed[coord]=-speed[coord]
      if center[coord]+radius>size(coord):
         speed[coord]=-speed[coord]
main()