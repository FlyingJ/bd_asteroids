import pygame

import constants as const

from circleshape import CircleShape

class Shot(CircleShape):

	def __init__(self, x, y):
		super().__init__(x, y, const.SHOT_RADIUS)

	def draw(self, screen):
		try:
			pygame.draw.circle(
				screen,
				color="yellow",
				center=self.position,
				radius=self.radius,
				width=2
			)
		except TypeError as e:
			print(e)

	def move(self, dt):
		self.position += self.velocity * dt

	def update(self, dt):
		self.move(dt)