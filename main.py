import cv2 as cv
import keyboard
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture('Leaf Blower Revolution')

# initialize the Vision class
vision_limestone = Vision('areasxx.jpg')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if keyboard.is_pressed('esc') and keyboard.is_pressed('shift'):
        break
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
print('Done.')
