import csv

data = []

def translateToDecimalMinus(odds):
	new_odds = 100/(float(odds[1:])) + 1
	return round(new_odds, 2)

def translateToDecimalPlus(odds):
	new_odds = (float(odds)/100) + 1
	return round(new_odds, 2)

with open('worldcup06-14_playoffs.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		data.append(row)

update = []

for i in data:
	temp = []
	temp.append(i[0])
	temp.append(i[1])
	temp.append(i[3])
	temp.append(i[4])
	temp.append(i[5])
	temp.append(i[6])
	if (int(i[7]) < 0):
		temp.append(translateToDecimalMinus(i[7]))
	else:
		temp.append(translateToDecimalPlus(i[7]))

	if (int(i[8]) < 0):
		temp.append(translateToDecimalMinus(i[8]))
	else:
		temp.append(translateToDecimalPlus(i[8]))

	if (int(i[9]) < 0):
		temp.append(translateToDecimalMinus(i[9]))
	else:
		temp.append(translateToDecimalPlus(i[9]))

	update.append(temp)


games = update.reverse()

bankroll = 0


for i in update:
	print (i)
	if (i[4] == "Draw"):
		bankroll = bankroll + ((float(i[7])-1)*100)
	else:
		bankroll = bankroll - 100

	print (bankroll)




