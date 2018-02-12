from random import *

subjects = []
verbs = []
objects = []
punctuation = []
adjectives = []
conjunctions = []

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

def generateWord():
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

    print(sentence)

for x in range(100):
    generateWord()

