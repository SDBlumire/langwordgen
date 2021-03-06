import re
from random import randint

def chardef(definition, string):
    existingdata = loadfile()
    print("Adding Entry: "+string+" = "+definition)
    existingdata.append([string, definition])
    store = open('data.txt', 'w')
    for i in range(len(existingdata)):
        store.write(existingdata[i][0] + " = " + existingdata[i][1] + "\n")
    store.close()
    
def genstring():
    con = ["k", "g", "d", "t", "", "b", "p", "x", "z"]
    vow = ["a", "e", "o", "i", "u", "ai", "au", "ei", "wa", "we", "oi", "ou", "ia", "ie", "io", "iu", "wo", "wi"]
    fin = ["m", "n", "l", "ng"]
    genstr = con[randint(0, len(con)-1)] + vow[randint(0, len(vow)-1)] + fin[randint(0, len(fin)-1)]
    return genstr

def testex(string):
    exdata = loadfile()
    for i in range(len(exdata)):
        if exdata[i][0] == string:
            return False
    return True
        
def generateswadesh():
    swadesh = ["I", "you", "we (inclusive)", "this", "that", "who?", "what?", "not", "all", "many", "one", "two", "big", "long", "small", "woman", "man", "person", "fish", "bird", "dog", "louse", "tree", "seed", "leaf", "root", "bark", "skin", "flesh", "blood", "bone", "grease", "egg", "horn", "tail", "feather", "hair", "head", "ear", "eye", "nose", "mouth", "tooth", "tongue", "fingernail", "foot", "knee", "hand", "belly", "neck", "breasts", "heart", "liver", "drink", "eat", "bite", "see", "hear", "know", "sleep", "die", "kill", "swim", "fly", "walk", "come", "lie", "sit", "stand", "give", "say", "sun", "moon", "star", "water", "rain", "stone", "sand", "earth", "cloud", "smoke", "fire", "ash", "burn", "path", "mountain", "red", "green", "yellow", "white", "black", "night", "hot", "cold", "full", "new", "good", "round", "dry", "name", "all", "and", "animal", "ashes", "at", "back", "bad", "bark", "because", "belly", "big", "bird", "bite", "black", "blood", "blood", "blow", "bone", "breast", "breathe", "brother", "burn", "child", "clothing", "cloud", "claw", "cold", "come", "cook", "count", "cut", "dance", "day", "die", "dig", "dirty", "dog", "drink", "dry", "dull", "dust", "ear", "earth", "eat", "egg", "eight", "eye", "fall", "far", "fat/grease", "father", "fear", "feather", "few", "fight", "fire", "fish", "five", "float", "flow", "flower", "fog", "foot", "four", "freeze", "fruit", "full", "give", "good", "grass", "green", "guts", "hair", "hand", "he", "head", "hear", "heart", "heavy", "here", "hit", "hold/take", "horn", "how", "hundred", "hunt", "husband", "I", "ice", "if", "in", "kill", "knee", "know", "lake", "laugh", "leaf", "left (side)", "leg", "lie", "live", "liver", "long", "louse", "man/male", "many", "meat/flesh", "moon", "mother", "mountain", "mouth", "name", "narrow", "near", "neck", "new", "night", "nose", "not", "old", "one", "other", "person", "play", "pull", "push", "rain", "red", "right (correct)", "right (side)", "river", "road", "root", "rope", "rotten", "rub", "salt", "sand", "say", "scratch", "sea", "see", "seed", "seven", "sew", "sharp", "shoot", "short", "sing", "sister", "sit", "skin", "sky", "sleep", "small", "smell", "smoke", "smooth", "snake", "snow", "some", "spear", "spit", "split", "squeeze", "stab/pierce", "stand", "star", "stick", "stone", "straight", "suck", "sun", "swell", "swim", "tail", "ten", "that", "there", "they", "thick", "thin", "think", "this", "three", "throw", "tie", "tongue", "tooth", "tree", "turn", "two", "vomit", "walk", "warm", "wash", "water", "we (exclusive)", "wet", "what?", "when?", "where?", "white", "who?", "wide", "wife", "wind", "wing", "wipe", "with", "woman", "woods", "work", "worm", "yes", "year"]
    for i in range(len(swadesh)):
        chardef(swadesh[i], getUnusedString())

def getUnusedString():
    a = genstring()
    while testex(a) == False:
        a = genstring()
    return a

def orderall():
    sortdata = []
    exdata = loadfile()
    for i in range(len(exdata)):
        sortdata.append(exdata[i][0])
        print("SCANNING "+exdata[i][0])
    sortdata.sort()
    nexdata = []
    for i in range(len(sortdata)):
        for o in range(len(exdata)):
            if sortdata[i] == exdata[o][0]:
                print("Match: "+sortdata[i])
                nexdata.append([sortdata[i], exdata[o][1]])
                print("Adding Entry: "+sortdata[i]+" = "+exdata[o][1])
    store = open('data.txt', 'w')
    for i in range(len(nexdata)):
        store.write(nexdata[i][0] + " = " + nexdata[i][1] + "\n")
        print("Writing Entry: " + nexdata[i][0] + " = " + nexdata[i][1])
    store.close()

def lookup(wordt):
    lodata = loadfile()
    for i in range(len(lodata)):
        if lodata[i][0] == wordt:
            print(wordt+" = "+lodata[i][1])

def lookupe(worde):
    ledata = loadfile()
    for i in range(len(ledata)):
        try:
            if re.search(worde, ledata[i][1]).group(0) == worde:
                print(ledata[i][1]+" = "+ledata[i][0])
        except:
            pass
            

def loadfile():
    data = []
    store = open('data.txt', 'r')
    for line in store:
        word = re.search(r'[A-z]*(?=\s*=)', line).group(0)
        meaning = re.search(r'(?<==\s).*', line).group(0)
        data.append([word, meaning])
    store.close()
    return data
