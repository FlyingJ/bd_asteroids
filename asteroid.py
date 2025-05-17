import pygame
import random

import constants as const

from circleshape import CircleShape

class Asteroid(CircleShape):

	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		try:
			pygame.draw.circle(
				screen,
				color="white",
				center=self.position,
				radius=self.radius,
				width=2
			)
		except TypeError as e:
			print(e)

	def move(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= const.ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		resultant_velocities = [
			const.SPLIT_SPEED_AMP * self.velocity.rotate(random_angle),
			const.SPLIT_SPEED_AMP * self.velocity.rotate(-random_angle)
			]
		resultant_radius = self.radius - const.ASTEROID_MIN_RADIUS

		for velocity in resultant_velocities:
			shard = Asteroid(self.position.x, self.position.y, resultant_radius)
			shard.velocity = velocity

	def update(self, dt):
		self.move(dt)