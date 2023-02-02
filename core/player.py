import pygame as pg

from .sound import sounds
from .controlls import controlls



class Player :
	def __init__ (self) :
		self.img = [
			pg.image.load('assets/textures/player/idle.png').convert_alpha(),
			pg.image.load('assets/textures/player/walk_0.png').convert_alpha(),
			pg.image.load('assets/textures/player/walk_1.png').convert_alpha(),
			pg.image.load('assets/textures/player/show_cross.png').convert_alpha()]

		self.anim = {'walk': 0}

		self.pos = [100, 100]
		self.speed = 0.5

		self.level = 0


	def colliding (self, colliders) :
		colliding = 0

		for collider in colliders :
			if pg.Rect((self.pos[0], self.pos[1]+12, 8, 4)).colliderect(collider) :
				colliding = 1

		return colliding


	def update (self, dt, colliders) :
		keys = pg.key.get_pressed()
		vel = [0, 0]

		if keys[pg.K_w] : vel[1] = -self.speed
		if keys[pg.K_s] : vel[1] =  self.speed
		if keys[pg.K_a] : vel[0] = -self.speed
		if keys[pg.K_d] : vel[0] =  self.speed

		self.pos[0] += vel[0]
		if self.colliding(colliders) : self.pos[0] -= vel[0]
		self.pos[1] += vel[1]
		if self.colliding(colliders) : self.pos[1] -= vel[1]

		if keys[pg.K_e] and self.speed == 0.5 :
			self.speed = 0
			sounds['player']['show cross'].play()
		elif not keys[pg.K_e] :
			self.speed = 0.5


	def animate (self) :
		img = self.img[0]

		keys = pg.key.get_pressed()

		if not keys[pg.K_e] and (keys[controlls['up']] or keys[controlls['down']] or keys[controlls['left']] or keys[controlls['right']]) :
			self.anim['walk'] += 1

			if self.anim['walk'] >= 0 and self.anim['walk'] < 20 : img = self.img[1]
			elif self.anim['walk'] >= 20 : img = self.img[2]

			if self.anim['walk'] in [0, 20, 30] : sounds['player']['walk'].play()

			if self.anim['walk'] >= 30 : self.anim['walk'] = 0

		elif keys[pg.K_e] : img = self.img[3]


		return img


	def render (self, frame) :
		frame.blit(self.animate(), self.pos)