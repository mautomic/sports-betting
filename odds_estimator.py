
def translateToDecimal(val):
	new_odds = val
	odds = str(val)
	if (val > 100):
		new_odds = float(odds)/100 + 1
	elif (odds[0] == "-"):
		new_odds = 100/(float(odds[1:])) + 1
	else:
		pass
	return new_odds


def getHouseEdge(fav, dog):

	favML = translateToDecimal(fav)
	dogML = translateToDecimal(dog)

	favProb = (1 / favML)
	dogProb = (1 / dogML)
	house_edge = (1 - favProb - dogProb)
	printInfo(favProb, favML, dogProb, dogML, house_edge)

def getDog(fav, house_edge):

	favML = translateToDecimal(fav)

	favProb = (1 / favML)
	dogProb = (1 - house_edge - favProb)
	dogML = (1 / dogProb)
	printInfo(favProb, favML, dogProb, dogML, house_edge)


def getFav(dog, house_edge):

	dogML = translateToDecimal(dog)

	dogProb = (1 / dogML)
	favProb = (1 - house_edge - dogProb)
	favML = (1 / favProb)
	printInfo(favProb, favML, dogProb, dogML, house_edge)


def printInfo(favProb, favML, dogProb, dogML, house_edge):
	print ("Implied prob of favorite = " + str(round(favProb, 3)))
	print ("Implied prob of dog = " + str(round(dogProb, 3)))
	print ("ML of favorite = " + str(round(favML, 3)))
	print ("ML of dog = " + str(round(dogML, 3)))
	print ('House edge = ' + str(round(-house_edge*100, 3)) + "%")

#standard house edge
house_edge = -.02

#getDog(-182, house_edge)
getHouseEdge(1.625, 2.3)



