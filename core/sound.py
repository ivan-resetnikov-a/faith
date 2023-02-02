import pygame as pg
pg.mixer.init()

print('=== LOADING SOUNDS ===')



class Dummy :
	def play (self) :
		print('Error occured while trying to load sound!')


def loadSound (path, vol=0.2) :
	try :
		print(f'[ ] Loading file {path}', end='\r')
		sound = pg.mixer.Sound('assets/sounds/'+path)
		sound.set_volume(vol)
		print(f'[Y] Loading file {path}')
		return sound
	except Exception as error:
		print(f'[X] Error loading sound file {path}: {error}')
		return Dummy()


sounds = {
	'player' : {
		'walk' : loadSound('player_walk.wav', 0.15),
		'show cross' : loadSound('show_cross.wav', 0.2)
	}
}