import pygame # Import pygame library
import sys # Import system library

pygame.init() # Initialize graphics engine

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_DIMENSION = (SCREEN_WIDTH, SCREEN_HEIGHT) # Storing the screen dimensions in a tuple

image_file = pygame.image.load("image.png") # Load our image file stored on the computer

screen = pygame.display.set_mode(SCREEN_DIMENSION) # Create screen object 
pygame.display.set_caption("Screen Title") # Setting the screen title

while True:
    for event in pygame.event.get(): # Get pygame events with a loop
        if event.type == pygame.QUIT: # We test for quit event
            pygame.quit() # Quit pygame
            sys.exit() # Close application
        
        screen.fill("black") # Fill screen with the color black

        screen.blit(image_file, (80, 80)) # Draw the image on the selected screen's x: 80 and y:80 pos

        pygame.display.update() # Update the screen