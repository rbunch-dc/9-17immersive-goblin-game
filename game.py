# 1. Include pygame
# Include pygame which we got from pip
import pygame

# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()

# 3. Create a screen with a particular size
# the screen size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('background.png')

# 4. Create a game loop (while)
# Create a boolean for whether the game should be going or not
game_on = True
while game_on:
	# we are inside the main game loop.
	# it will keep running, as long as our bool is true
	# 5. Add a quit event (Python needs an escape)
	# Pygame comes with an event loop! (sort of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			# the user clicked the red x in the top left
			game_on = False

	# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you watn you to draw it
	pygame_screen.blit(background_image, [0,0])

	# 7. Repeat 6 over and over over...
	pygame.display.flip()
