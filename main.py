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
debug = ""
loop_time = time()
print("""Hold shift + ESC to stop
Hold shift + P to pause.""")
while(bot.is_running):
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
    loop_time = bot.flow_handle(0.5 ,loop_time, 'debug')
print('Done.')
