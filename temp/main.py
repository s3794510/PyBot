import cv2 as cv
import numpy as np
import os
from time import time,sleep
from PyBot.BotController import BotController
from PyBot.vision import Vision
from PyBot.windowcapture import WindowCapture
import win32gui, win32ui, win32con, win32api, keyboard, winsound, pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


while(False):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


def actions(bot):
    pass
    
print('Here 0')

bot = BotController("Leaf Blower Revolution")
bot.run()
# initialize the WindowCapture class
wincap = WindowCapture('Leaf Blower Revolution')
# initialize the Vision class
vision_limestone = Vision('areasxx.jpg')
while not keyboard.is_pressed('esc') or not keyboard.is_pressed('shift'):
    loop_time = time()
    #bot.press_key('V', 0, 0.1)
    #bot.press_key('U', 0, 0.1)
    #bot.press_key('U', 0, 0.1)
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    # display the processed image
    points = vision_limestone.find(screenshot, 0.5, 'points')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
bot.exit()
#cv.destroyAllWindows()


print('Done.')
