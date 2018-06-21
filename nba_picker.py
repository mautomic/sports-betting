import csv

read = []
temp = []

with open('nba2017_quick.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		read.append(row)

for i in range(0, len(read), 2):
	temp.append(read[i] + read[i+1])

for i in temp:
	print(i)