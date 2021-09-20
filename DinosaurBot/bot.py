from time import time
from PIL import ImageGrab, ImageOps
import pyautogui as pt
import time
from numpy import *

class coordinates():
    replayBtn = (482,527)
    dinosaur = (189,532)
    #284 = x coordinate to check for tree
    #560 = y coordinate

def restartGame():
    pt.click(coordinates.replayBtn)

def pressSpace():
    pt.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pt.keyUp("space")

def imageGrab():
    box = (coordinates.dinosaur[0] + 95 , coordinates.dinosaur[1], coordinates.dinosaur[0] + 198, coordinates.dinosaur[1] + 33)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 3646):
            pressSpace()
            time.sleep(0.1)

main()
