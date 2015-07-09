from pokedex import *
from random import *

# Status used by player class object
PLAYER = 0
BALANCED = 1
UNBALANCED = -1

# the class player
class player(object):
	# status = tells whether the node is a player node or a balanced node or unbalanced node
	# pID is player ID of player
	# playerLeft is the left player of the node(if it exists)
	# playerRight is the right player of the node (if it exists)

	# intialization of player object. will always set status as PLAYER
	def __init__(self,pID):
		self.status = PLAYER
		self.pID = pID
		self.playerLeft = None
		self.playerRight = None
	
	def addPlayer(self,pID):
		if self.playerLeft.status == PLAYER:
			temp = player(0)
			temp.status = BALANCED
			temp.playerLeft = self.playerLeft
			temp.playerRight = player(pID)
			self.playerLeft = temp

		elif self.playerRight.status == PLAYER:
			temp = player(0)
			temp.status = BALANCED
			temp.playerLeft = self.playerRight
			temp.playerRight = player(pID)
			self.playerRight = temp

		elif self.status == BALANCED:
			self.playerLeft.addPlayer(pID)

		else:
			self.playerRight.addPlayer(pID)

		# After it does its recursive stuff, check the status 
		if self.playerLeft.status == self.playerRight.status:
			self.status = BALANCED
		else: 
			self.status = UNBALANCED


	def showPlayerTree(self, counter = 0):
		if self.playerLeft != None:
			self.playerLeft.showPlayerTree(counter + 1)
			
		for i in range(counter):
			print "\t",
		print "STATUS: " + str(self.status)
		
		for i in range(counter):
			print "\t",
		print "PID: " + str(self.pID)
		
		if self.playerRight != None:
			self.playerRight.showPlayerTree(counter + 1)
		

# this is the function that will create a bracket of num size(will alway one of size 2 since that is the default size)
def createBracket(num):
	bracket = player(0)	
	bracket.status = BALANCED
	bracket.playerLeft = player(1)
	bracket.playerRight = player(2)
	if num > 2:
		for i in range(num-2):
			bracket.addPlayer(i+3)
	return bracket


