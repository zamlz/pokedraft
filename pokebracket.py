from pokedex import *
from random import *

class player(object):
	def __init__(self):
		self.isPlayer = True
		self.isBalance = True
		self.playerLeft = None
		self.playerRight = None
	
	def printInfo(self):
		print self.isPlayer
		print self.isBalance
		print self.playerLeft
		print self.playerRight


