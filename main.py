from pyo import *
import os
s = Server().boot()
s.start()


alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",",",".","\n"]
file= open("textfile.txt","r")
sFolder = "sounds/"
#sounds = ["00.wav","01.wav","02.wav","03.wav","04.wav","05.wav","06.wav","7.wav","08.wav","09.wav","10.wav","11.wav","12.wav","13.wav","14.wav","15.wav","16.wav","17.wav","18.wav","19.wav","20.wav","21.wav","22.wav","23.wav","24.wav","25.wav","26.wav","27.wav","28.wav","30.wav"]
sounds = []
soundsListLen = list()

# Convert letters array to num
def let2num(letter):
    return alpha.index(letter)         
x = map(let2num, file.read())


# Get nbr of files in directory
dirs = os.listdir(sFolder)
for file in dirs:
    soundsListLen.append(file)
listLength = len(soundsListLen)
#print(listLength)

# Put files in direct. into sounds array
for i in range(listLength):
    sounds.append(dirs[i])
print(sounds)


# fonction calling each sounds in for loop
def loopSound():
    for i in x:
        player = SfPlayer(sFolder+sounds[i], speed=1, mul=0.5).mix(2).out()

loopSound()






print("end")

s.gui(locals())