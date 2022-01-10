import cv2
import pybot
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
#bot.run()
bot = pybot.PyBot(window_name)
bot.run(debug)
print('Program is closed.')
i = input("Press any key to end program.\n")