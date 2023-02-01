import pygame as pg

from .sound import sounds
from .controlls import controlls



class Player :
	def __init__ (self) :
		self.img = [
			pg.image.load('assets/textures/player/idle.png').convert_alpha(),
			pg.image.load('assets/textures/player/walk_0.png').convert_alpha(),
			pg.image.load('assets/textures/player/walk_1.png').convert_alpha()]

		self.anim = {'walk': 0}

		self.pos = [0, 0]
		self.speed = 0.5

		self.level = 0
		


	def update (self, dt) :
		keys = pg.key.get_pressed()

		if keys[pg.K_w] : self.pos[1] -= self.speed
		if keys[pg.K_s] : self.pos[1] += self.speed
		if keys[pg.K_a] : self.pos[0] -= self.speed
		if keys[pg.K_d] : self.pos[0] += self.speed


	def animate (self) :
		keys = pg.key.get_pressed()

		if keys[controlls['up']] or keys[controlls['down']] or keys[controlls['left']] or keys[controlls['right']] :
			self.anim['walk'] += 1

			if self.anim['walk'] >= 0 and self.anim['walk'] < 20 : img = self.img[1]
			elif self.anim['walk'] >= 20 : img = self.img[2]

			if self.anim['walk'] in [0, 20, 30] : sounds['player']['walk'].play()

			if self.anim['walk'] >= 30 : self.anim['walk'] = 0

		else : img = self.img[0]


		return img


	def render (self, frame) :
		frame.blit(self.animate(), self.pos)