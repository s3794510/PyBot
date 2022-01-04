import cv2
import keyboard
import os
from time import sleep, time
from bothandler import BotHandler
from windowcapture import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
window_name = 'Leaf Blower Revolution'
#window_name = 'areasxx.jpg - Paint'


# initialize bot
bot = BotHandler(window_name)
# resize window
bot.WindowHandler.window_resize(640, 360)
# initialize the WindowCapture class
wincap = WindowCapture(window_name)
# initialize the Vision class
area_img = Vision('areasxx.jpg')
teleport_img = Vision('teleport.jpg')

loop_time = time()
while(True):
    sleep(2)
    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = area_img.find(screenshot, 0.8, None, cv2.COLOR_BGR2GRAY)
    if not (len(points)):
        bot.keyboard_press('v', 0)
        pass
    if (len(points)):
        points = teleport_img.find(screenshot, 0.95, None, cv2.COLOR_BGR2GRAY)
        if (len(points)):
            x,y = points[0]
            bot.leftclick(x,y, 0)

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
