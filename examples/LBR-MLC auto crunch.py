import cv2, win32con
from playsound import playsound
from pybot import PyBot
import time, os
def main():
    
    needleimg_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'needle_images')
    window_name = 'Leaf Blower Revolution'
    needle_mlcbutton = os.path.join(needleimg_dir, 'mlcbutton.jpg')
    needle_craftbar = os.path.join(needleimg_dir, 'craftbar.jpg')
    needle_crafingxxx = os.path.join(needleimg_dir, 'craftingxxx.jpg')
    needle_megaleafcrunch = os.path.join(needleimg_dir, 'megaleafcrunch.jpg')
    needle_megacrunch = os.path.join(needleimg_dir, 'megacrunch.jpg')
    needle_confirm = os.path.join(needleimg_dir, 'confirm.jpg')
    # initialize bot
    #bot = bothandler.BotHandler(window_name)
    debug = ''
    debug_find_image = 'rectangles show'
    # Input an existing wav filename
    bot = PyBot(window_name, debug)

    # Add images to find

    # mlc_auto_crunch
    bot.add_image(needle_mlcbutton, needle_mlcbutton)
    bot.add_image (needle_megaleafcrunch, needle_megaleafcrunch)
    bot.add_image (needle_megacrunch, needle_megacrunch)
    bot.add_image (needle_confirm,needle_confirm)
    # craft_leaves
    #bot.add_image ('craftbar', needle_craftbar)
    #bot.add_image ('craftingxxx', needle_crafingxxx)


    # Bot actions
    def actions(text = 'ABC'):
        print(f"this is action {text}")

    def craft_leaves(): #not working
        #if bot.find_image('craftingxxx', 0.5, cv2.COLOR_BGR2GRAY, debug_find_image):
        if not (bot.find_image('craftbar', 0.8, None, debug_find_image)):
            #bot.key_press(' ', 0)
            pass

    def mlc_auto_crunch():
        if points:=bot.find_image(needle_megaleafcrunch, 0.7, cv2.COLOR_BGR2GRAY, ''):
            if points:=bot.find_image(needle_megacrunch, 0.7, cv2.COLOR_BGR2GRAY, ''):
                bot.left_click(points[0],0.1)
                pass
            pass
        else:
            if points:=bot.find_image(needle_confirm, 0.7, cv2.COLOR_BGR2GRAY, ''):
                bot.left_click(points[0],0.1)
                pass
            elif points:=bot.find_image(needle_mlcbutton,0.9, None, debug_find_image):
                bot.left_click(points[0],0.1)
                pass
    # bot resize window
    bot.resize(640,380)

    # Run bot with the defined set of actions
    bot.run(0, 0, mlc_auto_crunch)

def testing():

    pass

#testing()

# Driver code
if __name__ == '__main__':
    main()