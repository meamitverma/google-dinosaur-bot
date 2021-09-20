from PIL import ImageGrab
import pyautogui as pt

class coordinates():
    replayBtn = (482,527)

def restartGame():
    pt.click(coordinates.replayBtn)

restartGame()