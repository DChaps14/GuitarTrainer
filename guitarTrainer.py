import random
import numpy as np
import cv2
from matplotlib import pyplot as plt

scale_dict = {0:"Major", 1:"Minor Pentatonic", 2:"Blues", 3:"Melodic Minor"}
note_dict = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G"}
inflection_dict = {0:"", 1:"#", 2:"b"}
eStringDict = {0:5, 1:7, 2:8, 3:10, 4:0, 5:1, 6:3}
aStringDict = {0:0, 1:2, 2:3, 3:5, 4:7, 5:8, 6:10}
dStringDict = {0:7, 1:9, 2:10, 3:0, 4:2, 5:3, 6:5}
gStringDict = {0:2, 1:4, 2:5, 3:7, 4:9, 5:10, 6:0}
bStringDict = {0:10, 1:0, 2:1, 3:3, 4:5, 5:6, 6:8}
dictDict = {0:eStringDict, 1:aStringDict, 2:dStringDict, 3:gStringDict, 4:bStringDict, 5:eStringDict}

def getNewScale():
    scale = scale_dict.get(random.randrange(4))
    note = note_dict.get(random.randrange(7))
    inflection = inflection_dict.get(random.randrange(3))
    
    string = "{} scale in {}{}"
    print(string.format(scale, note, inflection))    
    
    img = cv2.imread('{}.jpg'.format(scale),0)
    plt.imshow(img, cmap = "gray", interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()    

def generateRandomMelody():
    staveTable = []
    pitchPrompt = "Please indicate where you want your melody to be: (h)igh, (m)edium, (l)ow, or (w)hole fretboard.\n"
    lengthPrompt = "Please indicate how many notes you wish your melody to be: "
    length = input(lengthPrompt)
    length = int(length)
    pitch = input(pitchPrompt)
    
    for i in range(6):
        staveTable.append(["-"]*length)
    
    for i in range(length):
        string = random.randrange(2)
        note = random.randrange(8)
        inflection = random.randrange(-1, 1)
        
        #If note is 7, this indicates a rest
        if pitch == "l" and note != 7:
            if string == 0:
                staveTable[5][i] = str(eStringDict.get(note)+inflection)
            else:
                staveTable[4][i] = str(aStringDict.get(note)+inflection)
        elif pitch == "m" and note != 7:
            if string == 0:
                staveTable[3][i] = str(dStringDict.get(note)+inflection)
            else:
                staveTable[2][i] = str(gStringDict.get(note)+inflection)
        elif pitch == "h" and note != 7: #pitch must be high
            if string == 0:
                staveTable[1][i] = str(bStringDict.get(note)+inflection)
            else:
                staveTable[0][i] = str(eStringDict.get(note)+inflection)
        elif note != 7:
            string = random.randrange(6)
            staveTable[5-string][i] = str(dictDict.get(string).get(note)+inflection)
            
    for i in range(len(staveTable)):
        staveString = ""
        for j in range(length):
            if staveTable[i][j] < "0" and staveTable[i][j] != "-":
                staveTable[i][j] = 0            
            staveString += "|{}|".format(staveTable[i][j])
        print(staveString)
    
    

def main():
    commandInput = "Please indicate what feature you wish to use:\n(m)elody generator, (s)cale practice, or (e)xit: "
    command = input(commandInput)
    while command != "e":
        if command == "m":
            generateRandomMelody()
        elif command == "s":
            getNewScale()
        command = input(commandInput)
            
    
main()