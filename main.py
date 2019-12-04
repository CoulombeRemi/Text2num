from pyo import *
import os
import random
from strings import Multi_strings
s = Server().boot()
s.start()
#s.amp = .3

# 48
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",",",".","\n","-","$","@","!","\'","\"","(",")","0","1","2","3","4","5","6","7","8","9"]
file= open("textfile.txt","r")
sPath = "sounds/"
sounds = []
soundsListLen = list()
readSpeed = random.uniform(.75,1.1)


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

print(len(alpha))
print(len(sounds))
# fonction calling each sounds in for loop
def loopSound():
    for i in x:
        player = SfPlayer(sPath+sounds[i], speed=readSpeed, mul=0.5).mix(2).out()
        
loopSound()


print("end")

s.gui(locals())