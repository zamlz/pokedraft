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



pokeDex = PokeDex()

# the draft menu; all draft options will be shown here
def draftMenu():
	bracket = player()
	bracket.isPlayer = False
	bracket.playerLeft = player()
	bracket.playerRight = player()
	bracket.printInfo()

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

