import cv2
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
area_img = Vision('areasxx.jpg')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    
    # display the processed image
    #points = area_img.find(screenshot, 0.8, 'points', cv2.COLOR_BGR2GRAY)
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if keyboard.is_pressed('esc') and keyboard.is_pressed('shift'):
        break
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
print('Done.')
