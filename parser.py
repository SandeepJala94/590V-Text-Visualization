import re
import csv

def removeEndingNonLetter(word):
	done = 0
	# while(done == false)
	# 	if(word[len(word)]

	return word.lower()

def printTextFileByParagraph(myList):
	paragraphCount = 1
	for paragraph in myList:
		print(paragraphCount, ") ", paragraph)
		paragraphCount = paragraphCount+1

def printDict(myDict):
	lineCount=1
	for key in myDict.keys():
		print(lineCount, " ", key, " ", myDict[key])
		lineCount = lineCount+1



f = open("PsychologyOfLinguisticForm.txt","r")
myList = []
for line in f:
    myList.append(line)

printTextFileByParagraph(myList)

wordFreDict = {}
for line in myList:
	for word in re.split(' ', line):
		newWord = removeEndingNonLetter(word)
		if newWord in wordFreDict.keys():
			wordFreDict[newWord] = wordFreDict[newWord] + 1
		else:
			wordFreDict[newWord] = 1

printDict(wordFreDict)

# with open('dict.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in wordFreDict.items():
#        writer.writerow([value])

# outfile = open( 'dict.txt', 'w' )
# for key, value in sorted( wordFreDict.items() ):
#     outfile.write( str(key) + ',\t' + str(value) + '\n' )