from time import sleep
from threading import Thread
class displayItem:
    def __init__(self,width,displayArray):
        self.width = width
        self.displayArray = displayArray

    def consoleDraw(self):
        for y in range (0,8):
            for x in range(0,self.width):
                if self.displayArray[y][x]==1:
                    print("#", end='')
                else:
                    print(" ", end='')
            print("")


class display:
    def __init__(self):
        self.screen =  []
        self.screenWidth=0
        self.string = "X"
        self.displaySize=32
        self.rotateDelay=0.05
        self.displayedScreen = []
        self.rotatedCount = 0;

    def setDisplaySize(self,displays):
        self.displaySize = displays*8
    
    def setRotateDelay(self,speed):
        if(speed>=0):
            self.rotateDelay = speed
            return 0
        else:
            return -1
    

    def rotate(self,toRotate = -1):
        runs =0
        while ((runs< toRotate)or (toRotate<0)):
            sleep(self.rotateDelay)   

            if self.rotatedCount>=(self.screenWidth-self.displaySize):
                self.rotatedCount=0;
                runs +=1

            if self.displaySize>self.screenWidth:
                smalVal = self.screenWidth
            else:
                smalVal = self.displaySize
            
            for y in range (0,8):
                for x in range(self.rotatedCount,smalVal+self.rotatedCount):
                    if self.screen[y][x]==1:
                        print("#", end='')
                    else:
                        print(" ", end='')
                print("")
            
            self.rotatedCount +=1


    def joinLists(self, x,y):
        z=[]
        for i in range(0,8):
            z[i] = x[i] + y[i]
        return z

    def printScreen(self):
        for y in range (0,8):
            for x in range(0,self.screenWidth):
                if self.screen[y][x]==1:
                    print("#", end='')
                else:
                    print(" ", end='')
            print("")

    def stringSet(self,stringg):
        self.string = stringg
        self.screen = [[0],[0],[0],[0],[0],[0],[0],[0]]
        self.screenWidth=1
        for c in self.string:
            if c in character.keys():                
                self.screen = [x+y for x,y in zip(self.screen,character[c].displayArray)]
                self.screenWidth += character[c].width 

    def stringSetRotate(self,stringg):
        self.string = stringg
        self.screen = [[0],[0],[0],[0],[0],[0],[0],[0]]
        self.screenWidth=1
        for x in range(0, self.displaySize):
            self.screen = [x+y for x,y in zip(self.screen,character["VLine"].displayArray)]
            self.screenWidth += character["VLine"].width 
        for c in self.string:
            if c in character.keys():                
                self.screen = [x+y for x,y in zip(self.screen,character[c].displayArray)]
                self.screenWidth += character[c].width 
        for x in range(0, self.displaySize):
            self.screen = [x+y for x,y in zip(self.screen,character["VLine"].displayArray)]
            self.screenWidth += character["VLine"].width 



character = {
    "VLine":displayItem(1,[[0],[0],[0],[0],[0],[0],[0],[0]]),
    " ":displayItem(6,[ [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]),
    "A":displayItem(6,[ [0,0,1,0,0,0],
                        [0,1,0,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,1,1,1,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "B":displayItem(6,[ [1,1,1,1,0,0],
                        [0,1,0,0,1,0],
                        [0,1,0,0,1,0],
                        [0,1,1,1,0,0],
                        [0,1,0,0,1,0],
                        [0,1,0,0,1,0],
                        [1,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "C":displayItem(6,[ [0,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,1,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "D":displayItem(6,[ [1,1,1,1,0,0],
                        [0,1,0,0,1,0],
                        [0,1,0,0,1,0],
                        [0,1,0,0,1,0],
                        [0,1,0,0,1,0],
                        [0,1,0,0,1,0],
                        [1,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "E":displayItem(5,[ [1,1,1,1,0],
                        [1,0,0,0,0],
                        [1,0,0,0,0],
                        [1,1,1,1,0],
                        [1,0,0,0,0],
                        [1,0,0,0,0],
                        [1,1,1,1,0],
                        [0,0,0,0,0]]),
    "F":displayItem(5,[ [1,1,1,1,0],
                        [1,0,0,0,0],
                        [1,0,0,0,0],
                        [1,1,1,1,0],
                        [1,0,0,0,0],
                        [1,0,0,0,0],
                        [1,0,0,0,0],
                        [0,0,0,0,0]]),
    "G":displayItem(6,[ [0,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,0,0],
                        [1,0,0,1,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "H":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,1,1,1,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "I":displayItem(4,[ [1,1,1,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [0,1,0,0],
                        [1,1,1,0],
                        [0,0,0,0]]),
    "J":displayItem(6,[ [0,0,1,1,1,0],
                        [0,0,0,1,0,0],
                        [0,0,0,1,0,0],
                        [0,0,0,1,0,0],
                        [0,0,0,1,0,0],
                        [1,0,0,1,0,0],
                        [0,1,1,0,0,0],
                        [0,0,0,0,0,0]]),
    "K":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,1,0,0],
                        [1,0,1,0,0,0],
                        [1,1,0,0,0,0],
                        [1,0,1,0,0,0],
                        [1,0,0,1,0,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "L":displayItem(6,[ [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,1,1,1,1,0],
                        [0,0,0,0,0,0]]),
    "M":displayItem(6,[ [1,0,0,0,1,0],
                        [1,1,0,1,1,0],
                        [1,0,1,0,1,0],
                        [1,0,1,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "N":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,1,0,0,1,0],
                        [1,0,1,0,1,0],
                        [1,0,0,1,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "O":displayItem(6,[ [0,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "P":displayItem(6,[ [1,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,1,1,1,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [0,0,0,0,0,0]]),
    "Q":displayItem(6,[ [0,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,1,0,1,0],
                        [1,0,0,1,0,0],
                        [0,1,1,0,1,0],
                        [0,0,0,0,0,0]]),
    "R":displayItem(6,[ [1,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,1,1,1,0,0],
                        [1,0,1,0,0,0],
                        [1,0,0,1,0,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "S":displayItem(6,[ [0,1,1,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,0,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "T":displayItem(6,[ [1,1,1,1,1,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,0,0,0]]),
    "U":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,0,0]]),
    "V":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,0,1,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,0,0,0]]),
    "W":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,1,0,1,0],
                        [1,0,1,0,1,0],
                        [1,0,1,0,1,0],
                        [0,1,0,1,0,0],
                        [0,0,0,0,0,0]]),
    "X":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,0,1,0,0],
                        [0,0,1,0,0,0],
                        [0,1,0,1,0,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,0,0,0,0,0]]),
    "Y":displayItem(6,[ [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [1,0,0,0,1,0],
                        [0,1,0,1,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,0,0,0]]),
    "Z":displayItem(6,[ [1,1,1,1,1,0],
                        [0,0,0,0,1,0],
                        [0,0,0,1,0,0],
                        [0,0,1,0,0,0],
                        [0,1,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,1,1,1,1,0],
                        [0,0,0,0,0,0]]), 
}
















