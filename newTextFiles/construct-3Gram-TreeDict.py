import json
import pprint

def seriesOfReplacements(myLine):
	tempLine = myLine
	tempLine = tempLine.replace(",", " ")
	tempLine = tempLine.replace("-"," ")
	tempLine = tempLine.replace("."," ")
	tempLine = tempLine.replace("!", " ")
	tempLine = tempLine.replace(":", " ")
	tempLine = tempLine.replace(";", " ")
	tempLine = tempLine.replace("?", " ")
	tempLine = tempLine.replace("(", " ")
	tempLine = tempLine.replace(")", " ")
	tempLine = tempLine.replace("{", " ")
	tempLine = tempLine.replace("}", " ")
	tempLine = tempLine.replace("[", " ")
	tempLine = tempLine.replace("]", " ")
	tempLine = tempLine.replace("\"", " ")
	tempLine = tempLine.replace("'", " ")
	return tempLine.lower()

def createFirstLayer(givenFile):
    f = open(givenFile,"r")
    ThreeGramDict = {}
    for line in f:
        tempLine = seriesOfReplacements(line)
        for word in tempLine.split():
            if word not in ThreeGramDict.keys():
                ThreeGramDict[word] = {"name":word, "children": []}

    return ThreeGramDict

def createSecondLayer(givenDict, givenFile):
    f = open(givenFile,"r")
    for line in f:
        tempLine = seriesOfReplacements(line)
        for i in range(1,len(tempLine.split())):
            #print(tempLine.split()[i]
            #print(ThreeGramDict[tempLine.split()[i-1]])
            ThreeGramDict[tempLine.split()[i-1]] = {tempLine.split()[1]: {}}


    # for key in ThreeGramDict.keys():
    #     print(key, ": ", ThreeGramDict[key])
        #print(key)

def createSecondLayerV2(givenDict, givenFile):
    f = open(givenFile, 'r')
    for line in f:
        tempLine = seriesOfReplacements(line)
        for i in range(1,len(tempLine.split())):
            prevWord = tempLine.split()[i-1]
            currentWord = tempLine.split()[i]
            #givenDict[prevWord]['children'] = givenDict[prevWord]['children'].update([{"name": currentWord}, {"children": []}])
            givenDict[prevWord]['children'].append({"name": currentWord, "children": {}})
            #givenDict[prevWord]['children'].append({"children": []})


    # for key in givenDict.keys():
    #     if len(givenDict[key]['children']) > 1:
    #         print(key, ") ", givenDict[key], "\n")
        #print(key, ": ", givenDict[key])

    return givenDict

ThreeGramDict = createFirstLayer("PsychologyOfLinguisticForm.txt")

#createSecondLayer(ThreeGramDict, "PsychologyOfLinguisticForm.txt")
ThreeGramDict = createSecondLayerV2(ThreeGramDict, "PsychologyOfLinguisticForm.txt")

listOfWords = ['complex','journal','comprehension','some','most','when','process','articulatory'
,'features'
,'information'
,'cues'
,'verb'
,'between'
,'about'
,'particular'
,'perception'
,'distinct'
,'knowledge'
,'cognitive'
,'theories'
,'memory'
,'brain'
,'system'
,'researchers'
,'analysis'
,'representation'
,'thought'
,'model'
,'aphasia'
,'psychology'
,'human'
,'spoken'
,'motor'
,'acoustic'
,'set'
,'perceptual'
,'individual'
,'like'
,'experimental'
,'phonetics'
,'levels'
,'morphemes'
,'based'
,'during'
,'associated'
,'theory'
,'signal'
,'scratched'
,'roles'
,'thematic'
,'lexicon'
,'access'
,'studies'
,'conceptual'
,'related'
,'review'
,'fundamental'
,'than'
,'produce'
,'liberman'
,'see'
,'proposed'
,'planning'
,'fowler'
,'even'
,'languages'
,'morpheme'
,'modern'
,'assumption'
]
# for key in ThreeGramDict.keys():
#     print(key, ": ", ThreeGramDict[key])

for word in listOfWords:
	newFile = word + ".json"
	outfile2 = open(newFile, "w")
	outfile2.write(str(ThreeGramDict[word]))

# for key in ThreeGramDict.keys():
# 	#print(key)
# 	#print(str(key))
# 	newTextFile = str(key) + ".json"
# 	print(newTextFile)
# 	try:
# 		outfile2 = open(newTextFile, "w")
# 		entireDictAsText = str(ThreeGramDict[key])
# 		entireDictAsJSON = json.load(entireDictAsText)
# 		outfile2.write(json.dumps(entireDictAsJSON, indent=4, sort_keys=True))
# 	except:
# 		print("ERROR OCCURRED HERE FOR ", str(key))

#print(ThreeGramDict)

# for key in ThreeGramDict.keys():
#     if len(ThreeGramDict[key]['children']) > 1:
#         print(key, ") ", ThreeGramDict[key], "\n")
