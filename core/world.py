import pygame as pg



class Object :
	def __init__ (self, name, pos) :
		self.img = pg.image.load(f'assets/textures/objects/{name}.png').convert_alpha()

		self.pos = pos


	def render (self, frame) :
		frame.blit(self.img, self.pos)