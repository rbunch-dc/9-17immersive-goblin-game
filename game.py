# 1. Include pygame
# Include pygame which we got from pip
import pygame

# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()

# 3. Create a screen with a particular size
# the screen size MUST be a tuple
screen_size = (512,480)
# Actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)
# Set a pointless caption
pygame.display.set_caption("Goblin Chase")
# set up a var with our image
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')

# 8. Set up the hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

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
		elif event.type == pygame.KEYDOWN:
			# print "User pressed a key!"
			if event.key == keys['up']:
				# user pressed up!!
				# hero['y'] -= hero['speed']
				keys_down['up'] = True
			elif event.key == keys['down']:
				# hero['y'] += hero['speed']
				keys_down['down'] = True
			elif event.key == keys['left']:
				# hero['x'] -= hero['speed']
				keys_down['left'] = True
			elif event.key == keys['right']:
				# hero['x'] += hero['speed']
				keys_down['right'] = True

	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

	# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you watn you to draw it
	pygame_screen.blit(background_image, [0,0])
	pygame_screen.blit(hero_image, [hero['x'],hero['y']])

	# 7. Repeat 6 over and over over...
	pygame.display.flip()
