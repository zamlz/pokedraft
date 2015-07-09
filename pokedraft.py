from pokedex import *
from random import *
from pokebracket import *

pokeDex = PokeDex()

# This is the function for pool draft.
# it has two arguments called isExcl an isSwap which will be used to create a different playing experience.
def poolDraft(isExcl, isSwap):
	while True:
		clearScreen()
		if isExcl:
			print "P/E"
		else:
			if isSwap:
				print "P/U/S"
			else: 
				print "P/U/N"
		print "\nType S to start or type X to quit"
		choice = str(raw_input("\n>>> "))
		if choice == "S" or choice == "s":
			pass
		elif choice == "X" or choice == "x":
			break
		else:
			raw_input("\nNot a valid option.")

# This is the function for booster draft.
# it has two arguments called isExcl an isSwap which will be used to create a different playing experience.
def boostDraft(isExcl,isSwap):
	while True:
		clearScreen()
		if isExcl:
			print "B/E"
		else:
			if isSwap:
				print "B/U/S"
			else: 
				print "B/U/N"
		print "\nType S to start or type X to quit"
		choice = str(raw_input("\n>>> "))
		if choice == "S" or choice == "s":
			pass
		elif choice == "X" or choice == "x":
			break
		else:
			raw_input("\nNot a valid option.")

# the draft menu; all draft options will be shown here
def draftMenu():
	while True:
		clearScreen()
		print "\n\nWelcome to the Draft Menu\n"
		print "\n Please choose an option."
		print "\n\t1. Pool - E"
		print "\t2. Pool - U - N"
		print "\t3. Pool - U - S"
		print "\t4. Booster - E"
		print "\t5. Booster - U - N"
		print "\t6. Booster - U - S"
		print "\t7. Quit (or x)"
		
		choice = str(raw_input("\n>>> "))

		if choice == "1":
			poolDraft(True,False)
		elif choice == "2":
			poolDraft(False,False)
		elif choice == "3":
			poolDraft(False,True)
		elif choice == "4":
			boostDraft(True, False)
		elif choice == "5":
			boostDraft(False,False)
		elif choice == "6":
			boostDraft(False,True)
		elif choice == "7" or choice == "x" or choice == "X":
			break
		else:
			raw_input("\nNot a valid option.")


# The menu to modify the pokemon draft settings. Also accesses pokedex settings. 
def settingsMenu():
	while True:
		clearScreen()
		print "\n\nWelcome to Settings Menu\n\nDO NOT MESS AROUND WITH DevFUNCs UNLESS YOU KNOW WHAT YOU ARE DOING!!!\n"
		print "\n Please choose an option."
		print "\n\t1. Draft options placeholder"
		print "\t2. Draft options placeholder"
		print "\t3. DevFUNCs.DexDBmod"
		print "\t4. DevFUNCs.DexDBappend"
		print "\t5. Quit (or x)"
		
		choice = str(raw_input("\n>>> "))

		if choice == "1":
			pass
		elif choice == "2":
			pass
		elif choice == "3":
			pokeDex.DexDBmod()
		elif choice == "4":
			pokeDex.DexDBappend()
		elif choice == "5" or choice == "x" or choice == "X":
			break
		else:
			raw_input("\nNot a valid option.")	

# the Main menu of the program.
def mainMenu():
	loadSettings()
	while True:
		clearScreen()
		print "\n\nWelcome to \n"
		printTitle()
		print "\n Please choose an option."
		print "\n\t1. Start Pokemon Draft"
		print "\t2. View PokeDex"
		print "\t3. About"
		print "\t4. Settings"
		print "\t5. Quit (or x)"
		
		choice = str(raw_input("\n>>> "))

		if choice == "1":
			draftMenu()
		elif choice == "2":
			pokeDex.mainMenu()
		elif choice == "3":
			about()
		elif choice == "4":
			settingsMenu()
			loadSettings()
		elif choice == "5" or choice == "x" or choice == "X":
			break
		else:
			raw_input("\nNot a valid option.")
	
	clearScreen()
	raw_input("\n\n\t Thank you for using Pokemon Draft!")
	clearScreen()


# The function which loads settings(if i decided to implement more settings besides pokedex)
def loadSettings():
	pass

# Prints the title. Just Artsy style points stuff
def printTitle():
	x = randrange(1,3)
	if x == 1:
		print ";-.      ,                     "
		print "|  )     |                     "
		print "|-'  ,-. | , ,-. ;-.-. ,-. ;-. "
		print "|    | | |<  |-' | | | | | | | "
		print "'    `-' ' ` `-' ' ' ' `-' ' '"                              
		print ",-.              .      "       
		print "|  \          ,- |     "        
		print "|  | ;-. ,-:  |  |-   "         
		print "|  / |   | |  |- |   "          
		print "`-'  '   `-`  |  `-'"           
		print "             -'    "
	elif x == 2:
		print "\n   ___      _                              "
		print "  / _ \___ | | _____ _ __ ___   ___  _ __  "
		print " / /_)/ _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ "
		print "/ ___/ (_) |   <  __/ | | | | | (_) | | | |"
		print "\/    \___/|_|\_\___|_| |_| |_|\___/|_| |_| "
		print "    ___            __ _                    "
		print "   /   \_ __ __ _ / _| |_                  "
		print "  / /\ / '__/ _` | |_| __|                 "
		print " / /_//| | | (_| |  _| |_                  "
		print "/___,' |_|  \__,_|_|  \__|                 "
                           
# The about page. so far... only has a ascii pikachu...                           
def about():
	clearScreen()
	print "quu..__"
	print " $$$b  `---.__"
	print "  \"$$b        `--.                          ___.---uuudP"
	print "   `$$b           `.__.------.__     __.---'      $$$$\"              ."
	print "     \"$b          -'            `-.-'            $$$\"              .'|"
	print "       \".                                       d$\"             _.'  |"
	print "         `.   /                              ...\"             .'     |"
	print "           `./                           ..::-'            _.'       |"
	print "            /                         .:::-'            .-'         .'"
	print "           :                          ::''\\          _.'            |"
	print "          .' .-.             .-.           `.      .'               |"
	print "          : /'$$|           .@\"$\\           `.   .'              _.-'"
	print "         .'|$u$$|          |$$,$$|           |  <            _.-'"
	print "         | `:$$:'          :$$$$$:           `.  `.       .-'"
	print "         :                  `\"--'             |    `-.     \\"
	print "        :##.       ==             .###.       `.      `.    `\\"
	print "        |##:                      :###:        |        >     >"
	print "        |#'     `..'`..'          `###'        x:      /     /"
	print "         \\                                   xXX|     /    ./"
	print "          \\                                xXXX'|    /   ./"
	print "          /`-.                                  `.  /   /"
	print "         :    `-  ...........,                   | /  .'"
	print "         |         ``:::::::'       .            |<    `."
	print "         |             ```          |           x| \ `.:``."
	print "         |                         .'    /'   xXX|  `:`M`M':."
	print "         |    |                    ;    /:' xXXX'|  -'MMMMM:'"
	print "         `.  .'                   :    /:'       |-'MMMM.-'"
	print "          |  |                   .'   /'        .'MMM.-'"
	print "          `'`'                   :  ,'          |MMM<"
	print "            |                     `'            |tbap\\"
	print "             \\                                  :MM.-'"
	print "              \\                 |              .''"
	print "               \\.               `.            /"
	print "                /     .:::::::.. :           /"
	print "               |     .:::::::::::`.         /"
	print "               |   .:::------------\       /"
	print "              /   .''               >::'  /"
	print "              `',:                 :    .'"
	print "  SOURCE:chris.com/ASCII                  "
	raw_input("\nPress Enter to Continue...")

mainMenu()

