import re
import csv

def seriesOfReplacements(myLine):
	tempLine = myLine
	tempLine = tempLine.replace(",", " ")
	tempLine = tempLine.replace("-"," ")
	tempLine = tempLine.replace("."," ")
	tempLine = tempLine.replace("!", " ")
	tempLine = tempLine.replace(":", " ")
	tempLine = tempLine.replace(";", " ")
	tempLine = tempLine.replace("?", " ")
	return tempLine

def isLetter(myChar):
	if myChar == " ":
		return 1

	if myChar == "":
		return 1

	if myChar == "\n":
		return 1

	if ord(myChar) >= 97:
		if ord(myChar) <= 122:
			return 1

	return 0

def removeEndingNonLetter(myWord):
	done = 0
	word = myWord.lower()
	while(done == 0):
		i = len(word)
		print("Inside removeEndingNonLetter -->", word, "<---")
		if isLetter(word[i-1])==0:
			word = word[:-1]
		else:#isLetter(word[i-1])==1
			done = 1

	return word

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

#printTextFileByParagraph(myList)

wordFreDict = {}
lineCount = 1
for line in myList:
	tempLine = seriesOfReplacements(line)
	print(lineCount, ") ", line)
	print(lineCount, ") ", line)
	lineCount = lineCount+1
	for word in tempLine.split():
		#tempWord = seriesOfReplacements(word)
		#newWord = removeEndingNonLetter(temp)
		newWord = word.lower()
		if newWord in wordFreDict.keys():
			wordFreDict[newWord] = wordFreDict[newWord] + 1
		else:
			wordFreDict[newWord] = 1

printDict(wordFreDict)

# with open('dict.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in wordFreDict.items():
#        writer.writerow([value])

outfile = open( 'dict.txt', 'w' )
for key in wordFreDict.keys():
	outfile.write(key + ', ' + str(wordFreDict[key]) + '\n' )
