from pyo import *
import os
import random
s = Server().boot()
s.start()


alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",",",".","\n"]
file= open("textfile.txt","r")
sPath = "sounds/"
sounds = []
soundsListLen = list()
readSpeed = random.uniform(.1,1)

# Convert letters array to num
def let2num(letter):
    return alpha.index(letter)         
x = map(let2num, file.read())


# Get nbr of files in directory
dirs = os.listdir(sPath)
for file in dirs:
    soundsListLen.append(file)
listLength = len(soundsListLen)

# Put files in direct. into sounds array
for i in range(listLength):
    sounds.append(dirs[i])

# fonction calling each sounds in for loop
def loopSound():
    for i in x:
        player = SfPlayer(sPath+sounds[i], speed=readSpeed, mul=0.5).mix(2).out()
        



loopSound()






print("end")

s.gui(locals())