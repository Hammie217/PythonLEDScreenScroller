from threading import Thread
from main import display
from main import displayItem
import pytest

def testSetRotate():
    assert myDisplay.setRotateDelay(-0.1)==0


myDisplay = display()
myDisplay.stringSet("HI")
myDisplay.printScreen()
myDisplay.setRotateDelay(0)
myDisplay.stringSetRotate("HELLO WORLD")
myDisplay.printScreen()

Thread(target=myDisplay.rotate(1)).start()
