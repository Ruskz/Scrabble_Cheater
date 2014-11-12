# This program takes in a rack of letters in the game of scrabble and then
# computes all words and their associated values

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10," ": 0} # All values for letters in scrabble

wordFile = open("sowpods.txt","r") #read the file
wordList = wordFile.readlines() # MOves words to a list

for i in range(0,len(wordList)):
    word = wordList[i]
    wordList[i] = word[0:len(word)-1].lower()

# Obtains a valid rack from the user
def get_rack():
    print "Enter the rack in the following format \"adngsesf\""
    while True:
        userRack = raw_input("Enter rack: ")
        if len(userRack) == 8:
            break
        else:
            print "Please enter the correct number of letters"
    return userRack.lower()

# Creates a list of valid words from the user's rack
def valid_word(wordList,userRack):
    validList = []
    
    for word in wordList:
        valid = True
        deletingRack = userRack
        
        for i in range(0,len(word)):
            if word[i] in deletingRack:
                deletingRack = deletingRack.replace(word[i],"",1)
            elif " " in deletingRack:
                deletingRack = deletingRack.replace(" ","",1)
            else:
                valid = False
                break

        if valid == True:
            validList.append(word)

    return validList

def calc_values(validList,scores):
    wordValues = {}
    for word in validList:
        score = 0
        for i in range(0,len(word)):
            score += scores[word[i]]
        wordValues[word] = score
    return wordValues

def max_value_key(valueList):
    keyList = list(valueList.keys())
    valueList = list(valueList.values())
    return keyList[valueList.index(max(valueList))]

userRack = get_rack()
validList = valid_word(wordList,userRack)
wordValues = calc_values(validList,scores)
maxKey =  max_value_key(wordValues)
maxValue = wordValues[maxKey]

print "The following word has the highest score value for the given rack."
print str(maxKey) + " : " + str(maxValue)

