
import csv

temp = []
data = []

def translateToDecimal(odds):
	new_odds = 100/(float(odds[1:])) + 1
	return new_odds

def getDog(fav, house_edge):

	favML = translateToDecimal(fav)
	favProb = (1 / favML)
	dogProb = (1 - house_edge - favProb)
	return (1 / dogProb)


with open('mlb2017.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		temp.append(row)

for i in range(0, len(temp), 2):
	data.append(temp[i] + temp[i+1])

# returns for buying favorites/dogs with 1u on closing line
unit = 1
bankroll = 100
betCounter = 0
roi = 0.0
gameCounter = 0

# for game in data:
# 	gameCounter =  gameCounter + 1
# 	print(str(gameCounter) + ": " + str(game))

gameCounter = 0

for game in data:
	gameCounter =  gameCounter + 1
	if ('-' in game[4]):
		favML = game[4]
		#print (str(gameCounter) + ": " + str(favML))
		ML = translateToDecimal(favML)
		#ML = getDog(favML, .02)

		#place bet
		bankroll = bankroll - unit

		if (int(game[2]) > int(game[8])):
			bankroll = bankroll + (unit * (ML-1))

		print (round(bankroll, 2))

	else:
		if ('-' in game[3]):
			favML = game[10]
		else:
			favML = game[9]
		#print (str(gameCounter) + " " + str(favML))
		ML = translateToDecimal(favML)
		#ML = getDog(favML, -0.02)

		#place bet
		bankroll = bankroll - 1

		if (int(game[8]) > int(game[2])):
			bankroll = bankroll + (unit * (ML-1))

		print (round(bankroll,2))

print ("---------------")
print (str(gameCounter))
print (str(round(bankroll - 100, 2)) + " units")
print ("roi = " + str(round((bankroll - 100)*100/gameCounter, 2)) + "%")

