import cv2
from playsound import playsound
from pybot import PyBot
import time, os
def main():
    
    needleimg_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'needle_images')
    window_name = 'Leaf Blower Revolution'
    needle_mlcbutton = os.path.join(needleimg_dir, 'mlcbutton.jpg')
    print("***********************",needle_mlcbutton)
    # initialize bot
    #bot = bothandler.BotHandler(window_name)
    debug = 'debug'
    # Input an existing wav filename
    bot = PyBot(window_name, debug)
    bot.resize(640,380)
    bot.add_image('mlcbutton', needle_mlcbutton)
    bot.run(actions)

def actions(text = 'ABC'):
    print(f"this is action {text}")

# Driver code
if __name__ == '__main__':
    main()