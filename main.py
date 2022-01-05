import os,winsound
from time import sleep, time
from bothandler import BotHandler

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
window_name = 'Leaf Blower Revolution'
#window_name = 'areasxx.jpg - Paint'

# initialize bot
bot = BotHandler(window_name)
debug = None
print("""Hold shift + ESC to stop
Hold shift + P to pause.
Hold shift + F to show FPS
Program is running.
""")
bot.run()
print('Program is closed.')

