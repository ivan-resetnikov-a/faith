import pygame as pg

import core



class Faith :
	def __init__ (self) :
		# config
		self.size, self.rez = (1000, 800), (250, 200)
		self.title = 'Faith'
		
		self.timeMult = 1
		self.fps = 60

		# window
		self.window = pg.display.set_mode(self.size)
		self.frame  = pg.Surface(self.rez)
		self.clock  = pg.time.Clock()
		pg.display.set_caption(self.title)


	def update (self) :
		self.player.update(self.timeMult, self.colliders)


	def render (self) :
		self.frame.fill((0, 0, 0))
		################
		topObjects = []
		for obj in self.objects :
			if obj.pos[1]+(obj.img.get_height()*0.5) < self.player.pos[1] : obj.render(self.frame)
			else : topObjects.append(obj)

		self.player.render(self.frame)

		[obj.render(self.frame) for obj in topObjects]
		################
		self.window.blit(pg.transform.scale(self.frame, self.size), (0, 0))
		self.clock.tick(self.fps)
		pg.display.flip()


	def run (self) :
		self.onStart()

		self.running = 1
		while self.running :
			for event in pg.event.get() :
				if event.type == pg.QUIT :
					self.running = 0

			self.update()
			self.render()


	def loadLevel (self) :
		content = core.loadFromJSON(f'data/faith/world/{self.player.level}.json')

		self.colliders, self.objects = [], []

		# load object
		[self.objects.append(core.Object(obj['name'], obj['pos'])) for obj in content['objects']]

		# load colliders
		[self.colliders.append(tuple(collider)) for collider in content['colliders']]


	def onStart (self) :
		self.player = core.Player()

		self.loadLevel()



Faith().run()