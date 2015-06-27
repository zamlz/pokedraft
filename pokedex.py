# Made for pytohn 2.7
import os

class pokemon(object):
	
	# pokeNo = pokemon ID number (integer) 
	# pokeName = pokemon name (String)
	# pokeTier = pokemon tier (String)
	# pokeType = pokemon type (String)
	# pokeIsMega = Does it have mega? (boolean)
	# pokeInfo = Any information on the pokemon (String)
	# pokeAbility = Any abilities this pokemon has (String)
	# pokeStat = Stats of the pokemon (list of integers)
	# pokeRules = Any addition pokemon specific rules for Draft (String)
	
	def __init__(self, pokeNo, pokeName, pokeTier, pokeType, pokeIsMega, pokeInfo, pokeAbility, pokeStat, pokeRules):
		self.pokeNo = pokeNo
		self.pokeName = pokeName
		self.pokeTier = pokeTier
		self.pokeType = pokeType
		self.pokeIsMega = pokeIsMega
		self.pokeInfo = pokeInfo
		self.pokeAbility = pokeAbility
		self.pokeStat = pokeStat
		self.pokeRules = pokeRules

	# Method to get full detailed info on self
	def getDetailPokeInfo(self):
		clearScreen()
		print "\nPokemon DexNo: %d\nPokemon Name : %sPokemon Tier : %sPokemon Type :" % (self.pokeNo, self.pokeName, self.pokeTier),
		for pType in self.pokeType:
			print pType,

		print "\nDescription: "
		print self.pokeInfo
		
		if self.pokeIsMega:
			print "Mega-Status:\nThis pokemon does have a Mega-Evolution."
		else:
			print "Mega-Status:\nThis pokemon does not have a Mega-Evolution"
		
		print "\nAbilities:",
		for ability in self.pokeAbility:
			print ability,
		
		print "\nStats:"
		print "\tHP  - %d" % (int(self.pokeStat[0]))
		print "\tAtk - %d" % (int(self.pokeStat[1]))
		print "\tDef - %d" % (int(self.pokeStat[2]))
		print "\tSpA - %d" % (int(self.pokeStat[3]))
		print "\tSpD - %d" % (int(self.pokeStat[4]))
		print "\tSpe - %d" % (int(self.pokeStat[5]))
		
		print "\nAdditional Rules: %s" % (self.pokeRules)
		raw_input("Press Enter to go back.")
		clearScreen()


class PokeDex(object):
	
	# pokelist is a big list of objects of class pokemon.
	pokeList = []
	#Attributes here
	Types = []
	Tiers = []
	Abilities = []
	# tiers for gen6...
	gen6OU = []
	gen6BL = []
	gen6UU = []

	# intialization of pokedex reads from a file called pokeDB
	def __init__(self):
		self.DexDBload()

	# SETTINGS FUNCTION
	# To append new pokemon to the end of the database. Only for creating the database purposes...
	def DexDBappend(self):
		cont = True
		condition = 'y'
		f = open("pokeDB","a")

		while cont:
			pokename = str(raw_input("Enter the pokemon name: "))
			pokeno = str(raw_input("Enter the pokemon dex number: "))
			poketier = str(raw_input("Enter pokemon Tier: "))
			poketype = str(raw_input("Enter pokemon type: "))
			pokemega = str(raw_input("Enter pokemon mega boolean: "))
			pokeinfo = str(raw_input("Enter Pokemon Info: "))
			pokeability = str(raw_input("Enter pokemon ability: "))
			pokestat = str(raw_input("Enter pokemon stats: "))
			pokerule = str(raw_input("Enter pokemon special rules: "))
			condition = str(raw_input("Do you wish to save this info (y/n/x): "))
			while condition!='y' and condition!='n' and condition!='x':
				condition = str(raw_input("Sorry I did not catch that (y/n/x): "))
			if condition == 'x':
				cont = False
			elif condition == 'n':
				continue
			else:
				f.write(str(pokeno)+"\n")
				f.write(str(pokename)+"\n")
				f.write(str(poketier)+"\n")
				f.write(str(poketype)+"\n")
				f.write(str(pokemega)+"\n")
				f.write(str(pokeinfo)+"\n")
				f.write(str(pokeability)+"\n")
				f.write(str(pokestat)+"\n")
				f.write(str(pokerule)+"\n")
		f.close()
		self.DexDBload()

	# SETTINGS FUNCTION
	# This will modify existing entries of the database...
	def DexDBmod(self):
		pass

	# SETTINGS FUNCTION
	# This is to load the database.
	def DexDBload(self):
		self.pokeList = []
		# The data types we are going to use
		pokeNo = 0 
		pokeName = ""
		pokeTier = ""
		pokeType = ""
		pokeIsMega = False
		pokeInfo = ""
		pokeAbility = ""
		pokeStat = []
		pokeRules = ""
		# a temp for intialization purposes
		pokeTemp = ""
		pokeTemp2 = []

		counter = 0
		pokeDB = open("pokeDB","r")

		for line in pokeDB:
			print line
			if counter == 0:
				pokeNo = int(line)
				counter+=1
			
			elif counter == 1:
				pokeName = line
				counter+=1
			
			elif counter == 2:
				pokeTier = line
				self.attrAdd(pokeTier,2)
				counter+=1	
			
			elif counter == 3:
				pokeType = line.split()
				for j in pokeType:
					self.attrAdd(j,0)
				counter+=1
			
			elif counter == 4:
				if line != "True\n":
					pokeIsMega = False
				else:
					pokeIsMega = True
				counter+=1
			
			elif counter == 5:
				pokeInfo = line
				counter+=1
			
			elif counter == 6:
				pokeAbility = line.split()
				for k in pokeAbility:
					self.attrAdd(k,1)
				counter+=1
			
			elif counter == 7:
				pokeStat = line.split()
				counter+=1
			
			elif counter == 8:
				pokeRules = line
				counter = 0
				pokemonTemp = pokemon(pokeNo, pokeName, pokeTier, pokeType, pokeIsMega, pokeInfo, pokeAbility, pokeStat, pokeRules)
				self.pokeList.append(pokemonTemp)
				print "SUCCESS"
		pokeDB.close()

	def attrAdd(self, temp, i):
		if i == 0:
			for item in self.Types:
				if item == temp:
					break
			else:
				self.Types.append(temp)
		elif i == 1:
			for item in self.Abilities:
				if item == temp:
					break
			else:
				self.Abilities.append(temp)
		else:
			for item in self.Tiers:
				if item == temp:
					break
			else:
				self.Tiers.append(temp)
	
	# Method to get a full detailed info on pokemon number i
	def getDexInfo(self):
		cont = True
		while cont:
			clearScreen()
			try:
				i = str(raw_input("\nEnter a pokemon Dex number: "))
				# code to check if input string is a int somehow...
				self.pokeList[int(i)-1].getDetailPokeInfo()
				cont = False
			except ValueError:
				raw_input("\nThats not a number")

	# This will list all the pokemon in the pokedex( has page turns)
	def pokeListing(self,pList):
		pass

	# This function will give a listing of pokemon of a specific type/tier/stat/isMega/Ability
	def attrSearch(self):
		while True:
			clearScreen()
			print "\n\nPokeDex Attribute Search"
			print "\n Choose an Attribute"
			print "\n\t1. Pokemon Type"
			print "\t2. Pokeomn Tier"
			print "\t3. Pokemon Ability"
			print "\t4. Quit (or x)"
			
			choice = str(raw_input("\n>>> "))
			# do remove these for loops and create a proper listing function....
			if choice == "1":
				self.attrListing(self.Types,1)	
			elif choice == "2":
				self.attrListing(self.Tiers,2)
			elif choice == "3":
				self.attrListing(self.Abilities,3)	
			elif choice == "4" or choice == "x" or choice == "X":
				break
			else:
				raw_input("\nNot a valid option.")	

	# Currenctly crude version of the attribute listing....
	def attrListing(self, Attr,i):
		n=1
		while True:
			clearScreen()
			print "\n\nSearch by ",
			if i == 1:
				print "Type\n"
			elif i ==2:
				print "Tier\n"
			elif i ==3:
				print "Ability\n"
			for item in Attr:
				print str(n)+". "+item
				n+=1
			choice = int(raw_input("\n>>> "))
			temp = []
			for item in self.pokeList:
				if (item.pokeType == Attr[choice-1] and i == 1) or (item.pokeTier == Attr[choice-1] and i == 2) or (item.pokeAbility == Attr[choice-1] and i == 3):
					temp.append(item)
			#instead of a for loop to print the pokemon name, we have to sent the list to pokeListing...
			for item in temp:
				print item.pokeName
			raw_input("")
			break



	# This function will try to do a standard search based on a user inputed string and will return a list
	# of pokemon that have similar names to that string.
	def pokeSearch(self):
		pass

	# This the main menu of the pokedex
	def mainMenu(self):
		while True:
			clearScreen()
			print "\nWelcome to The PokeDex!"
			print "\n\t\tBy zAMLz"
			print "\n Please choose an option."
			print "\n\t1. View Pokemon List"
			print "\t2. Enter a DexNo"
			print "\t3. Search by Attribute"
			print "\t4. Search"
			print "\t5. Quit (or x)"
			
			choice = str(raw_input("\n>>> "))

			if choice == "1":
				self.pokeListing()
			elif choice == "2":
				self.getDexInfo()
			elif choice == "3":
				self.attrSearch()
			elif choice == "4":
				self.pokeSearch()
			elif choice == "5" or choice == "x" or choice == "X":
				break
			else:
				raw_input("\nNot a valid option.")	


def clearScreen():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')
