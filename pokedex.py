# Made for pytohn 2.7

class pokemon(object):
	
	# pokeNo = pokemon ID number (integer) 
	# pokeName = pokemon name (String)
	# pokeIsMega = Does it have mega? (boolean)
	# pokeInfo = Any information on the pokemon (String)
	# pokeAbility = Any abilities this pokemon has (String)
	# pokeStat = Stats of the pokemon (list of integers)
	# pokeRules = Any addition pokemon specific rules for Draft (String)
	
	def __init__(self, pokeNo, pokeName, pokeIsMega, pokeInfo, pokeAbility, pokeStat, pokeRules):
		self.pokeNo = pokeNo
		self.pokeName = pokeName
		self.pokeIsMega = pokeIsMega
		self.pokeInfo = pokeInfo
		self.pokeAbility = pokeAbility
		self.pokeStat = pokeStat
		self.pokeRules = pokeRules

	# Method to get full detailed info on self
	def getDetailPokeInfo(self):
		print "\nPokemon Name: %s\nPokemon DexNo: %d\n" % (self.pokeName, self.pokeNo)
		print "Description: "
		print self.pokeInfo
		if self.pokeIsMega:
			print "Mega-Status:\nThis pokemon does have a Mega-Evolution."
		else:
			print "Mega-Status:\nThis pokemon does not have a Mega-Evolution"
		print "\nAbilities: %s" % (self.pokeAbility)
		print "Stats:"
		print "\tHP  - %d" % (int(self.pokeStat[0]))
		print "\tAtk - %d" % (int(self.pokeStat[1]))
		print "\tDef - %d" % (int(self.pokeStat[2]))
		print "\tSpA - %d" % (int(self.pokeStat[3]))
		print "\tSpD - %d" % (int(self.pokeStat[4]))
		print "\tSpe - %d" % (int(self.pokeStat[5]))
		print "\nAdditional Rules: %s" % (self.pokeRules)
		raw_input("\nPress Enter to go back.")


class PokeDex(object):
	
	# pokelist is a big list of objects of class pokemon.
	pokeList = []
	
	# tiers for gen6...
	gen6GlobalBan = [] 
	gen6OU = []
	gen6BL = []
	gen6UU = []

	# intialization of pokedex reads from a file called pokeDB
	def __init__(self):
		
		# The data types we are going to use
		pokeNo = 0 
		pokeName = ""
		pokeIsMega = False
		pokeInfo = ""
		pokeAbility = ""
		pokeStat = []
		pokeRules = ""
		# a temp for intialization purposes
		pokeTemp = ""
		pokeTemp2 = []

		with open("pokeDB","r") as pokeDB:
			for i in range(2):
				pokeNo = int(pokeDB.readline())
				pokeName = pokeDB.readline()
				
				pokeTemp = pokeDB.readline()
				if pokeTemp != "True":
					pokeIsMega = False
				else:
					pokeIsMega = True
				
				pokeInfo = pokeDB.readline()
				pokeAbility = pokeDB.readline()
				
				pokeTemp = pokeDB.readline()
				pokeStat = pokeTemp.split()

				pokeRules = pokeDB.readline()

				pokemonTemp = pokemon(pokeNo, pokeName, pokeIsMega, pokeInfo, pokeAbility, pokeStat, pokeRules)
				self.pokeList.append(pokemonTemp)


	# Method to get a full detailed info on pokemon number i
	def getInfo(self,i):
		self.pokeList[i].getDetailPokeInfo()		



def mainmenu():
	# print "\nWelcome to Pokemon Draft"
	# print "\n\t\tBy zAMLz"
	# pokeDex.getInfo(0)
	pokeDex.getInfo(1)


# start of the program #
########################

pokeDex = PokeDex() 	# Intializes a global pokedex
mainmenu()			# Start the mainmenu prompt