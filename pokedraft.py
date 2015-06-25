from pokedex import *
from pokeDBmod import *
import random

pokeDex = PokeDex()

def draftMenu():
	pass

def settingsMenu():
	pass

def mainMenu():
	loadSettings()
	pokeDex = PokeDex()
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



def loadSettings():
	pass

def printTitle():
	x = random.randrange(1,3)
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

