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
		print "\nPokemon DexNo: %d\nPokemon Name : %s\nPokemon Tier : %s\nPokemon Type :" % (self.pokeNo, self.pokeName, self.pokeTier),
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

	def modInfo(self):
		pokeNo = self.pokeNo
		pokeName = self.pokeName
		pokeTier = self.pokeTier
		pokeType = self.pokeType
		pokeIsMega = self.pokeIsMega
		pokeInfo = self.pokeInfo
		pokeAbility = self.pokeAbility
		pokeStat = self.pokeStat
		pokeRules = self.pokeRules
		temp = pokemon(pokeNo, pokeName, pokeTier, pokeType, pokeIsMega, pokeInfo, pokeAbility, pokeStat, pokeRules)
		while True:
			clearScreen()
			print "\n\nSet to Modify pokemon: %s\n" % (temp.pokeName)
			print "\n Please choose a field to modify."
			print "\n\t1. Pokemon Name"
			print "\t2. Pokemon Dex Number"
			print "\t3. Pokemon Tier"
			print "\t4. Pokemon Type"
			print "\t5. Pokemon Mega Status"
			print "\t6. Pokemon Info"
			print "\t7. Pokemon Ability"
			print "\t8. Pokemon Stat Spread"
			print "\t9. Pokemon Additional Rules"
			print "\t------------------------------\n\t10. Preview Changes"
			print "\t11. Save Changes and Quit"
			print "\t12. Discard Changes and Quit"
			
			choice = str(raw_input("\n>>> "))

			if choice == "1":
				temp.pokeName = str(raw_input("\nPlease Enter the pokemon name: "))
			elif choice == "2":
				try:
					temp.pokeNo = int(raw_input("Please Enter the pokemon dex number: "))
				except ValueError:
					raw_input("\nThat is not a number")
			elif choice == "3":
				temp.pokeTier = str(raw_input("\nPlease Enter the pokemon tier: "))
			elif choice == "4":
				temp.pokeType = str(raw_input("\nPlease Enter the pokemon type(s): ")).split()
			elif choice == "5":
				tempBool = str(raw_input("\nPlease Enter the pokemon mega status: "))
				if tempBool == "True":
					temp.pokeIsMega = True
				else:
					temp.pokeIsMega = False
			elif choice == "6":
				temp.pokeInfo = str(raw_input("\nPlease Enter the pokemon info: "))
				temp.pokeInfo+="\n"
			elif choice == "7":
				temp.pokeAbility = str(raw_input("\nPlease Enter the pokemon Abilities: ")).split()
			elif choice == "8":
				temp.pokeStat = str(raw_input("\nPlease Enter the pokemon stat spread: ")).split()
			elif choice == "9":
				temp.pokeRules = str(raw_input("\nPlease Enter the pokemon additional rules: "))
				temp.pokeRules+="\n"
			elif choice == "10":
				temp.getDetailPokeInfo()
			elif choice == "11" or choice == "s" or choice == "S":
				self.pokeNo = temp.pokeNo
				self.pokeName = temp.pokeName
				self.pokeTier = temp.pokeTier
				self.pokeType = temp.pokeType
				self.pokeIsMega = temp.pokeIsMega
				self.pokeInfo = temp.pokeInfo
				self.pokeAbility = temp.pokeAbility
				self.pokeStat = temp.pokeStat
				self.pokeRules = temp.pokeRules
				break
			elif choice == "12" or choice == "x" or choice == "X":
				break
			else:
				raw_input("\nNot a valid option.")

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
		self.pokeListing(self.pokeList,True)
		self.DexDBwrite()
		self.DexDBload()

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
			#print line
			if counter == 0:
				pokeNo = int(line)
				counter+=1
			
			elif counter == 1:
				pokeName = line.split()[0]
				counter+=1
			
			elif counter == 2:
				pokeTier = line.split()[0]
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
				# print "SUCCESS"
		pokeDB.close()

	# SETTINGS FUNCTION
	# This will write what is stored in pokeList back into pokeDB
	def DexDBwrite(self):
		f = open("pokeDB","w")
		
		for poke in self.pokeList:
			temp = ""
			f.write(str(poke.pokeNo)+"\n")
			f.write(str(poke.pokeName)+"\n")
			f.write(str(poke.pokeTier)+"\n")
			
			for item in poke.pokeType:
				temp = temp + item + " "
			f.write(str(temp)+"\n")

			if poke.pokeIsMega:
				f.write("True\n")
			else:
				f.write("False\n")
			
			f.write(str(poke.pokeInfo))

			temp = ""
			for item in poke.pokeAbility:
				temp = temp + item + " "
			f.write(str(temp)+"\n")
			
			temp = ""
			for item in poke.pokeStat:
				temp = temp + item + " "
			f.write(str(temp)+"\n")

			f.write(str(poke.pokeRules))
		f.close()


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
				i = int(raw_input("\nEnter a pokemon Dex number: "))
				if i >= len(self.pokeList) or i <= 0:
					raw_input("\nThat pokemon Dex number does not exist.")
				else:
					self.pokeList[i-1].getDetailPokeInfo()
					cont = False
			except ValueError:
				raw_input("\nThats not a number")

	# This will list a list of pokemon in the pokedex with a viewable and useable ui
	def pokeListing(self,pList,allowModify):

		pageHead = 0
		pageCur = 1
		cont = True

		pages = len(pList)/32
		if len(pList)%32 != 0:
			pages+=1

		while cont:
			clearScreen()
			if allowModify == False:
				print "\nPokemon Listing\n"
			else:
				print "\nPokemon Listing (Modify)\n"
			
			for i in range(8):
				pageLine = ""
				if pageHead+i < len(pList):
					print ("\n%3d. %-12s") % (pageHead+i+1, pList[pageHead+i].pokeName.split()[0]),
				if pageHead+i+8 < len(pList):
					print ("%3d. %-12s") % (pageHead+i+9, pList[pageHead+i+8].pokeName.split()[0]),
				if pageHead+i+16 < len(pList):
					print ("%3d. %-12s") % (pageHead+i+17, pList[pageHead+i+16].pokeName.split()[0]),
				if pageHead+i+24 < len(pList):
					print ("%3d. %-12s") % (pageHead+i+25, pList[pageHead+i+24].pokeName.split()[0]),
			print "\n\n Previous Page(< or ,)		Next Page(> or .)		Quit(x)"
			print "\nPlease Enter a pokemon number or a command."
			choice = str(raw_input("\n ~ "))
			if choice == "<" or choice == ",":
				if pageCur-1 <= 0:
					raw_input("\nA previous page does not exist.")
				else:
					pageCur-=1
					pageHead-=32
			elif choice == ">" or choice == ".":
				if pageCur+1 > pages:
					raw_input("\nA next page does not exist.")
				else:
					pageCur+=1
					pageHead+=32
			elif choice == "x" or choice == "X":
				cont = False
			else:
				try:
					ch = int(choice)
					if ch > len(pList) or ch <= 0:
						raw_input("\nThat pokemon Dex number does not exist.")
					else:
						if allowModify == False:
							pList[ch-1].getDetailPokeInfo()
						else:
							self.pokeList[ch-1].modInfo()
				except ValueError:
					raw_input("\nThat's not a valid input!")



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

	# The purpose of this function is that after the user has chosen the specific attribute, it will search through the list of pokemon
	# and create of list of pokemon that share that attribute.
	def attrSearchPhaseTwo(self,choice,search):	
		nList = []
		for item in self.pokeList:
			if search == 1:
				temp = item.pokeType
			elif search == 2:
				temp = item.pokeTier.split()
			elif search == 3:
				temp = item.pokeAbility
			for ty in temp:
				if ty == choice:
					nList.append(item)
					break
		nList = sorted(nList)
		self.pokeListing(nList,False)

	# Different listings for all attribute
	def attrListing(self,pList,search):

		pList = sorted(pList)
		pageHead = 0
		pageCur = 1
		cont = True

		pages = len(pList)/32
		if len(pList)%32 != 0:
			pages+=1

		while cont:
			clearScreen()
			print "\nAttribute Listing: \n",
			if search == 1:
				print "Types"
			elif search ==2:
				print "Tiers"
			else:
				print "Abilities"
			
			for i in range(8):
				pageLine = ""
				if pageHead+i < len(pList):
					print ("\n%3d. %-12s") % (pageHead+i+1, pList[pageHead+i].split()[0]),
				if pageHead+i+8 < len(pList):
					print ("%3d. %-12s") % (pageHead+i+9, pList[pageHead+i+8].split()[0]),
				if pageHead+i+16 < len(pList):
					print ("%3d. %-12s") % (pageHead+i+17, pList[pageHead+i+16].split()[0]),
				if pageHead+i+24 < len(pList):
					print ("%3d. %-12s") % (pageHead+i+25, pList[pageHead+i+24].split()[0]),
			print "\n\n Previous Page(< or ,)		Next Page(> or .)		Quit(x)"
			
			if search == 1:
				print "\nPlease Enter a Type or a command."
			elif search ==2:
				print "\nPlease Enter a Tier or a command."
			else:
				print "\nPlease Enter a Ability or a command."

			choice = str(raw_input("\n ~ "))
			if choice == "<" or choice == ",":
				if pageCur-1 <= 0:
					raw_input("\nA previous page does not exist.")
				else:
					pageCur-=1
					pageHead-=32
			elif choice == ">" or choice == ".":
				if pageCur+1 > pages:
					raw_input("\nA next page does not exist.")
				else:
					pageCur+=1
					pageHead+=32
			elif choice == "x" or choice == "X":
				cont = False
			else:
				try:
					ch = int(choice)
					if ch > len(pList) or ch <= 0:
						raw_input("\nThat option does not exist.")
					else:
						self.attrSearchPhaseTwo(pList[ch-1].split()[0],search)
				except ValueError:
					raw_input("\nThat's not a valid input!")

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
				self.pokeListing(self.pokeList,False)
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
