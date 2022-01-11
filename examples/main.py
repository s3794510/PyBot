import cv2
from playsound import playsound
import pybot
from pygame import mixer
import time
def main():
    #os.chdir(os.path.dirname(os.path.abspath(__file__)))
    window_name = 'Leaf Blower Revolution'
    #window_name = 'areasxx.jpg - Paint'
    # initialize bot
    #bot = bothandler.BotHandler(window_name)
    debug = 'debug'
    print("""Hold shift + ESC to stop
Hold shift + P to pause/unpause.
Hold shift + F to show FPS
Program is running.
    """)


    # Input an existing wav filename

    bot = pybot.PyBot(window_name, debug)
    bot.run()
    print('Program is closed.')
    i = input("Press any key to end program.\n")


# Driver code
if __name__ == '__main__':
    main()