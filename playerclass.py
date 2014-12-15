import pygame, math

class Player():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
		self.place(pos)
		self.changed = False
		self.didBounceX = False
		self.didBounceY = False
		self.living = True
		self.facing = "up"
		self.maxSpeed = 10
	
	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		self.didBounceX = False
		self.didBounceY = False
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
		
	def move(self):
		self.rect = self.rect.move(self.speed)
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.pos = self.place(1,70)
			if self.rect.left < 0 or self.rect.right > width:
				self.pos = self.place(1023,70)
				self.didBounceX = True
				#print "hit xWall"
		
							
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
				
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0

		
		
		
		
		
