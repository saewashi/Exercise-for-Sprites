#!/usr/bin/env python
'''

For every line, please add a comment describing what it does.

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL) # This is providing a congfiguration of logging, to say the program has a critical error.
logger = logging.getLogger(__name__) # This is getting the logger name.

screen_size = (800,600) # This is setting the screen size/resolution of the computer.
FPS = 60 # This is Frames Per Second, which ic set to 60 so that the frame runs for 60 seconds over and over
red = (255,0,0) # This is the colors that will be  used in the program.
black = (0,0,0) # This is the second color that will be used in the program.

class Block(pygame.sprite.Sprite): # This is declaring a class block, which is getting the Sprites from pygame.
	def __init__(self, position, direction): # This is initalizing self, the postion of the sprite, and the direction.
		pygame.sprite.Sprite.__init__(self) # This is initalizing the Sprite.
		self.image = pygame.Surface((50, 50)) # This is setting the surface image of the sprite.
		self.image.fill(red) # this is filling the image with the color red.
		self.rect = self.image.get_rect() # this is getting the shape of the image.
		(self.rect.x,self.rect.y) = position # this is setting thr position of the sprite.
		self.direction = direction # This is using self to set another set of directions

	def update(self): # This is to update the program
		(dx,dy) = self.direction # this is getting the directions of the sprite
		self.rect.x += dx # This is getting one direction of the rect
		self.rect.y += dy # this is getting the y rect direction
		(WIDTH,HEIGHT) = screen_size # This is setting the width and height to the screen_size.
		if self.rect.left > WIDTH: # This is creating an if statement for the Width if the rect left is greater.
			self.rect.right = 0 # this is setting the rect right equal to 0
		if self.rect.right < 0: # this is an if statement if the rect right is less than 0
			self.rect.left = WIDTH # this is stating that rect.left equals width
		if self.rect.top > HEIGHT: # This is another if statement saying if the rect top is greater than height
			self.rect.bottom = 0 # This is setting rect bottom equal to 0
		if self.rect.bottom < 0: # This is an if statement saying if rect bottom is less than 0
			self.rect.top = HEIGHT # This is setting rect top equal to height


def main(): # This is defining the main function
	pygame.init() # This is initalzing pygame
	screen = pygame.display.set_mode(screen_size) # this is setting the pygame display to the screen_size
	clock = pygame.time.Clock() # this is the pygame clock, for mmaking sure the program ticks for the FPS

	blocks = pygame.sprite.Group() # this is setting blocks eual to the Sprite groups
	block = Block((200,200),(-1,1)) # This is setting the color or size of the block?
	blocks.add(block) # this is adding an additional block.

	while True: # This is creating a while loop for true
		clock.tick(FPS) # This is setting the clock to tick for the FPS that was set earlier in the programming
		screen.fill(black) # this is to fill the screen with a black image

		for event in pygame.event.get(): # this is creating a for loop, and getting the pygame event.
			if event.type == pygame.QUIT: # this is an if statement that is equal to quiting the pygame program.
				pygame.quit() # quits the pygame program if the user exits
				sys.exit(0) # closes the program enirely on the system, so that it stops running

		blocks.update() # This is updating the blocks
		blocks.draw(screen) # this is drawing the block on the screen
		pygame.display.flip() # this is what I call the Mirror Effect, where the display is flipped to show everything on screen, without flashing, etc

if __name__ == '__main__':
	main()
	# This is calling main, so that others can manipulate the program, without changing the whole program itself.
