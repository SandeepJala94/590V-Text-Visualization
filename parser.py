import re
import csv

def removeEndingNonLetter(word):
	done = 0
	# while(done == false)
	# 	if(word[len(word)]

	return word.lower()

f = open("PsychologyOfLinguisticForm.txt","r")
myList = []
for line in f:
    myList.append(line)

lineCount = 1
for line in myList:
	print(lineCount, ") ", line)
	lineCount = lineCount+1

wordFreDict = {}
for line in myList:
	for word in re.split(' ', line):
		newWord = removeEndingNonLetter(word)
		if newWord in wordFreDict.keys():
			wordFreDict[newWord] = wordFreDict[newWord] + 1
		else:
			wordFreDict[newWord] = 1

for key in wordFreDict.keys():
	print(key, " ", wordFreDict[key])

# with open('dict.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in wordFreDict.items():
#        writer.writerow([value])

outfile = open( 'dict.txt', 'w' )
for key, value in sorted( wordFreDict.items() ):
    outfile.write( str(key) + ',\t' + str(value) + '\n' )