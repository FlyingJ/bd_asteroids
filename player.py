import pygame

import constants as const

from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

	def __init__(self, x, y):
		super().__init__(x, y, const.PLAYER_RADIUS)

		self.rotation = 0
		self.shot_cooldown_timer = 0

	# in the player class
	def triangle(self):
	    forward = pygame.Vector2(0, 1).rotate(self.rotation)
	    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
	    a = self.position + forward * self.radius
	    b = self.position - forward * self.radius - right
	    c = self.position - forward * self.radius + right
	    return [a, b, c]

	def draw(self, screen):
		try:
			pygame.draw.polygon(
				screen,
				"white",
				self.triangle(),
				2)
		except TypeError as e:
			print(e)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * const.PLAYER_SPEED * dt

	def rotate(self, dt):
		self.rotation += const.PLAYER_TURN_SPEED * dt

	def shoot(self):
		if self.shot_cooldown_timer <= 0:
			shot = Shot(self.position.x, self.position.y)
			shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * const.PLAYER_SHOOT_SPEED
			self.shot_cooldown_timer = const.PLAYER_SHOOT_COOLDOWN

	def update(self, dt):
		self.shot_cooldown_timer -= dt

		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(dt)
		if keys[pygame.K_d]:
			self.rotate(-dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

