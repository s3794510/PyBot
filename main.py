import os,winsound
from time import sleep, time
from bothandler import BotHandler

#os.chdir(os.path.dirname(os.path.abspath(__file__)))
window_name = 'Leaf Blower Revolution'
#window_name = 'areasxx.jpg - Paint'
# initialize bot
bot = BotHandler(window_name)
debug = None
print("""Hold shift + ESC to stop
Hold shift + P to pause/unpause.
Hold shift + F to show FPS
Program is running.
""")
bot.run()
print('Program is closed.')
i = input("Press any key to end program.\n")

