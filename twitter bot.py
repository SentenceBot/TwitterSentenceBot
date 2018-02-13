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


canTweet = True
tweetInterval = 5

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
    subjectSeed = randint(0,len(subjects)-1)
    verbSeed = randint(0,len(verbs)-1)
    objectSeed = randint(0,len(objects)-1)
    punctuationSeed = randint(0,len(punctuation)-1)
    adjectiveSeed = randint(0,len(adjectives)-1)
    conjunctionSeed = randint(0,len(conjunctions)-1)
    sentenceSeed = randint(0,2)

    if(sentenceSeed==0):
        sentence = subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==1):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + punctuation[punctuationSeed]
    elif(sentenceSeed==2):
        sentence = adjectives[adjectiveSeed] + " " + subjects[subjectSeed] + " " + verbs[verbSeed] + " " + objects[objectSeed] + " " + conjunctions[conjunctionSeed] + " " + adjectives[round(adjectiveSeed/2)] + punctuation[punctuationSeed]

    for minCheck in range(int(60/tweetInterval)):
        now = datetime.datetime.now()
        if(now.minute==minCheck*tweetInterval and canTweet):
            canTweet = False
            api.update_status(status=sentence)
            print("Tweeted sentence: " + sentence)
        if(now.minute!=minCheck):
            canTweet = True
            

while(True):
    GenerateSentenceAndTweet()
    time.sleep(1)
