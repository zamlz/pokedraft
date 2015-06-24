
cont = True
condition = 'y'
f = open("testfile","a")

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