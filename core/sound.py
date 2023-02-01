import pygame as pg
pg.mixer.init()


def loadSound (path, vol=0.2) :
	sound = pg.mixer.Sound('assets/sounds/'+path)
	sound.set_volume(vol)
	return sound


sounds = {
	'player' : {
		'walk' : loadSound('player_walk.wav', 0.07)
	}
}