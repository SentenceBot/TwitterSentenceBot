import sys
import os
import time
import datetime
from random import *
from twython import Twython
print("Imported libraries...")

import config
print("Imported private keys...")
print("")

subjects = []
verbs = []
objects = []
punctuation = []
adjectives = []
conjunctions = []

tweetInterval = 10

with open("subjects.txt", "r") as f:
        subjects = f.read()
        subjects = subjects.split("\n")
with open("verbs.txt", "r") as f:
        verbs = f.read()
        verbs = verbs.split("\n")
with open("objects.txt", "r") as f:
        objects = f.read()
        objects = objects.split("\n")
with open("punctuation.txt", "r") as f:
        punctuation = f.read()
        punctuation = punctuation.split("\n")
with open("adjectives.txt", "r") as f:
        adjectives = f.read()
        adjectives = adjectives.split("\n")
with open("conjunctions.txt", "r") as f:
        conjunctions = f.read()
        conjunctions = conjunctions.split("\n")
print("Loaded words into memory...")
print("")

api = Twython(config.CONSUMER_KEY,config.CONSUMER_SECRET,config.ACCESS_KEY,config.ACCESS_SECRET)
print("Logged into Twitter!")
print("")

def GenerateSentenceAndTweet():
    canTweet = True
    subjectSeed = randint(0,len(subjects)-1)
    verbSeed = randint(0,len(verbs)-1)
    objectSeed = randint(0,len(objects)-1)
    punctuationSeed = randint(0,len(punctuation)-1)
    adjectiveSeed = randint(0,len(adjectives)-1)
    conjunctionSeed = randint(0,len(conjunctions)-1)
    sentenceSeed = randint(0,3)
    hashtagSeed = randint(0,15)

    if(sentenceSeed==0 and hashtagSeed == 0):
        sentence = "#" + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==0 and hashtagSeed == 1):
        sentence = subjects[subjectSeed] + " " + "#" + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==0 and hashtagSeed == 2):
        sentence = subjects[subjectSeed] + " " + verbs[verbSeed] + " " + "#" + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==0):
        sentence = subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==1 and hashtagSeed == 0):
        sentence = "#" + adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==1 and hashtagSeed == 1):
        sentence = adjectives[adjectiveSeed] + " " + "#" + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==1 and hashtagSeed == 2):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + "#" + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==1 and hashtagSeed == 3):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + "#" + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==1):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==2 and hashtagSeed == 0):
        sentence = "#" + adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==2 and hashtagSeed == 1):
        sentence = adjectives[adjectiveSeed] + " " + "#" + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==2 and hashtagSeed == 2):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + "#" + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==2 and hashtagSeed == 3):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + "#" + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==2 and hashtagSeed == 4):
        sentence = "#" + adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + "#" + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==2):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==3 and hashtagSeed == 0):
        sentence = "#" + adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + " " + subjects[round(subjectSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==3 and hashtagSeed == 1):
        sentence = adjectives[adjectiveSeed] + " " + "#" + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + " " + "#" + subjects[round(subjectSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==3 and hashtagSeed == 2):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + "#" + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + " " + subjects[round(subjectSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==3 and hashtagSeed == 3):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + "#" + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + " " + subjects[round(subjectSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==3 and hashtagSeed == 4):
        sentence = "#" + adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + "#" + adjectives[round(adjectiveSeed/2)] + " " + "#" + subjects[round(subjectSeed/2)] + punctuation[punctuationSeed]
    elif(sentenceSeed==3):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + " " + subjects[round(subjectSeed/2)] + punctuation[punctuationSeed]


    now = datetime.datetime.now().minute
    for intervalCheck in range(int(60/tweetInterval)):
        if(now==intervalCheck*tweetInterval and canTweet):
            api.update_status(status=sentence)
            print(str(datetime.datetime.now().hour%12) + ":" + str(datetime.datetime.now().minute) + " | " + "Tweeted sentence: " + sentence)
            canTweet = False
        if(now!=intervalCheck*tweetInterval):
            canTweet = True
            

while(True):
    try:
        GenerateSentenceAndTweet()
    except:
        pass
    time.sleep(60)
