from random import *
import sys
import os
import time
import datetime

import config

from twython import Twython
print("Imported libraries...")

tweetInterval = 15
exclamationChance = 10
hashtagChance = 10
allCapsChance = 20

with open("nouns.txt", "r") as f:
        nouns = f.read()
        nouns = nouns.split("\n")
        
with open("verbs.txt", "r") as f:
        verbs = f.read()
        verbs = verbs.split("\n")
        
with open("adjectives.txt", "r") as f:
        adjectives = f.read()
        adjectives = adjectives.split("\n")
        
with open("adverbs.txt", "r") as f:
        adverbs = f.read()
        adverbs = adverbs.split("\n")
        
with open("pronouns.txt", "r") as f:
        pronouns = f.read()
        pronouns = pronouns.split("\n")
        
with open("prepositions.txt", "r") as f:
        prepositions = f.read()
        prepositions = prepositions.split("\n")
        
with open("conjunctions.txt", "r") as f:
        conjunctions = f.read()
        conjunctions = conjunctions.split("\n")
        
with open("determiners.txt", "r") as f:
        determiners = f.read()
        determiners = determiners.split("\n")
        
with open("exclamations.txt", "r") as f:
        exclamations = f.read()
        exclamations = exclamations.split("\n")
        
with open("punctuations.txt", "r") as f:
        punctuations = f.read()
        punctuations = punctuations.split("\n")

with open("sentenceTypes.txt", "r") as f:
        sentenceTypes = f.read()
        sentenceTypes = sentenceTypes.split("\n")
print("Loaded words & sentences...")

api = Twython(config.CONSUMER_KEY,config.CONSUMER_SECRET,config.ACCESS_KEY,config.ACCESS_SECRET)
print("Logged into Twitter!")
print("")

def CheckTime():
    now = datetime.datetime.now()

    for i in range(int(60/tweetInterval)):
        if(now.minute == i * tweetInterval and now.second == 17):
            return True

def GenerateSentence():
    typeOn = randint(0, len(sentenceTypes) - 1)

    words = sentenceTypes[typeOn]
    words = words.split(",")
    
    wordList = []
    for word in words:
        wordList.append(word)

    generatedSentence = ""

    i = 0
    for word in words:
        if(randint(0,hashtagChance) == 0 and wordList[i] != str(10) and wordList[i] != str(7)):
            generatedSentence = generatedSentence + "#"
        
        if int(word) == 1:
            generatedSentence = generatedSentence + nouns[randint(0, len(nouns) - 1)]
        elif int(word) == 2:
            generatedSentence = generatedSentence + verbs[randint(0, len(verbs) - 1)]
        elif int(word) == 3:
            generatedSentence = generatedSentence + adjectives[randint(0, len(adjectives) - 1)]
        elif int(word) == 4:
            generatedSentence = generatedSentence + adverbs[randint(0, len(adverbs) - 1)]
        elif int(word) == 5:
            generatedSentence = generatedSentence + pronouns[randint(0, len(pronouns) - 1)]
        elif int(word) == 6:
            generatedSentence = generatedSentence + prepositions[randint(0, len(prepositions) - 1)]
        elif int(word) == 7:
            generatedSentence = generatedSentence + conjunctions[randint(0, len(conjunctions) - 1)]
        elif int(word) == 8:
            generatedSentence = generatedSentence + determiners[randint(0, len(determiners) - 1)]
        elif int(word) == 9:
            generatedSentence = generatedSentence + exclamations[randint(0, len(exclamations) - 1)]

        try:
            if(wordList[i + 1] != str(10)):
                generatedSentence = generatedSentence + " "
            else:
                generatedSentence = generatedSentence + punctuations[randint(0, len(punctuations) - 1)]
                if(randint(0,exclamationChance) == 0):
                    generatedSentence = generatedSentence + " " + exclamations[randint(0, len(exclamations))]
        except:
            pass
        i = i + 1

    if(randint(0, allCapsChance) == 0):
        generatedSentence = generatedSentence.upper()

    return generatedSentence

while(True):
    if(CheckTime()):
        api.update_status(status = GenerateSentence())
        print("tweeted\n")
    time.sleep(1)
